import requests
import logging
from typing import Dict


class NotificationService:
    def send(self, webhook_url: str, payload: Dict) -> None:
        raise NotImplementedError


class SlackService(NotificationService):
    def send(self, webhook_url: str, payload: Dict) -> None:
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            webhook_url, json=payload, headers=headers, timeout=10
        )
        response.raise_for_status()
        logging.info("Slack notification sent.")


class DiscordService(NotificationService):
    def send(self, webhook_url: str, payload: Dict) -> None:
        discord_payload = {"content": payload.get("text")}
        response = requests.post(
            webhook_url, json=discord_payload, timeout=10
        )
        response.raise_for_status()
        logging.info("Discord notification sent.")


class TeamsService(NotificationService):
    def send(self, webhook_url: str, payload: Dict) -> None:
        teams_payload = {
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            "summary": payload.get("text"),
            "themeColor": "0076D7",
            "title": payload.get("attachments", [{}])[0].get("title"),
            "text": payload.get("attachments", [{}])[0].get("text"),
            "potentialAction": [
                {
                    "@type": "OpenUri",
                    "name": "View Pull Request",
                    "targets": [
                        {
                            "os": "default",
                            "uri": payload.get("attachments", [{}])[0]
                                   .get("title_link")
                        }
                    ]
                }
            ]
        }
        response = requests.post(
            webhook_url, json=teams_payload, timeout=10
        )
        response.raise_for_status()
        logging.info("Teams notification sent.")


def get_service(service: str) -> NotificationService:
    normalized = service.lower().strip()
    if normalized == "slack":
        return SlackService()
    elif normalized == "discord":
        return DiscordService()
    elif normalized == "teams":
        return TeamsService()
    else:
        raise ValueError(f"Unsupported notification service: {service}")
