import requests
import os

# 配置信息（建议通过环境变量管理）
REPO_OWNER = "YourOrg"
REPO_NAME = "YourRepo"
# 需要在 GitHub Settings -> Developer settings -> Personal access tokens 申请
TOKEN = os.getenv("GITHUB_TOKEN") 

def get_referring_sites():
    """
    抓取过去 14 天内引流至 GitHub 的来源站点数据
    """
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/traffic/popular/referrers"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

if __name__ == "__main__":
    if not TOKEN:
        print("⚠️ 请先设置环境变量：export GITHUB_TOKEN='你的TOKEN'")
    else:
        stats = get_referring_sites()
        if stats:
            print(f"\n📊 GitHub 流量来源审计报告 (过去 14 天)")
            print(f"| 来源站点 | 总访客 (Views) | 独立访客 (Uniques) |")
            print(f"| :--- | :--- | :--- |")
            for site in stats:
                print(f"| {site['referrer']} | {site['count']} | {site['uniques']} |")
            print("\n✅ 请将上述表格填入对应项目的 distribution-log.md 或 report/ 中")

