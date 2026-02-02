import requests

BASE_URL = "https://api.github.com"

def get_user(username: str) -> dict:
    url = f"{BASE_URL}/users/{username}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-api-lab"
    }

    response = requests.get(url, headers=headers, timeout=15)

    # basic error handling
    if response.status_code != 200:
        raise RuntimeError(
            f"Request failed: {response.status_code} - {response.text}"
        )

    return response.json()

if __name__ == "__main__":
    user = get_user("NehaCkumari")  # try other usernames later
    print("login:", user["login"])
    print("name:", user["name"])
    print("public repos:", user["public_repos"])
    print("followers:", user["followers"])
