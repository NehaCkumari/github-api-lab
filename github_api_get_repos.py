import requests

BASE_URL = "https://api.github.com"

def list_repos(username: str, per_page: int = 5) -> list[dict]:
    url = f"{BASE_URL}/users/{username}/repos"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-api-lab",
    }
    params = {
        "per_page": per_page,   # how many results in one page (max 100)
        "sort": "updated"       # order repos by latest update
    }

    response = requests.get(url, headers=headers, params=params, timeout=15)

    if response.status_code != 200:
        raise RuntimeError(f"Request failed: {response.status_code} - {response.text}")

    return response.json()

if __name__ == "__main__":
    repos = list_repos("NehaCkumari", per_page=5)
    for r in repos:
        print(f'{r["name"]} | ⭐ {r["stargazers_count"]} | updated: {r["updated_at"]}')
