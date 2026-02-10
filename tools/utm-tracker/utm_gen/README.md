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


## 📅 未来扩展计划

* [ ] **Web 界面版**：为不熟悉终端的小白提供网页版生成界面。
* [ ] **自动缩短链接**：集成短链接生成 API。
* [ ] **数据看板对接**：直接将生成的链接同步至自动化分析工具。

---

## UTM使用指南

**UTM (Urgency Tracking Module)** 让你精准识别哪些流量来自 V2EX，哪些来自知乎，从而判断不同平台的运营效率。

以下是小白营员的使用指南：

### 1. 核心逻辑

通过在目标 URL 后添加特定参数，将原本模糊的访问记录转化为可分析的数据。

* **示例链接**：`https://project.com/?utm_source=juejin&utm_medium=article&utm_campaign=launch`

---

### 2. 实操步骤：使用 `utm_gen.py` 自动化生成

为了防止手动拼接链接出错，小白营员应统一使用基础设施中的工具：

1. **定位路径**：进入目录 `methods-and-tools/infrastructure/utm-tracker/`。
2. **执行命令**：
```bash
python utm_gen.py [目标URL] [分发平台] [项目/任务名]

```


3. **参数对齐**：
* **目标URL**：通常是项目的 GitHub 仓库或官方 Docs 链接。
* **分发平台**：填入你即将发帖的平台（如 `v2ex`, `zhihu`, `juejin`）。
* **项目/任务名**：当前的 Campaign 名称（如 `makepad-performance`）。

---

### 3. 应用场景与闭环记录

* **发布时**：将生成的带 UTM 标签的链接嵌入到你的技术博文、视频简介或社交动态中。
* **登记时**：在 `projects/example/community-and-outreach/distribution-log.md` 登记该链接。
* **复盘时**：后期通过分析工具抓取这些标签，统计出哪个平台的回流率最高，并同步至 `report/`。

---
*Upstream Logbook | Powered by Upstream Labs*

