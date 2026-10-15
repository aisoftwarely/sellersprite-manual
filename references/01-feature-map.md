# 01 · 功能全景图与入口

> 来源：卖家精灵功能手册 <https://www.sellersprite.com/v3/knowledge/feature/home>
> 本文件用于快速定位「某个需求该用哪个功能、入口在哪」。

## 一、功能分区总览

卖家精灵工具按六大分区组织：**大数据选品 / 关键词优化 / 运营推广 / 免费工具 / AI 解读 / 集成接入**。

### 1. 大数据选品

| 功能 | 入口 | 一句话用途 |
|---|---|---|
| 查竞品 | `/v3/competitor-lookup` | 按 ASIN / 关键词 / 品牌 / 卖家查竞品销量、BSR、价格、评论 |
| 选产品 | `/v3/product-research` | 微观选品：按销量/增长/评论/评分/价格/上架时间筛 ASIN |
| 选市场 | `/v3/market-research` | 宏观选品：按类目节点比对各维度指标选细分市场 |
| 关键词选品 | `/v2/keyword-research` | 需求端选品：从买家搜索行为发现市场机会 |
| ABA 数据选品 | `/v3/aba-research` | 基于亚马逊品牌分析（ABA）搜索词数据选品 |
| 外观专利 | `/v3/patent` | 查外观专利，规避侵权 |
| 全球商标库 | `/v3/branddb` | 查全球商标 |
| 产品库 | `/v3/product-store` | 沉淀自选产品样本池 |

### 2. 关键词优化

| 功能 | 入口 | 一句话用途 |
|---|---|---|
| 关键词挖掘 | `/v3/keyword-miner` | 以词拓词，构建关键词库；含「批量分析关键词」 |
| 关键词反查 | `/v3/keyword-reverse` | 单 ASIN 反查近 30 天搜索流量词 + 历史全量词导出 |
| 流量词对比 | `/v3/keyword-comparison` | 对比多个竞品的流量词覆盖差异 |
| 拓展流量词 | `/v3/traffic/extend` | 批量反查多个 ASIN（≤20）/ 全变体拓词 |
| 关键词转化率 | `/v3/keyword-conversion-rate` | 关键词转化相关数据 |
| 关键词收录（免费） | `/v2/keyword-checker` | 查产品被亚马逊收录了哪些关键词 |
| 关键词词库 | `/v3/keyword-store` | 沉淀、筛选、管理关键词资产 |
| 实时查竞价 | `/v3/real-time-bidding` | 查实时广告竞价 |

### 3. 运营推广

| 功能 | 入口 | 一句话用途 |
|---|---|---|
| 广告洞察 | `/v3/ads-insights` | 拆解竞品 SP/SBV 关键词广告架构 |
| 查流量来源 | `/v3/reversing` | 关键词或 ASIN 查搜索流量来源结构 |
| 关联流量 | `/v3/relation-keyword` | 查 ASIN 近 90 天关联曝光入口与免费/付费结构 |
| 出单词反查 | `/v2/aba/reverse/search` | 反查核心出单词（数据源为 ABA 搜索词） |
| AI 评论分析 2.0 | `/v3/ai-review-analysis` | AI 归纳买家评论：好评/差评/期待/人群/场景 |
| 产品监控 | `/v2/product-tracking` | 监控竞品 BSR/价格/评论数，每 24h 更新 |
| 关键词监控 | `/v2/keyword-tracking` | 监控关键词自然排名与广告排名 |
| 店铺上新监控 | `/v2/store-tracking` | 监控店铺上新频率与方向，每日更新 |

### 4. 免费工具

| 功能 | 入口 | 一句话用途 |
|---|---|---|
| Listing 生成器 | `/v3/listing-builder` | 生成 Listing 文案 |
| 销量预测 | `/v2/tools/sales-estimator` | 预估销量 |
| 利润计算器 | `/v3/calculator/index` | FBA 利润/利润率测算 |
| 折后价计算器 | `/v3/calculator/index?type=discount` | 折扣价测算 |
| Google Trends | `/blog/google-trends-for-sellersprite` | 站外趋势辅助判断季节性 |
| 链接生成器 | `/v3/link-builder` | 生成带追踪的链接 |
| 批量下载图片 | `/v3/batch-download-pictures` | 批量下载商品图 |
| TK 达人推广 | `mjjl.cn/xWynWM` | TikTok 达人推广资源 |

### 5. AI 解读

| 模块 | 入口（`/v3/ai-history?module=`） |
|---|---|
| 竞品运营拆解 | `KP` |
| 市场洞察 | `MA` |
| AI-找竞品 | `CL` |
| Listing 诊断 | `LA` |
| AI-拓产品 | `EP` |
| AI-关键词需求洞察 | `KRT` |

### 6. 集成接入

| 能力 | 入口 |
|---|---|
| MCP（接入 AI 工作流 / Agent） | `/v3/mcp`，接入指南 `/v3/knowledge/feature/mcp-installation-tutorial` |
| MCP 密钥管理 | `/v3/mcp-manager?tab=keys` |
| 开放 API | `https://open.sellersprite.com/api` |

### 7. 浏览器插件（v3.2.4）

| 能力 | 说明 |
|---|---|
| 插件介绍 / 下载 | `/cn/sellersprite-extension`、`/v3/knowledge/feature/sellersprite-chrome-extension-download` |
| 插件-产品库 | 在亚马逊页面直接采集样本 |
| 插件-市场分析 | 在亚马逊搜索结果页直接生成市场分析 |
| 插件-产品查询 / Keepa 替代 | 页面内查产品数据；Keepa 数据永久免费 |
| 插件-AI 评论分析 | 详情页内生成简版评论报告 |
| 插件-关键词收录 | 查关键词收录情况 |

> 插件数据（价格、BSR、关键词排名等）为**实时**抓取；其余为系统处理后的估算值。

## 二、按「我要做什么」选功能

| 我要… | 首选功能 | 辅助功能 |
|---|---|---|
| 判断某类目能不能做 | 选市场 → 市场分析报告 | 查竞品（关键词/品牌查）、利润计算器 |
| 找具体可做的 ASIN | 选产品（推荐模式） | 查竞品、产品对比、1688 找货源、利润计算器 |
| 从买家需求找机会 | 关键词选品、ABA 数据选品 | 关键词挖掘、选市场 |
| 建 Listing 关键词库 | 关键词挖掘 + 拓展流量词 | 关键词词库、流量词对比 |
| 分析竞品出单词 | 关键词反查、出单词反查 | 拓展流量词、流量词对比 |
| 拆竞品广告打法 | 广告洞察 | 查流量来源、关键词反查 |
| 找竞品流量入口 | 查流量来源、关联流量 | 广告洞察 |
| 找产品改进方向 | AI 评论分析 | 选产品（未被满足的市场） |
| 持续盯竞品 | 产品监控、关键词监控、店铺上新监控 | 关键词反查（历史趋势） |
| 算清楚能不能赚钱 | 利润计算器 | 销量预测 |

## 三、官方手册入口清单

| 手册页 | URL |
|---|---|
| 功能手册主页 | `/v3/knowledge/feature/home` |
| 快速入门 | `/v3/knowledge/guide` |
| 视频课堂 | `/v3/knowledge/video` |
| 运营干货 | `/v3/knowledge/operation` |
| 常见问题（使用与功能 FAQ） | `/v3/knowledge/feature/faq-for-cs` |
| 常见问题（账号/套餐） | `/cn/help/faq` |
| 子账号使用帮助 | `/v3/knowledge/feature/child-account-guide` |
| 企业账号认证及权益 | `/v3/knowledge/feature/enterprise-certification` |
| 数据更新说明 | `/cn/help?tag=数据更新` |
