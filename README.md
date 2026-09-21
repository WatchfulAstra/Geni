# Savi Browser Agent

Savi Browser Agent is a lightweight MCP-based browser automation system.

It gives an AI agent direct control of a real Chromium browser through
Playwright and the Model Context Protocol (MCP).

The initial goal is simple:

> Let an AI open a website, interact with it, read the result, and provide
> a screenshot as visual evidence.

---

## Architecture

```text
AI Agent
   │
   │ MCP
   ▼
server.py
   │
   ▼
browser.py
   │
   ▼
Playwright
   │
   ▼
Chromium
   │
   ▼
Web
