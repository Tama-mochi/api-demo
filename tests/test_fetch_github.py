import pytest
from fetch_github import fetch_github_user

class FakeResp:
    def __init__(self, data):
        self._data = data
    def raise_for_status(self):
        pass
    def json(self):
        return self._data

def test_fetch_github_user_octocat(monkeypatch):
    # “octocat” の典型的な返却 JSON をモック
    fake_data = {
        "login": "octocat",
        "id": 583231,
        "public_repos": 8
    }
    # requests.get をモックして常に FakeResp(fake_data) を返す
    monkeypatch.setattr("requests.get", lambda *args, **kwargs: FakeResp(fake_data))

    result = fetch_github_user("octocat")
    # 整形後の辞書が期待どおりか検証
    assert result["login"] == "octocat"
    assert result["id"] == 583231
    assert result["public_repos"] == 8
