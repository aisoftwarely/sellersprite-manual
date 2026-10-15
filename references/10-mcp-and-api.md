# 10 · 把卖家精灵接入 AI 工作流（MCP 与开放 API）

> 官方接入指南：<https://www.sellersprite.com/v3/knowledge/feature/mcp-installation-tutorial>
> MCP 介绍：`/v3/mcp` ｜ 密钥管理：`/v3/mcp-manager?tab=keys` ｜ 开放 API：`https://open.sellersprite.com/api`

## 一、为什么对「多 Agent 切换」的用户尤其重要

如果经常在 ChatGPT、豆包、Coze、Cherry Studio、Claude Code、CodeBuddy、Codex、WorkBuddy 等不同 Agent 之间切换，**每次都要重新打开卖家精灵网页、手动查 ASIN、复制数据**，是最大的效率损耗。

接入 **卖家精灵 MCP** 后，可以直接在任意已配置的 AI 工具里用自然语言查询：

> 帮我用卖家精灵查询美国站 ASIN：B0DCZ2QFV8 的近 30 天销量。

AI 通过 MCP 获取数据并直接在对话中展示。

**MCP = 连接 AI 工具与卖家精灵的桥梁**：
- AI 工具：理解问题、展示结果；
- 卖家精灵：提供商品数据查询能力；
- MCP：让 AI 工具能调用卖家精灵的功能。

## 二、支持的 AI 客户端

| 类别 | 客户端 | 安装教程路径 |
|---|---|---|
| 聊天类 | ChatGPT 网页版 | `mcp-installation-tutorial-for-chatgpt` |
| 聊天类 | 豆包工作 | `mcp-installation-tutorial-for-doubao` |
| 聊天类 | 扣子 Coze | `mcp-installation-tutorial-for-coze` |
| 聊天类 | Chatbox | `mcp-installation-tutorial-for-chatbox` |
| 聊天类 | Cherry Studio | `mcp-installation-tutorial-for-cherrystudio` |
| 办公 Agent | **WorkBuddy** | `mcp-installation-tutorial-for-workbuddy` |
| 办公 Agent | Accio Work | `mcp-installation-tutorial-for-acciowork` |
| 编程类 | CodeBuddy 独立 IDE 版 | `mcp-installation-tutorial-for-codebuddy` |
| 编程类 | Antigravity IDE | `mcp-installation-tutorial-for-antigravity` |
| 编程类 | Codex | `mcp-installation-tutorial-for-codex` |
| 编程类 | Claude Code | `mcp-installation-tutorial-for-claudecode` |

> 教程 URL 前缀为 `https://www.sellersprite.com/v3/knowledge/feature/`。

## 三、安装前置准备

### 1. 获取连接信息

打开卖家精灵【MCP 密钥管理】页面并登录：`https://www.sellersprite.com/v3/mcp-manager?tab=keys`

两种接入方式：

| 方式 | 适用 | 操作 |
|---|---|---|
| 复制**快速集成 URL** | ChatGPT 网页版 | 找到【快速集成 URL】→ 点右侧【复制 URL】→ 填入 ChatGPT 的 MCP 创建窗口 |
| 复制 **AI 自动安装文案** | 支持自动配置的客户端 | 点【复制接入文案，交给 AI 自动配置】→【一键复制】→ 把完整文案发给对应 AI 工具 |

### 2. 准备 AI 客户端

确保目标 AI 工具已安装/登录，并具备 MCP 接入能力。不同客户端的 MCP 配置入口、授权方式、安装步骤不同。

### 3. ⚠️ 保护个人密钥

快速集成 URL、自动安装文案**可能包含个人密钥**：
- **不要**上传公共仓库；
- **不要**分享至群聊或公开页面；
- 仅在可信的个人客户端中配置。

> 对本仓库而言：把 MCP 密钥写进 `SKILL.md` 或 `references/` 并推送到 GitHub 是**高危操作**，务必避免。密钥只应存在于本机客户端的配置文件中。

## 四、验证接入成功

**第 1 步：确认连接器已启用**
进入 AI 客户端的 MCP / 连接器管理页，检查连接器 **`ss_mcp`** 是否已添加且处于正常连接或启用状态。

**第 2 步：查询一个商品**
在对话中输入：

> 调用卖家精灵 MCP 查询美国站 B0DCZ2QFV8 的标题和近 30 天销量。

若成功返回商品信息 → 本次查询正常运行。

> ⚠️ **只有实际调用工具并获得返回结果，才能确认数据查询可用**。仅看到连接器开启不代表每次查询都成功。

## 五、应用场景

| 场景 | 说明 |
|---|---|
| 快速查询商品数据 | 已知 ASIN 时，直接在 AI 对话中查询，不必切换到卖家精灵网页 |
| 整理查询结果 | 获取标题、销量等数据后，让 AI 整理为表格，便于阅读和记录 |
| 在 AI Agent 中使用商品数据 | 配置后让 Agent 在任务中调用卖家精灵商品查询工具 |

> 实际可执行的任务取决于客户端支持的工具调用能力，以及卖家精灵 MCP 返回的数据。

## 六、常见问题

| 问题 | 回答 |
|---|---|
| MCP 需要编程吗？ | 通常不需要。ChatGPT 网页版可用快速集成 URL，其他多个客户端支持复制安装文案完成配置 |
| 安装成功后能直接查销量吗？ | 可以尝试用自然语言调用。是否成功取决于连接状态、工具权限和接口实际返回结果 |
| 为什么 AI 无法调用？ | 先确认连接器是否启用，再检查当前对话或 Agent 是否有工具调用权限；仍失败则按客户端错误信息排查 |
| 密钥可以共享吗？ | **不建议**。连接信息可能包含个人密钥，应妥善保管，避免公开传播 |
| AI 给出了销量数字 = 安装成功？ | **不一定**。应确认客户端确实调用了 MCP 并成功返回对应 ASIN 的数据，**避免把模型自行生成的数字误当作查询结果** |
| 接入后还需要打开官网吗？ | MCP 已支持且能成功调用的数据查询可直接在 AI 客户端完成；其他操作是否仍需网页，取决于 MCP 实际提供的工具能力 |

## 七、开放 API（面向开发者）

- 文档：<https://open.sellersprite.com/api>
- 适用：需要自建数据管道、批量拉取、或把卖家精灵数据接入自有系统的场景。
- 与 MCP 的区别：MCP 面向「对话式 AI 客户端」即插即用；API 面向「程序化调用」，需要自己写请求与鉴权。

## 八、跨 Agent 使用的推荐做法

```
1. 在卖家精灵 MCP 密钥管理页生成一次连接信息
2. 对每个常用 Agent 分别完成一次 MCP 配置（ChatGPT / Claude Code / WorkBuddy / Codex ...）
3. 把本 skill 仓库放到各 Agent 都能读到的位置（或作为 git submodule / 复制到各自 skills 目录）
4. 查询数据走 MCP，方法论与字段解读走本 skill
```

> 这样在任意 Agent 中都能得到**同一套口径**的调研结论，避免不同工具间方法不一致。
