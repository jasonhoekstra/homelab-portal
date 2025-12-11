#!/usr/bin/env python3
"""
Homelab Portal - Service launcher dashboard
"""

import os
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Service definitions with health check endpoints
SERVICES = [
    {
        "name": "Mattermost",
        "description": "Team chat and collaboration",
        "url": "http://mattermost.tailc328d1.ts.net:8065",
        "health_url": "http://mattermost.tailc328d1.ts.net:8065/api/v4/system/ping",
        "icon": "chat",
    },
    {
        "name": "Flowise",
        "description": "AI workflow builder",
        "url": "http://metatron.tailc328d1.ts.net:3000",
        "health_url": "http://metatron.tailc328d1.ts.net:3000/api/v1/ping",
        "icon": "robot",
    },
    {
        "name": "n8n",
        "description": "Workflow automation",
        "url": "http://n8n.tailc328d1.ts.net:5678",
        "health_url": "http://n8n.tailc328d1.ts.net:5678/healthz",
        "icon": "workflow",
    },
    {
        "name": "LM Studio",
        "description": "Local LLM inference",
        "url": "http://workstation-001.tailc328d1.ts.net:1234",
        "health_url": "http://workstation-001.tailc328d1.ts.net:1234/v1/models",
        "icon": "brain",
    },
    {
        "name": "Orchestrator",
        "description": "Claude Code agent manager",
        "url": "http://metatron.tailc328d1.ts.net:5556",
        "health_url": "http://metatron.tailc328d1.ts.net:5556/health",
        "icon": "server",
    },
]


def check_health(url: str, timeout: int = 3) -> bool:
    """Check if a service is healthy."""
    try:
        resp = requests.get(url, timeout=timeout)
        return resp.status_code < 500
    except Exception:
        return False


@app.route("/")
def index():
    """Render the dashboard."""
    return render_template("index.html", services=SERVICES)


@app.route("/api/health")
def health_check():
    """Return health status of all services."""
    results = {}
    for service in SERVICES:
        results[service["name"]] = check_health(service["health_url"])
    return jsonify(results)


@app.route("/api/health/<service_name>")
def service_health(service_name: str):
    """Return health status of a specific service."""
    for service in SERVICES:
        if service["name"].lower() == service_name.lower():
            return jsonify({
                "name": service["name"],
                "healthy": check_health(service["health_url"]),
            })
    return jsonify({"error": "Service not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
