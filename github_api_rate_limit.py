import requests
from github_api_utils import make_headers

BASE_URL = "https://api.github.com"

def get_rate_limit() -> dict:
    url = f"{BASE_URL}/rate_limit"
    headers = make_headers()

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = get_rate_limit()
    core = data["resources"]["core"]
    print("limit:", core["limit"])
    print("remaining:", core["remaining"])
    print("reset:", core["reset"])
