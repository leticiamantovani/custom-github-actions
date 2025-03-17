import os
import json
import requests

# Get environment variables from GitHub Actions
slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")
pr_title = os.getenv("PR_TITLE")
pr_url = os.getenv("PR_URL")
pr_action = os.getenv("PR_ACTION")
pr_author = os.getenv("PR_AUTHOR")
repo_name = os.getenv("GITHUB_REPOSITORY")

# Map PR actions to friendly messages
action_messages = {
    "opened": "🚀 New Pull Request Opened!",
    "closed": "❌ Pull Request Closed!",
    "approved": "✅ Pull Request Approved!",
    "rejected": "⛔ Pull Request Rejected!"
}

# Slack message payload
slack_message = {
    "text": action_messages.get(pr_action, "🔄 Pull Request Update"),
    "attachments": [
        {
            "title": pr_title,
            "title_link": pr_url,
            "text": f"👤 Author: {pr_author}\n📂 Repository: {repo_name}",
            "color": "#36a64f"
        }
    ]
}

# Send the message to Slack
response = requests.post(slack_webhook_url, data=json.dumps(slack_message), headers={"Content-Type": "application/json"})

if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Failed to send message: {response.status_code}, {response.text}")
