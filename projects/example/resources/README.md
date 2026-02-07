
# 资源存放指南 (resources guide)

> **说明**：本目录用于存放项目过程中的静态资源。所有非文本类的“努力证明”与“资产”均应在此留存。


## 1. 关键商业资产清单 (Asset Checklist)
为了对齐商业化验证目标，请将以下文件存放在本目录：

* **调研与反馈**：
    * `local-research-report/`：本地调研报告、原始问卷数据分析。
    * `pilot-user-feedback/`：试点用户的访谈录音或反馈记录。
* **商业化文件**：
    * `business-plan/`：BP 草案及最终修订版。
    * `commercial-evidence/`：**付费意向书 (Letter of Intent)**、合作协议扫描件(pdf/jpg)。
* **多媒体资产**：
    * `branding/`：项目 Logo 原件、UI 设计稿、架构设计图。
    * `media/`：演示视频、直播录像、宣传海报、短视频分发脚本原件、技术直播的 ppt。


## 2. 命名与引用规范
* **全小写原则**：所有文件名使用小写字母，单词间用 `-` 连接。
* **时间戳前缀**：建议文件名以日期开头，方便追溯。
    * 示例：
    1. **付费意向书**：`2026-02-06-paid-intent-letter.pdf`
    2. **付费意向书**：`2026-02-06-letter-of-intent-company-name.pdf`
    3. **用户意见反馈**：`2026-02-06-user-interview-feedback.pdf`。
    4. **本地调研报告**：`2026-02-06-user-research-report.pdf`
    5. **BP 草案**：`2026-02-06-business-plan-draft-v1.pptx`

* **相对路径引用**：
    * 在你的`report/`（周报）或 `logs/`（决策日志）中提到这些进展时，请使用 Markdown 相对路径链接到这些文件。
    * 示例：`![架构图](../resources/system-architecture.png)`。
    * 示例：`[查看付费意向书](../resources/letter-of-intent-company-name.pdf)`。
* **隐私处理**：如果意向书涉及敏感商业条款，建议在上传前对关键敏感信息进行遮盖处理，或仅上传脱敏后的扫描件，以符合开源透明但不泄密的原则。

---
*Upstream Logbook | Powered by Upstream Labs*
