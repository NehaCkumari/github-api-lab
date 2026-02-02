import requests
from github_api_utils import make_headers

BASE_URL = "https://api.github.com"

def list_all_repos(username: str, per_page: int = 100) -> list[dict]:
    """
    Fetch all repos for a user by paginating through GitHub API results.
    """
    url = f"{BASE_URL}/users/{username}/repos"
    headers = make_headers()

    all_repos: list[dict] = []
    page = 1

    while True:
        params = {
            "per_page": per_page,   # max is 100 on GitHub
            "page": page,
            "sort": "updated",
        }

        response = requests.get(url, headers=headers, params=params, timeout=15)

        if response.status_code != 200:
            raise RuntimeError(
                f"Request failed on page {page}: {response.status_code} - {response.text}"
            )

        batch = response.json()

        # When GitHub returns an empty list, you're done.
        if not batch:
            break

        all_repos.extend(batch)
        page += 1

    return all_repos

if __name__ == "__main__":
    username = "NehaCkumari"
    repos = list_all_repos(username)

    print(f"Total repos fetched for {username}: {len(repos)}")
    print("First 10 repo names:")
    for r in repos[:10]:
        print("-", r["name"])
