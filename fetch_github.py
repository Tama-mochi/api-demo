import os
import requests

# 環境変数 GITHUB_TOKEN に設定したトークンを取得
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {TOKEN}"}

def fetch_github_user(username: str) -> dict:
    # ← username の部分に任意のGitHubユーザー名を入れて呼び出す
    url = f"https://api.github.com/users/{username}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()

    # ここでJSONから必要なキーを抜き出し、任意のフィールド名に変更して整形できる
    formatted = {
        # "login": data["login"],        ← 抽出したいキー名を任意に変更可能
        # "id": data["id"],              ← 抽出したいキー名を任意に変更可能
        # "public_repos": data["public_repos"],  ← 抽出したいキー名を任意に変更可能
        "ログイン名": data["login"],        # 例: ログイン名
        "フォロワー数": data["followers"],    # 例: フォロワー数
        "アカウント作成日時": data["created_at"],   # 例: アカウント作成日時
    }
    return formatted

if __name__ == "__main__":
    # 任意のユーザー名を指定して関数を呼び出し
    print(fetch_github_user("octocat"))
