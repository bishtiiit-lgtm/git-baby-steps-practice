# Update Confluence Project Status

- Input format: project name, status period, Confluence page URL, summary of accomplishments, blockers, next steps, owner, and timestamp.
- Accept source data as short bullet points or a Markdown snippet for each section.
- Do not include secrets, tokens, or personal data beyond approved project ownership and names.
- Processing steps:
  + Read the target Confluence page and identify the existing project status section.
  + Replace the stale section or append a dated subsection for the current reporting period.
  + Keep only the latest status for each section: accomplishments, blockers, next steps.
  + Preserve the page structure, headers, and formatting used by the team.
  + Use a professional tone and concise factual language.
  + Include a timestamp and owner for the update.
- Output format:
  + `# Project Status - [Project Name]`
  + `## Period: [Start] to [End]`
  + `## Accomplishments`
  + `- ...`
  + `## Blockers`
  + `- ...`
  + `## Next Steps`
  + `- ...`
  + `## Updated By: [Owner]`
- Constraints:
  + Use Markdown only.
  + Use bullet points only under each section.
  + Keep the final update brief and scannable.
  + No fluff words, no long paragraphs, no tables.
  + Do not overwrite unrelated content on the page.
  + If required fields are missing, stop and ask for the missing inputs before publishing.
