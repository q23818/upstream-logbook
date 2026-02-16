
# 社区传播执行索引 (Community & Outreach Index)

> **定位**：管理本项目特有的外宣资产，所有对外分发的稿件、脚本及执行状态的物理索引。

---

## 1. 物理目录结构 (Directory Tree)

```text
community-and-outreach/
├── platform-matrix/
│   ├── tech-communities/           # 技术社区 (逻辑性/干货): V2EX, 掘金, 思否, 开源中国, CSDN, Medium, Reddit
│   │   ├── csdn                   # 国内技术综合平台 (重 SEO/教程)
│   │   ├── oschina                # 国内技术综合平台 (重 SEO/教程)
│   │   ├── v2ex/                  # 程序员垂直社区 (重讨论质量，禁软文)
│   │   ├── juejin                 # 国内技术综合平台 (重 SEO/教程)
│   │   ├── segmentfault           # 国内技术综合平台 (重 SEO/教程)
│   │   ├── medium/                # 海外技术阵地 (重价值传递/Geek 属性)
│   │   ├── reddit/                # 海外技术阵地 (重价值传递/Geek 属性)
│   │   ├── chinaunix.net/         # 国内开源技术社区
│   │   ├── 51cto.com/             # 国内开源技术社区
│   │   ├── cnblogs.com/           # 国内技术博客平台：硬核的纯技术博客平台
│   │   ├── Dev.to/                # 国际版掘金
│   │   ├── Hacker News/           # 全球极客的圣地
│   │   ├── Product Hunt/          # 全球新产品首发的最高殿堂
│   │   └── reddit/                # 海外技术阵地 (重价值传递/Geek 属性)
│   └── social-content/             # 社交与内容平台 (传播性/共鸣): 公众号, 小红书, 知乎, X
│       ├── wechat/                 # 深度长文与行业思考
│       ├── zhihu/                  # 深度长文与行业思考
│       ├── xiaohongshu/            # 视觉化/划重点/高颜值内容
│       └── x/                      # 极简动态/全球视野
├── video/                           # 视频分发 (直观性/动态): B站, 视频号, YouTube脚本
│   ├── bilibili/                   # 国内主流视频渠道
│   ├── wechat/                     # 国内主流视频渠道
│   └── youtube/                    # 全球视频覆盖
├── community/                       # 社群交互 (私域/即刻响应): 微信群, 飞书群, Telegram, Discord
│   ├── wechat/                     # 国内社群 (高效协作/通知)
│   ├── feishu/                     # 国内社群 (高效协作/通知)
│   ├── discord/                    # 海外社群 (DAO 属性/社区文化)
│   └── telegram/                   # 海外社群 (DAO 属性/社区文化)
└── web-assets/                      # 官方 Web 资产同步: GitHub (Robius Org), Docs, Homepage
    ├── docs/                        # 官方docs
    ├── homepage/                    # 官方homepage
    └── github/                      # github
```

---

## 2. 资产分布

目录严格按照“内容形态”划分，所有产出的 Markdown 稿件及脚本必须存入对应位置：

### 📂 [platform-matrix/](./platform-matrix/) (跨平台文案矩阵)
用于存放针对不同平台特性微调后的稿件分身。
- **[social-content/](./platform-matrix/social-content/)**：
    - **小红书/即刻**：侧重“高信息密度卡片”与“情绪共鸣”，必须包含 5-8 个标签。
    - **X (Twitter)/Medium**：海外分发重点，侧重“技术简洁性”与“开源价值观”。
- **[tech-communities/](./platform-matrix/tech-communities/)**：
    - **V2EX/掘金/CSDN/思否/开源中国**：深度技术长文，必须包含代码块、架构图。

### 📂 [video-scripts/](./video/) (短视频与直播脚本)
- 存放 **B站/视频号/YouTube** 的脚本。
- 必须包含：分镜逻辑、画面描述（Demo 演示截图）、以及对应的录屏原始素材索引。

### 📂 [community/](./community/) (社群管理与交互)
- 存放 **微信群/飞书群/Discord/Telegram** 的互动模版和推送话术。
- 包含：新功能发布话术、社区冲突处理逻辑、导师 QA 汇总。

### 📂 [web-assets/](./web-assets/) (Web 资产同步)
- 记录 **GitHub Discussions/Docs/Homepage** 的同步记录。
- 重点解决：如何将碎片化的日志整理为结构化的官方文档。

---

## 3. 本项目执行目标 (KPI Checklist)

*请营员定期更新此表以同步执行进度：*

| 内容类型 | 指标要求 | 存放路径示例 | 完成状态 |
| :--- | :--- | :--- | :--- |
| **技术深度长文** | 12+ 篇 | `platform-matrix/tech-communities/2026-xx-xx-title.md` | [ ] |
| **多模态分身文案** | 对应 12 篇长文 | `platform-matrix/social-content/` 下的各平台版本 | [ ] |
| **短视频/演示脚本** | 6+ 次 | `video/bilibili/v1-demo.md` | [ ] |
| **官方文档同步** | 核心技术点同步 | `web-assets/docs/` 下的更新记录 | [ ] |

---

## 4. 核心执行入口 (Quick Links)

* **【操作指南】通用运营标准**：[publishing-standards.md](../../../methods/publishing-standards.md) (各平台怎么发、发哪里的标准)
* **【自动化流程】**：[content-pipeline.md](../../../methods/content-pipeline.md) (了解 ai 如何辅助生成稿件)
* **【原始素材】项目弹药库**：[resources/](../resources/) (引用原始录屏、截图、意向书原件)
* **【撰稿模板】标准草稿格式**：[template-content-draft.md](./template-content-draft.md) (新建稿件请基于此模板)
* **【数据记录】发布流水账**：[distribution-log.md](./distribution-log.md) (发布后立即在此登记 URL 及 UTM 数据，用于数据追踪)

---

*Upstream Logbook | Powered by Upstream Labs*

