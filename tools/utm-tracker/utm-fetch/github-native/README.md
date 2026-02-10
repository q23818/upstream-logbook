# 方案 A：GitHub 原生流量审计 (GitHub Native Analytics)

> **定位**：零成本、零维护、小白营员首选的数据回收方案。

## 📖 实现原理
通过调用 GitHub REST API 的 Traffic 接口，识别过去 14 天内来自不同域名（如 `v2ex.com`, `zhihu.com`）向本仓库的跳转记录。虽然它无法精确到具体的一篇帖子（Campaign），但能反映出哪个平台在为你引流。


## 🛠️ 使用步骤
1. **准备 Token**：
   - 前往 GitHub [Personal Access Tokens](https://github.com/settings/tokens)。
   - 生成一个具有 `repo` 读取权限的 Token。
2. **运行脚本**：
   ```bash
   export GITHUB_TOKEN="你的Token"
   python fetch_github_stats.py
    ```

3. **数据登记**：
* 观察输出结果，重点关注 `Views`（总点击）和 `Uniques`（去重点击）。
* 将结果同步至 `projects/xxx/community-and-outreach/distribution-log.md`。
* **数据对比**：将脚本输出的 `Views` 数与你在 `distribution-log.md` 记录的平台点击数进行对比。


## ⚠️ 局限性

* **时效性**：GitHub 官方仅保存 **14 天** 内的数据，请务必每周运行一次并把结果手动同步至 `report/`。
* **精度**：无法识别 URL 中的 `?utm_campaign` 参数，只能识别到域名级别。


---
*Upstream Logbook | Powered by Upstream Labs*

