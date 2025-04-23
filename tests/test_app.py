# tests/test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_user_query_param(client, monkeypatch):
    # fetch_github_user をモック
    monkeypatch.setattr("fetch_github.fetch_github_user", lambda u: {"login": u})
    resp = client.get("/user?username=testuser")
    assert resp.status_code == 200
    assert resp.json["login"] == "testuser"
