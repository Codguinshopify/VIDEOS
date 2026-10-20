#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
ffmpeg -hide_banner -v error -y -framerate 5 -pattern_type glob -i 'assets/3d/shot-*.png' \
  -vf 'minterpolate=fps=30:mi_mode=mci:mc_mode=obmc:me_mode=bidir,tpad=stop_mode=clone:stop_duration=1.4,scale=1080:1920,format=yuv420p' \
  -r 30 -t 8 -c:v libx264 -preset fast -crf 18 -g 30 -keyint_min 30 -sc_threshold 0 -movflags +faststart -an assets/phone-arrow-target.mp4
