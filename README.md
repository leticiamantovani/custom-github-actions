# 🚀 Pull Request Notifier (GitHub Action)

A robust, reusable GitHub Action that sends Pull Request notifications to **Slack**, **Discord**, or **Microsoft Teams** using customizable webhooks.

---

## Features

* 🔔 Automatic notifications on PR events (opened, closed, reopened, review requested, review request removed)
* 💡 Supports Slack, Discord, and Teams via webhooks
* ♻️ **Reusable GitHub Action**: plug-and-play in any repository
* ✅ Typed Python code with error handling, logging, and validation
* 📦 Ready for CI and linting
* 🔒 Secure integration with GitHub Secrets

---

## Inputs (Local Testing)

When running the action locally, you need to set the following environment variables:

| Name         | Required | Description                                              |
| ------------ | -------- | -------------------------------------------------------- |
| service      | Yes      | The notification service: `slack`, `discord`, or `teams` |
| webhook_url | Yes      | Webhook URL for the selected service                     |
| pr_title    | Yes      | Pull Request title                                       |
| pr_url      | Yes      | Pull Request URL                                         |
| pr_action   | Yes      | Pull Request action (`opened`, `closed`, etc.)           |
| pr_author   | Yes      | Author of the Pull Request                               |
| repo_name   | Yes      | GitHub repository name                                   |

> **ℹ️ Note:**
> You only need to provide these values manually when running or testing the action locally, **not** when using it inside a GitHub Actions workflow.

## Inputs (GitHub Action)

When using the action in a GitHub Actions workflow, you need to set the following inputs:

| Name         | Required | Description                                              |
| ------------ | -------- | -------------------------------------------------------- |
| service      | Yes      | The notification service: `slack`, `discord`, or `teams` |
| webhook_url | Yes      | Webhook URL for the selected service                     |

---

## Example Usage (as a reusable GitHub Action)

> **This project is a reusable GitHub Action.**
> When used in a GitHub Actions workflow, you do **not** need to set PR-related values manually.
> The GitHub Actions runner automatically provides all Pull Request information using built-in context variables.
> You can use as many services as you want in the same workflow, just define environment variables for each service.

```yaml
name: Pull Request Notifier

on:
  pull_request:
    types: [opened, closed, reopened, review_requested, review_request_removed]

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Notify on Slack
        uses: leticiamantovani/custom-github-actions@main
        with:
          service: 'slack'
          webhook_url: ${{ secrets.SLACK_WEBHOOK_URL }}
          pr_title: ${{ github.event.pull_request.title }}
          pr_url: ${{ github.event.pull_request.html_url }}
          pr_action: ${{ github.event.action }}
          pr_author: ${{ github.event.pull_request.user.login }}
          repo_name: ${{ github.repository }}
```

---

## How to Run Locally for Development

If you want to test the action outside of GitHub Actions (for example, during development), you must manually set the required environment variables:

```sh
# Example for Slack
export SERVICE=slack
export WEBHOOK_URL=https://hooks.slack.com/services/XXX/YYY/ZZZ
export PR_TITLE="Test PR"
export PR_URL="https://github.com/your-user/repo/pull/1"
export PR_ACTION=opened
export PR_AUTHOR=octocat
export GITHUB_REPOSITORY=your-user/repo

python -m notifier.main
```

Or with Docker:

```sh
docker build -t pr-notifier .
docker run --rm \
  -e SERVICE=slack \
  -e WEBHOOK_URL="https://hooks.slack.com/services/XXX/YYY/ZZZ" \
  -e PR_TITLE="Test PR" \
  -e PR_URL="https://github.com/your-user/repo/pull/1" \
  -e PR_ACTION="opened" \
  -e PR_AUTHOR="leticia" \
  -e GITHUB_REPOSITORY="your-user/repo" \
  pr-notifier
```

> Change `SERVICE` and `WEBHOOK_URL` as needed to test with Discord or Teams.

---

## Development & CI

* All code is typed and modular, ready for testing and CI
* Easily extensible for new integrations

---

## Security

* Webhook URLs and secrets are never logged or exposed
* All secrets are handled via GitHub Actions Secrets

---

### **Ready to use for any engineering team. Feel free to contribute or extend!**
