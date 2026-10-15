#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""卖家精灵功能手册同步检查脚本 (SellerSprite Manual Sync)

用途
----
检测卖家精灵官网功能手册（https://www.sellersprite.com/v3/knowledge/feature/home）
的新增 / 更新 / 下线文章，用于保持本 skill 与官网同步。

原理
----
官网页面为前端渲染（直接抓 HTML 只能拿到 JS 壳），因此改用站点地图
sitemap.xml —— 其中包含全部 /v3/knowledge/feature/ 文章 URL 及 lastmod 时间戳。

用法
----
    python scripts/sync_manual.py                 # 检测差异并输出报告
    python scripts/sync_manual.py --full          # 输出完整文章清单
    python scripts/sync_manual.py --json out.json # 同时导出 JSON 报告
    python scripts/sync_manual.py --no-save       # 只检测，不更新快照
    python scripts/sync_manual.py --watch core    # 只看核心功能相关文章的变更

退出码
------
    0  无变更
    1  检测到变更
    2  运行错误（网络失败等）

依赖：仅标准库。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

SITEMAP_URL = "https://www.sellersprite.com/sitemap.xml"
FEATURE_PREFIX = "/v3/knowledge/feature/"
MANUAL_HOME = "https://www.sellersprite.com/v3/knowledge/feature/home"

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SNAPSHOT = os.path.join(HERE, "manual_snapshot.json")

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

# 与 references/ 文件对应的核心功能关键词，用于 --watch core
CORE_KEYWORDS = [
    "market-research", "product-research", "competitor-lookup",
    "keyword-research", "keyword-miner", "keyword-reverse", "traffic-extend",
    "keyword-comparison", "keyword-store", "keyword-checker",
    "aba", "ads-insights", "reversing", "relation-keyword",
    "tracking", "store-tracking", "review-analysis",
    "calculator", "listing", "child-account", "mcp", "api",
    "sales-estimating", "faq",
]

URL_RE = re.compile(r"<url>\s*<loc>(.*?)</loc>\s*<lastmod>(.*?)</lastmod>", re.S)


def fetch(url: str, timeout: int = 30) -> str:
    """抓取 URL 文本；对 SSL 证书问题做一次宽松重试。"""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.URLError as exc:
        if "CERTIFICATE" in str(exc).upper():
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                return resp.read().decode("utf-8", errors="replace")
        raise


def parse_sitemap(xml: str) -> dict:
    """返回 {url: lastmod}，仅保留功能手册文章。"""
    out = {}
    for loc, lastmod in URL_RE.findall(xml):
        loc = loc.strip()
        if FEATURE_PREFIX in loc:
            out[loc] = lastmod.strip()
    return out


def load_snapshot(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        return data.get("articles", data) if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save_snapshot(path: str, articles: dict, source: str) -> None:
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": source,
        "count": len(articles),
        "articles": dict(sorted(articles.items())),
    }
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def slug(url: str) -> str:
    return url.rstrip("/").rsplit("/", 1)[-1]


def is_core(url: str) -> bool:
    low = url.lower()
    return any(k in low for k in CORE_KEYWORDS)


def build_report(old: dict, new: dict) -> dict:
    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    updated = sorted(u for u in set(old) & set(new) if old[u] != new[u])
    return {"added": added, "updated": updated, "removed": removed}


def print_report(rep: dict, old: dict, new: dict, core_only: bool) -> None:
    def flt(urls):
        return [u for u in urls if is_core(u)] if core_only else urls

    added, updated, removed = flt(rep["added"]), flt(rep["updated"]), flt(rep["removed"])
    scope = "（仅核心功能）" if core_only else ""

    print("=" * 68)
    print(f"卖家精灵功能手册同步检查{scope}")
    print(f"时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"官网文章总数：{len(new)}    上次快照：{len(old) if old else '无（首次运行）'}")
    print("=" * 68)

    if not old:
        print("\n首次运行：已建立基线快照，下次运行即可检测变更。")
        print(f"快照文件：{DEFAULT_SNAPSHOT}")
        return

    if not (added or updated or removed):
        print("\n✅ 未检测到变更，skill 内容与官网同步。")
        return

    if added:
        print(f"\n🆕 新增文章 {len(added)} 篇：")
        for u in added:
            print(f"   + {slug(u)}")
            print(f"     {u}")
    if updated:
        print(f"\n♻️  更新文章 {len(updated)} 篇：")
        for u in updated:
            print(f"   ~ {slug(u)}   {old.get(u, '?')} → {new.get(u)}")
            print(f"     {u}")
    if removed:
        print(f"\n❌ 下线文章 {len(removed)} 篇：")
        for u in removed:
            print(f"   - {slug(u)}")
            print(f"     {u}")

    print("\n" + "-" * 68)
    print("建议动作：")
    if added or updated:
        print("  1. 打开上述链接，确认是否属于本 skill 覆盖的功能范围；")
        print("  2. 若有新功能或口径变化，更新对应 references/*.md；")
        print("  3. 在 CHANGELOG.md 记录本次同步。")
    if removed:
        print("  4. 下线文章对应内容需从 references/ 中清理或标注失效。")


def main() -> int:
    ap = argparse.ArgumentParser(description="卖家精灵功能手册同步检查")
    ap.add_argument("--snapshot", default=DEFAULT_SNAPSHOT, help="快照文件路径")
    ap.add_argument("--full", action="store_true", help="输出完整文章清单")
    ap.add_argument("--json", metavar="PATH", help="把报告导出为 JSON")
    ap.add_argument("--no-save", action="store_true", help="不更新快照")
    ap.add_argument("--watch", choices=["all", "core"], default="all", help="只看全部或核心功能")
    args = ap.parse_args()

    print(f"正在抓取站点地图：{SITEMAP_URL}")
    try:
        xml = fetch(SITEMAP_URL)
    except Exception as exc:  # noqa: BLE001
        print(f"[错误] 抓取失败：{exc}", file=sys.stderr)
        print("提示：请检查网络连接；若处于受限网络，可稍后重试。", file=sys.stderr)
        return 2

    new = parse_sitemap(xml)
    if not new:
        print("[错误] 未解析到任何功能手册文章，官网结构可能已变更。", file=sys.stderr)
        print(f"请手动检查：{MANUAL_HOME}", file=sys.stderr)
        return 2

    old = load_snapshot(args.snapshot)
    first_run = not old
    rep = build_report(old, new)

    if args.full:
        print("=" * 68)
        print(f"功能手册完整清单（{len(new)} 篇）")
        print("=" * 68)
        for u, d in sorted(new.items(), key=lambda kv: kv[1], reverse=True):
            flag = "★" if is_core(u) else " "
            print(f"{flag} {d[:10]}  {slug(u)}")

    print_report(rep, old, new, core_only=(args.watch == "core"))

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(
                {
                    "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    "total": len(new),
                    "previous_total": len(old),
                    "changes": rep,
                },
                fh,
                ensure_ascii=False,
                indent=2,
            )
        print(f"\nJSON 报告已写入：{args.json}")

    if not args.no_save:
        save_snapshot(args.snapshot, new, SITEMAP_URL)
        print(f"快照已更新：{args.snapshot}")

    if first_run:
        return 0
    has_change = bool(rep["added"] or rep["updated"] or rep["removed"])
    return 1 if has_change else 0


if __name__ == "__main__":
    sys.exit(main())
