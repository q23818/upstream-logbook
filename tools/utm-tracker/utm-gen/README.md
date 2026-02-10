# UTM 链接生成器 (UTM Tracker Gen)

> **职能**：落实《分发策略》中的“跟踪机制”，确保所有外部流量均可回溯。

## 📖 为什么需要它？
为了沉淀“可复制的方法论”，我们不能仅凭感觉评估分发效果。本工具强制要求营员生成带有 UTM 标签的链接，从而在 `distribution-log.md` 中记录精确的转化数据。

## 🛠️ 使用说明
1. **环境准备**：确保本地已安装 Python 3.x。
2. **运行命令**：
```bash
python utm_gen.py <目标URL> <平台名> <项目名>
```

3. **参数规范**：
* `<目标URL>`：你要推广的官方 Web 资产（如 GitHub 或 Docs）。
* `<平台名>`：建议使用小写，如 `v2ex`, `juejin`, `zhihu`, `xhs`。
* `<项目名>`：当前执行的项目文件夹名，如 `makepad`。


## 🔄 应用场景

* **发布时**：将生成的链接嵌入技术博文、视频简介或社交动态。
* **登记时**：在 `projects/example/community-and-outreach/distribution-log.md` 登记该链接。


## 📅 未来扩展计划

* [ ] **Web 界面版**：为不熟悉终端的小白提供网页版生成界面。
* [ ] **自动缩短链接**：集成短链接生成 API。
* [ ] **数据看板对接**：直接将生成的链接同步至自动化分析工具。

---
*Upstream Logbook | Powered by Upstream Labs*

