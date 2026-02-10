// 方案 B 核心逻辑：`tools/utm-tracker/utm-fetch/custom-proxy/worker.js`
// 这是一个运行在边缘节点的脚本。它不存储敏感信息，只负责“记账”和“转发”。

/**
 * Upstream 流量审计转发器
 * 实现逻辑：拦截带 UTM 的请求 -> 记录数据 -> 执行 302 重定向
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const params = url.searchParams;

    // 1. 提取 UTM 参数
    const source = params.get('utm_source') || 'unknown';
    const campaign = params.get('utm_campaign') || 'direct';
    const target = params.get('target'); // 目标跳转地址

    // 2. 数据审计记录 (此处以控制台输出为例，可接入数据库)
    console.log(`[Audit] Project: ${campaign} | Source: ${source} | Time: ${new Date().toISOString()}`);

    // 3. 逻辑校验：如果没有 target，默认跳转到组织的 GitHub 主页
    const finalDestination = target ? decodeURIComponent(target) : "https://github.com/YourOrg";

    // 4. 执行跳转
    return Response.redirect(finalDestination, 302);
  }
}

