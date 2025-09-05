
import os
import requests
import base64

GITHUB_TOKEN = os.getenv("PRIMUS_TOKEN")
REPO = "your-username/primus-html"
BRANCH = "main"
API_URL = f"https://api.github.com/repos/{REPO}/contents/"

def push_file(filepath, message="Primus sync update"):
    filename = os.path.basename(filepath)
    with open(filepath, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf-8")

    data = {
        "message": message,
        "content": content,
        "branch": BRANCH
    }

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.put(API_URL + filename, json=data, headers=headers)
    return response.json()

if __name__ == "__main__":
    push_file("README.md")
