from flask import Flask, request, render_template
from fetch_github import fetch_github_user

app = Flask(__name__)

@app.route("/")
def index():
    # 入力フォームを返す
    return render_template("index.html")

@app.route("/user")
def user_query():
    # クエリパラメータ ?username=xxx を取得
    username = request.args.get("username", "").strip()
    if not username:
        return {"error": "username パラメータを指定してください"}, 400
    return fetch_github_user(username)

@app.route("/user/<username>")
def user_api(username):
    # 従来のパスパラメータ方式
    return fetch_github_user(username)

if __name__ == "__main__":
    app.run(debug=True)
