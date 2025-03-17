# 🚀 GitHub Actions - Slack Pull Request Notifier

This repository contains a **GitHub Actions workflow** and a **Python script (`notify.py`)** to send notifications to a **Slack channel** whenever a Pull Request is **opened, closed, approved, or rejected** in a GitHub repository.

---

## 📌 Features
✅ **Automatic Slack notifications** when a PR is opened, closed, approved, or rejected.  
✅ **Reusable GitHub Action** that can be used across multiple repositories.  
✅ **Secure Webhook Integration** using GitHub Secrets.  
✅ **Customizable message formatting for Slack**.  

---

## 📜 How It Works

1. A **GitHub Actions workflow** triggers on Pull Request events.  
2. The workflow **extracts PR details** and sets environment variables.  
3. The `notify.py` script **sends a formatted message to Slack** via webhook.  

---

## 🛠️ Setup Instructions

### **1. Create a Slack Webhook URL**
- Go to [Slack API](https://api.slack.com/apps).
- Create a new app and enable **Incoming Webhooks**.
- Add a new **Webhook URL** to the desired Slack channel and copy the generated URL.

### **2. Add the Webhook URL as a GitHub Secret**
- In your GitHub repository, go to `Settings > Secrets and Variables > Actions > New repository secret`.
- Create a secret named **`SLACK_WEBHOOK_URL`** and paste the copied webhook URL.

### **3. Use the Workflow in Other Repositories**
In any repository where you want to use this Slack notification, create a workflow file:

📄 `.github/workflows/slack-notify.yml`:

```yaml
name: Call Slack Notification Workflow

on:
  pull_request:
    types:
      - opened
      - closed
      - review_requested
      - review_request_removed

jobs:
  call-slack-action:
    uses: your-username/github-actions-slack/.github/workflows/slack-notify.yml@main
    with:
      pr_title: ${{ github.event.pull_request.title }}
      pr_url: ${{ github.event.pull_request.html_url }}
      pr_action: ${{ github.event.action }}
      pr_author: ${{ github.actor }}
    secrets:
      SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
