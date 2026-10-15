# 卖家精灵功能手册 · SellerSprite Manual

> 把**卖家精灵（SellerSprite）**官网功能手册的功能体系、操作路径、指标口径与调研方法论，整理成一套可被任意 AI Agent 直接调用的 **Agent Skill**。
> 面向亚马逊（尤其**美国站**）的产品调研与市场调研场景。

**关于仓库名**：GitHub 仓库名只能使用 ASCII 字符（字母、数字与 `.` `-` `_`），因此英文名为 `sellersprite-manual`；中文名「卖家精灵功能手册」体现在本标题与仓库 Description。

[![Skill](https://img.shields.io/badge/type-Agent%20Skill-blue)]()
[![Lang](https://img.shields.io/badge/lang-中文-green)]()
[![License](https://img.shields.io/badge/license-MIT-lightgrey)]()

---

## 这是什么

一个**知识 + 方法论型**的 Agent Skill。它不代替你登录卖家精灵、不抓取你的账号数据，而是让 AI Agent 知道：

- **用哪个功能**解决什么问题；
- **怎么设置筛选条件**（推荐模式与自定义参数的具体数值）；
- **结果字段怎么读**、哪些指标容易被误读；
- 什么样的结论**可以下**、什么样只能算**待验证假设**。

设计目标是让你在 ChatGPT / Claude Code / CodeBuddy / WorkBuddy / Codex 等**不同 Agent 之间切换时，得到同一套口径的调研结论**。

## 特性

| 能力 | 说明 |
|---|---|
| 端到端工作流 | 市场调研、产品调研、关键词与竞品调研、监控复盘四大 Playbook |
| 指标口径表 | 每个字段的定义 + 正确解读 + 常见误读（含「自然+广告 > 100%」等陷阱） |
| 真实参数 | 推荐选品模式的完整筛选条件（销量、增长率、评分、价格、上架时间、配送方式） |
| 账号规则 | 子账号权限、套餐额度、导出限制、9 站支持范围 |
| 导出指引 | 「导出」vs「导出明细」的判断标准、勾选项冲突、各模块规则与省配额技巧 |
| 数据时效 | 插件实时 / 销量每日 / 关键词库每月 / 趋势选品每周 / 反查每日滚动 |
| AI 集成 | 卖家精灵官方 MCP 与开放 API 的接入方式与密钥安全 |
| 自动同步 | 脚本检测官网手册的新增 / 更新 / 下线文章 |

## 目录结构

```
sellersprite-manual/
├── SKILL.md                          # 主文件：触发条件、核心工作流、资源索引
├── README.md
├── CHANGELOG.md
├── LICENSE
├── .gitignore
├── references/
│   ├── 01-feature-map.md             # 功能全景图 + 全部入口 URL
│   ├── 02-market-research.md         # 选市场 · 市场分析报告九大维度
│   ├── 03-product-research.md        # 选产品 · 查竞品 · 历史趋势
│   ├── 04-keyword-research.md        # 关键词选品/ABA · 挖掘 · 反查 · 拓展 · 对比
│   ├── 05-traffic-and-ads.md         # 查流量来源 · 广告洞察 · 关联流量
│   ├── 06-tracking-monitoring.md     # 产品/关键词/店铺监控
│   ├── 07-review-and-listing.md      # AI 评论分析 · Listing 生成与诊断
│   ├── 08-tools-and-profit.md        # 利润计算器 · 免费工具
│   ├── 09-account-quota-data.md      # 子账号 · 套餐 · 额度 · 数据更新频率
│   ├── 10-mcp-and-api.md             # MCP 接入 · 开放 API · 密钥安全
│   ├── 11-metrics-glossary.md        # 指标术语表与防误读清单
│   └── 12-export-guide.md            # 导出 vs 导出明细：怎么选、规则、省配额
└── scripts/
    ├── sync_manual.py                # 官网手册同步检查脚本
    └── manual_snapshot.json          # 同步基线快照
```

## 安装

本仓库是一个标准 Agent Skill 目录（`SKILL.md` + `references/` + `scripts/`），把它放到你所使用 Agent 的 skills 目录即可。

```bash
git clone https://github.com/aisoftwarely/sellersprite-manual.git
```

常见 Agent 的 skills 目录：

| Agent | 目录 |
|---|---|
| Claude Code | `~/.claude/skills/` |
| WorkBuddy | `~/.workbuddy-ai/skills/` |
| 其他支持 Agent Skills 的工具 | 该工具文档指定的 skills / context 目录 |

```bash
# 以 WorkBuddy 为例
cp -r sellersprite-manual ~/.workbuddy-ai/skills/
```

> 若不支持 Skill 机制，也可直接把 `SKILL.md` 内容作为系统提示或项目说明喂给 Agent。

### 可选：接入卖家精灵 MCP（强烈推荐）

如果你经常在不同 Agent 之间切换，配置 **MCP** 可以让 Agent 直接查询数据，而不必每次手动开网页。

1. 登录卖家精灵 [MCP 密钥管理](https://www.sellersprite.com/v3/mcp-manager?tab=keys) 获取连接信息；
2. 按官方教程为每个常用客户端各配置一次：<https://www.sellersprite.com/v3/knowledge/feature/mcp-installation-tutorial>；
3. 验证：在对话中让 Agent 查询某个 ASIN 的销量，确认连接器 `ss_mcp` 正常工作。

> ⚠️ **连接信息可能包含个人密钥，切勿提交到本仓库或任何公开位置。** 详见 `references/10-mcp-and-api.md`。

## 使用示例

安装后，可以直接这样提问：

```
帮我调研亚马逊美国站「pet backpack」这个品类值不值得做，
用卖家精灵的数据给出市场容量、竞争格局和利润空间的判断。
```

```
反查竞品 ASIN B07Z82895W 的核心出单词，并分析它投了哪些广告类型。
```

```
我想做一款瑜伽垫，帮我建一个关键词库并筛出适合前期主推的长尾词。
```

```
我是卖家精灵子账号，导出数据有什么限制？监控额度够用吗？
```

```
我要导出关键词反查的数据，该点「导出」还是「导出明细」？
```

Agent 会按 `SKILL.md` 中的工作流调用对应功能，并引用 `references/` 中的字段口径给出结论。

## 与官网同步

官网功能手册：<https://www.sellersprite.com/v3/knowledge/feature/home>

```bash
python scripts/sync_manual.py            # 检测新增/更新/下线文章
python scripts/sync_manual.py --full     # 输出完整文章清单
python scripts/sync_manual.py --watch core   # 只看核心功能相关变更
```

脚本原理：官网页面为前端渲染（直接抓 HTML 只能拿到 JS 壳），因此改用**站点地图 `sitemap.xml`**，其中包含全部 `/v3/knowledge/feature/` 文章 URL 及其 `lastmod` 时间戳，与 `scripts/manual_snapshot.json` 快照对比。

退出码：`0` 无变更 ｜ `1` 检测到变更 ｜ `2` 运行错误。可用于 CI 或定时任务。

检测到变更后的处理流程：

1. 打开变更链接，判断是否属于本 skill 覆盖范围；
2. 若是新功能或口径变化 → 更新对应 `references/*.md`；
3. 在 `CHANGELOG.md` 记录本次同步；
4. 提交并推送。

## 内容覆盖范围

- **大数据选品**：选市场、选产品、查竞品、关键词选品、ABA 数据选品、外观专利、全球商标库、产品库
- **关键词优化**：关键词挖掘、关键词反查、流量词对比、拓展流量词、关键词转化率、关键词收录、关键词词库、实时查竞价
- **运营推广**：广告洞察、查流量来源、关联流量、出单词反查、AI 评论分析、产品监控、关键词监控、店铺上新监控
- **免费工具**：利润计算器、销量预估、折后价计算器、Listing 生成器、链接生成器、批量下载图片、Google Trends
- **AI 解读**：竞品运营拆解、市场洞察、AI-找竞品、Listing 诊断、AI-拓产品、AI-关键词需求洞察
- **账号与集成**：子账号、套餐额度、数据更新频率、MCP、开放 API

## 免责声明

- 本项目为**非官方**整理，与卖家精灵（SellerSprite）官方无隶属关系。
- 所有功能、参数、额度与数据更新频率**以官网实时说明为准**；官网调整后请运行同步脚本更新本仓库。
- 本仓库**不包含**任何账号凭证、MCP 密钥或用户数据。
- 调研结论仅供参考，不构成投资或经营建议。任何进入市场的决策需自行评估竞争、合规、供应链、库存与广告成本风险。

## License

[MIT](LICENSE)
