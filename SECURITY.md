# Security And Sanitization

This repository is intentionally sanitized.

## Excluded

- API keys and OAuth tokens.
- Raw OpenClaw configuration.
- Feishu, WeChat, Rokid, Notion, GitHub, Firecrawl, Brave, and YouTube secrets.
- Private chat screenshots.
- Company source documents.
- Raw server archives.
- Personal identifiers that are not required to understand the architecture.

## Included

- Sanitized runtime evidence.
- Redacted log snippets.
- Example configuration with placeholders.
- Reusable documentation and workflow structure.
- Scripts for sanitizing logs and checking obvious secret patterns.

## Public Sharing Rule

If a file is not necessary for explaining the architecture, it should not be public. If a file contains operational evidence, it must be redacted before committing.

