from notifier.message import build_message

def test_build_message_opened():
    payload = build_message(
        pr_action="opened",
        pr_title="Add feature X",
        pr_url="https://github.com/org/repo/pull/1",
        pr_author="octocat",
        repo_name="org/repo"
    )
    assert payload["text"] == "🚀 New Pull Request Opened!"
    assert payload["attachments"][0]["title"] == "Add feature X"
    assert "octocat" in payload["attachments"][0]["text"]

def test_build_message_default_action():
    payload = build_message(
        pr_action="unknown_event",
        pr_title="Test",
        pr_url="url",
        pr_author="test",
        repo_name="repo"
    )
    assert payload["text"] == "🔔 Pull Request Update"
