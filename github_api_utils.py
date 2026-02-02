import os

def make_headers() -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-api-lab",
    }

    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    return headers
