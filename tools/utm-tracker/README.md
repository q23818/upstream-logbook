# 📊 流量追踪与数据回流系统 (UTM Tracker Hub)

> **职能**：落实《分发策略》中的“跟踪机制”，确保所有外部流量均可回溯。

## 📖 闭环逻辑
为了沉淀“可复制的方法论”，我们不能仅凭感觉评估分发效果。本系统将流量管理分为两个阶段：

1.  **分发阶段 (utm-gen)**：强制要求营员生成带有 UTM 标签的链接，从而在分发时植入标记。
2.  **回收阶段 (utm-fetch)**：通过抓取工具提取回流数据，将统计到的“点击 -> Star/Fork”转化率写进 `report/` 周报中。

## 📂 模块说明
* **[`/utm-gen`](./utm-gen/README.md)**：UTM 链接生成工具。解决“链接拼写错、不规范”的问题。
* **[`/utm-fetch`](./utm-fetch/README.md)**：数据回收方案矩阵（方案 A/B/C）。解决“数据拿不到、统计难”的问题。

## 📈 数据回收 SOP (How to Close the Loop)
1.  **初级（手动）**：发布 48 小时后，观察平台互动数，填入 `distribution-log.md`。
2.  **进阶（自动化）**：使用 `utm-fetch` 中的脚本导出对应 `utm_source` 的点击量。
3.  **闭环（复盘）**：将数据同步至 `report/` 目录下的周报中，作为决策依据。

---
*Upstream Logbook | Powered by Upstream Labs*


-------------------------------------------------------

## UTM使用指南

**UTM (Urgency Tracking Module)** 让你精准识别哪些流量来自 V2EX，哪些来自知乎，从而判断不同平台的运营效率。

以下是小白营员的使用指南：

### 1. 核心逻辑

通过在目标 URL 后添加特定参数，将原本模糊的访问记录转化为可分析的数据。

* **示例链接**：`https://project.com/?utm_source=juejin&utm_medium=article&utm_campaign=launch`

---

### 2. 实操步骤：使用 `utm_gen.py` 自动化生成

为了防止手动拼接链接出错，小白营员应统一使用基础设施中的工具：

1. **定位路径**：进入目录 `tools/tools/utm-tracker/`。
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

