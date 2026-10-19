#!/usr/bin/env bash
set -euo pipefail
cd /workspace/VIDEOS
test -f evoquex-hyperframes-v15/package-lock.json || {
  echo "V15 sources are missing from the restored checkout; recover the published V15 branch without overwriting local changes."
  exit 1
}
for executable in node npm ffmpeg ffprobe chromium; do
  command -v "$executable" >/dev/null || {
    echo "Missing required executable: $executable"
    exit 1
  }
done
cd evoquex-hyperframes-v15
npm ci --cache /workspace/.npm --no-audit --no-fund
node scripts/hf.mjs doctor
