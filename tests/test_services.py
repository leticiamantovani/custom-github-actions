import pytest
from notifier.services import get_service, SlackService, DiscordService, TeamsService
from unittest.mock import patch

def test_get_service_slack():
    service = get_service("slack")
    assert isinstance(service, SlackService)

def test_get_service_discord():
    service = get_service("discord")
    assert isinstance(service, DiscordService)

def test_get_service_teams():
    service = get_service("teams")
    assert isinstance(service, TeamsService)

def test_get_service_invalid():
    with pytest.raises(ValueError):
        get_service("unknown")

def test_slack_send_success():
    service = SlackService()
    payload = {"text": "hi"}
    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.raise_for_status = lambda: None
        service.send("http://fake-url", payload)
        mock_post.assert_called_once()