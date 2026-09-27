#!/usr/bin/env bash
# Render every figures/*.svg to a 2x PNG (for the docx build) using headless Edge.
# Run from anywhere: bash manuscript/figures/render.sh [dir]   (dir defaults to figures/; use comics/ for the strips)
set -e
cd "${1:-$(dirname "$0")}"
shopt -s nullglob
EDGE="/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
TMP="$(mktemp -d)"
for svg in fig-*.svg comic-*.svg; do
  png="${svg%.svg}.png"
  vb=$(grep -o 'viewBox="[^"]*"' "$svg" | head -1 | tr -d '"' | cut -d= -f2)
  w=$(echo "$vb" | awk '{print $3}'); h=$(echo "$vb" | awk '{print $4}')
  { echo "<html><body style='margin:0'><style>svg{display:block;width:${w}px;height:${h}px}</style>"; cat "$svg"; echo "</body></html>"; } > "$TMP/p.html"
  "$EDGE" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --window-size="${w},${h}" --screenshot="$(cygpath -w "$PWD/$png")" "file:///$(cygpath -m "$TMP/p.html")" >/dev/null 2>&1
  echo "rendered $png"
done
rm -rf "$TMP" 2>/dev/null || true
