from flask import Flask
from fetch_github import fetch_github_user

app = Flask(__name__)

@app.route("/user/<username>")
def user_api(username):
    return fetch_github_user(username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
