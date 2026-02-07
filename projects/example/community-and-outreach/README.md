# 社区传播与全平台运营指南 (Community & Outreach)

> **核心目标**：将本项目的决策逻辑（里子）转化为全平台影响力（面子），确保 12+ 篇深度内容与 6+ 次视频分发的高质量落地。

## 1. 目录结构与职能定义

### 📂 [platform-matrix/](./platform-matrix/) (跨平台文案矩阵)
用于存放针对不同平台特性微调后的稿件分身。
- **[social-media/](./platform-matrix/social-media/)**：
    - **小红书/即刻**：侧重“高信息密度卡片”与“情绪共鸣”，必须包含 5-8 个标签。
    - **X (Twitter)/Medium/V2EX**：海外分发重点，侧重“技术简洁性”与“开源价值观”。
- **[developer-communities/](./platform-matrix/developer-communities/)**：
    - **掘金/CSDN/思否/开源中国**：深度技术长文，必须包含代码块、架构图。

### 📂 [video-scripts/](./video-scripts/) (短视频与直播脚本)
- 存放 **B站/视频号/YouTube** 的脚本。
- 必须包含：分镜逻辑、画面描述（Demo 演示截图）、以及对应的录屏原始素材索引。

### 📂 [community-management/](./community-management/) (社群管理与交互)
- 存放 **微信群/飞书群/Discord/Telegram** 的互动模版。
- 包含：新功能发布话术、社区冲突处理逻辑、导师 QA 汇总。

### 📂 [web-assets/](./web-assets/) (Web 资产同步)
- 记录 **GitHub Discussions/Docs/Homepage** 的同步记录。
- 重点解决：如何将碎片化的日志整理为结构化的官方文档。

## 2. 内容流转全自动化流程 (The Pipeline)

1. **输入层**：从 `logs/` 提取决策关键点，从 `resources/` 提取 Demo 录屏或截图。
2. **加工层**：
    - **长文加工**：由技术决策记录转化为 3000 字左右的技术深度博文。
    - **视频加工**：提取 Demo 核心操作，配以语音讲解，生成 3 分钟内的短视频。
3. **分发层**：利用各平台 API 或分发工具，按“技术社群 -> 社交媒体 -> 官方 Web”的顺序分发。
4. **反馈层**：抓取各平台阅读/点赞数据，反哺至 `report/` 周报中。

## 3. 跟踪机制
所有分发链接必须携带 UTM 参数，以便在全自动化流程中识别流量来源。
- 格式示例：`https://project-site.com/?utm_source=juejin&utm_medium=article&utm_campaign=launch`

*Upstream Logbook | Powered by Upstream Labs*


