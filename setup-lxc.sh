#!/bin/bash
# Setup script for homelab-portal LXC
# Run as root on fresh Ubuntu 22.04 LXC

set -e

echo "=== Installing dependencies ==="
apt-get update
apt-get install -y curl git ca-certificates gnupg

echo "=== Installing Docker ==="
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

echo "=== Installing Tailscale ==="
curl -fsSL https://tailscale.com/install.sh | sh

echo "=== Connecting to Tailscale ==="
echo "Run: tailscale up"
echo "Then authenticate in browser"
echo ""
echo "=== After Tailscale is connected ==="
echo "Run these commands:"
echo ""
echo "  cd /opt"
echo "  git clone https://github.com/jasonhoekstra/homelab-portal.git"
echo "  cd homelab-portal"
echo "  docker compose up -d"
echo ""
echo "Portal will be at: http://portal.tailc328d1.ts.net:8080"
