#!/usr/bin/env bash
# Installs REA (Reverse Engineer Anything, https://github.com/morluto/rea) and the
# Android engines it drives. Idempotent; safe to re-run in a fresh container.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BIN="$ROOT/tools/bin"
mkdir -p "$BIN"

REA_VERSION=6.4.0
JADX_MCP_URL=https://github.com/1013503897/jadx-headless-mcp/releases/download/v0.7.1/jadx-headless-mcp-0.7.1-all.jar
JADX_MCP_SHA=6e5eacf500b64292bfb73c49797c1958f6ee44646e43e868039ae7feb573ff75
APKTOOL_URL=https://github.com/iBotPeaches/Apktool/releases/download/v2.12.1/apktool_2.12.1.jar
JADX_URL=https://github.com/skylot/jadx/releases/download/v1.5.3/jadx-1.5.3.zip

command -v rea >/dev/null && [ "$(rea --version 2>/dev/null | tail -1)" = "$REA_VERSION" ] \
  || npm install -g "rea-agents@$REA_VERSION"

if [ ! -f "$BIN/jadx-headless-mcp-0.7.1-all.jar" ]; then
  curl -fsSL -o "$BIN/jadx-headless-mcp-0.7.1-all.jar" "$JADX_MCP_URL"
fi
echo "$JADX_MCP_SHA  $BIN/jadx-headless-mcp-0.7.1-all.jar" | sha256sum -c -

[ -f "$BIN/apktool.jar" ] || curl -fsSL -o "$BIN/apktool.jar" "$APKTOOL_URL"
cat > "$BIN/apktool" <<'SH'
#!/bin/sh
exec java -jar "$(dirname "$(readlink -f "$0")")/apktool.jar" "$@"
SH
chmod +x "$BIN/apktool"

if [ ! -x "$BIN/jadx/bin/jadx" ]; then
  curl -fsSL -o "$BIN/jadx.zip" "$JADX_URL"
  unzip -q -o "$BIN/jadx.zip" -d "$BIN/jadx" && rm "$BIN/jadx.zip"
  chmod +x "$BIN"/jadx/bin/*
fi

# Register the REA MCP server + skill for Claude Code at user level as well
# (the project-level .mcp.json and .claude/skills copy cover this repo).
rea setup --client claude_code --yes --json >/dev/null || true

cat <<MSG
REA ready. Export these before using the CLI:
  export REA_JADX_MCP_JAR=$BIN/jadx-headless-mcp-0.7.1-all.jar
  export REA_APKTOOL_COMMAND=$BIN/apktool
MSG
