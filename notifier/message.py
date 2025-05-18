from typing import Dict


def build_message(
    pr_action: str,
    pr_title: str,
    pr_url: str,
    pr_author: str,
    repo_name: str
) -> Dict:
    action_messages = {
        "opened": "🚀 New Pull Request Opened!",
        "closed": "❌ Pull Request Closed!",
        "approved": "✅ Pull Request Approved!",
        "rejected": "⛔ Pull Request Rejected!",
        "reopened": "🔄 Pull Request Reopened!",
        "review_requested": "👀 Pull Request Review Requested!",
        "review_request_removed": "❌ Review Request Removed!"
    }
    main_text = action_messages.get(pr_action, "🔔 Pull Request Update")

    return {
        "text": main_text,
        "attachments": [
            {
                "title": pr_title,
                "title_link": pr_url,
                "text": (
                    f"👤 Author: {pr_author}\n"
                    f"📂 Repository: {repo_name}"
                ),
                "color": "#36a64f"
            }
        ]
    }
