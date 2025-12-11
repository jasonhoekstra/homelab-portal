# Homelab Portal

Service launcher dashboard for the Buildway homelab. Accessible via Tailscale at `metatron.tailc328d1.ts.net:8080`.

## Services

| Service | URL | Description |
|---------|-----|-------------|
| Mattermost | mattermost.tailc328d1.ts.net:8065 | Chat |
| Flowise | metatron.tailc328d1.ts.net:3000 | AI Workflows |
| n8n | n8n.tailc328d1.ts.net:5678 | Automation |
| LM Studio | workstation-001.tailc328d1.ts.net:1234 | Local LLM |

## Quick Start

```bash
docker compose up -d
```

Access at http://metatron.tailc328d1.ts.net:8080

## Authentication

Uses Tailscale for network-level auth. Only devices on your tailnet can access.
