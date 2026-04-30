# Architecture

This project validated an AI office workflow in three layers:

1. **Agent reasoning layer**: Codex/OpenClaw-style model routing for planning, research, drafting, and tool decisions.
2. **Tool integration layer**: search APIs, Notion, YouTube, Firecrawl, GitHub, DOCX generation, and local file workflows.
3. **Delivery layer**: Feishu, WeChat, scheduled cron tasks, and a wearable-device bridge prototype.

## Runtime Flow

```mermaid
sequenceDiagram
    participant U as User
    participant A as Agent Gateway
    participant K as Knowledge Base
    participant S as Search APIs
    participant W as Writing Workflow
    participant D as Delivery Guard
    participant C as Channels

    U->>A: Request writing, news, or reminder task
    A->>K: Retrieve style, prior drafts, templates
    A->>S: Search and validate fresh sources
    A->>W: Draft structured output
    W->>A: Return article, brief, or plan
    A->>D: Queue scheduled or manual delivery
    D->>C: Send via Feishu / WeChat / wearable bridge
    D->>A: Write status, retry, and error logs
```

## Design Principles

- **Agent first, automation second**: let the model reason through the work before running fixed scripts.
- **Visible operations**: every scheduled job should leave logs that can be inspected.
- **Recoverable delivery**: push workflows need retry, dedupe, and fallback states.
- **Knowledge over prompts**: good writing quality depends on reusable examples, style rules, and source dossiers.
- **Separation of concerns**: Codex handles intelligence; MCP exposes tools; small services handle unattended scheduling.

