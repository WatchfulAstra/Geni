# Savi Browser Agent — MCP

## Purpose

Savi Browser Agent exposes a Chromium browser to an AI through the Model
Context Protocol (MCP).

The MCP server is the bridge between the AI and Playwright.

```text
AI
 │
 │ MCP
 ▼
Savi Browser Agent
 │
 │ Playwright
 ▼
Chromium
 │
 ▼
Website
