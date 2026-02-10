import sys
import urllib.parse

def generate_utm_link(base_url, platform, campaign):
    """
    根据项目规范生成标准 UTM 追踪链接
    规范参考：publishing-standards.md
    """
    params = {
        "utm_source": platform,     # 投放平台 (如 v2ex, juejin)
        "utm_medium": "article",    # 内容媒介，默认为文章
        "utm_campaign": campaign,   # 任务/项目名 (如 makepad)
    }
    
    # 自动处理 URL 拼接逻辑
    url_parts = list(urllib.parse.urlparse(base_url))
    query = dict(urllib.parse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urllib.parse.urlencode(query)
    
    return urllib.parse.urlunparse(url_parts)

if __name__ == "__main__":
    # 极简交互：python utm_gen.py [URL] [平台] [项目名]
    if len(sys.argv) < 4:
        print("用法: python utm_gen.py <目标URL> <平台名> <项目名>")
        print("示例: python utm_gen.py https://github.com/upstream-labs v2ex makepad")
    else:
        final_link = generate_utm_link(sys.argv[1], sys.argv[2], sys.argv[3])
        print("\n🚀 生成的追踪链接如下：")
        print(f"{final_link}\n")
        print("请复制此链接用于分发，并填入 distribution-log.md")
