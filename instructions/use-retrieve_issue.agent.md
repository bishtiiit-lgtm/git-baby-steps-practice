# Retrieve Jira Issues

- Use this instruction when current Jira issue details are needed for delivery reporting, risk analysis, or issue review.
- Run `tools/retrieve_issue.py` from the project root.
- Provide one or more Jira issue keys as positional arguments:
  - `python tools/retrieve_issue.py SAM1-123 KAN-456`
- Configure Jira authentication with these environment variables:
  - `JIRA_BASE_URL`: Jira site URL, such as `https://example.atlassian.net`.
  - `JIRA_EMAIL`: Jira account email.
  - `JIRA_API_TOKEN`: Jira API token.
- Optional flags `--base-url`, `--email`, and `--api-token` can override the environment variables for a single run.
- Read the JSON output for each issue's status, priority, assignee, due date, labels, estimates, update timestamp, and source URL.
- Treat an issue object containing `error` as a retrieval failure and report its issue key and error without discarding successful results.
- Keep API tokens out of command output, source files, and reports.
- Use the returned `source_url` when linking findings back to Jira.
