# algorithmresearch

Private working space for reverse-engineering research.

## Tooling

- **REA — Reverse Engineer Anything** ([morluto/rea](https://github.com/morluto/rea), npm `rea-agents@6.4.0`)
  is registered for Claude Code via `.mcp.json` (MCP server `rea`) and its workflow skill is vendored at
  `.claude/skills/reverse-engineer-anything/`.
- `tools/setup.sh` installs REA plus the Android engines it drives (audited jadx-headless-mcp 0.7.1 JAR,
  Apktool 2.12.1) and the standalone JADX 1.5.3 CLI used for bulk decompilation. Run it in each fresh container.
- `scripts/` holds the analysis helpers (APK identity/signature check, manifest audit, Exodus tracker scan,
  pattern scan over decompiled trees).

Downloaded APKs (`apks/`), decompiler output (`work/`) and tool binaries (`tools/bin`) are git-ignored.
