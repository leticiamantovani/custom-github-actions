import os
import logging
import sys

from .services import get_service
from .message import build_message


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def get_env_var(var_name: str, required: bool = True) -> str:
    value = os.getenv(var_name)
    if not value and required:
        logging.error(f"Missing required env variable: {var_name}")
        sys.exit(1)
    return value or ""


def main():
    try:
        service = get_env_var("SERVICE")
        webhook_url = get_env_var("WEBHOOK_URL")
        pr_title = get_env_var("PR_TITLE")
        pr_url = get_env_var("PR_URL")
        pr_action = get_env_var("PR_ACTION")
        pr_author = get_env_var("PR_AUTHOR")
        repo_name = get_env_var("GITHUB_REPOSITORY")

        payload = build_message(
            pr_action, pr_title, pr_url, pr_author, repo_name
        )
        notifier = get_service(service)
        notifier.send(webhook_url, payload)

        logging.info(f"Notification sent to {service.capitalize()}.")
    except Exception as e:
        logging.error(f"Failed to send notification: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
