#!/usr/bin/env bash
# Rebuild the book: combined markdown, Word (.docx), EPUB and PDF.
# Run from manuscript/:  bash build.sh        (add "pdf" to also print a PDF via headless Edge)
# The file list is explicit, so interludes and Exploded Views are never missed.
set -e
cd "$(dirname "$0")"
FILES=(
  00-prologue.md
  01-the-forest-that-died.md
  02-every-good-regulator.md
  02a-what-if-thermostat.md
  03-the-jump.md
  03a-what-if-todo-app.md
  04-the-viable-system.md
  04b-exploded-view-company.md
  05-compliant-and-fatal.md
  06-the-fee-for-bug-reports.md
  07-the-presumption.md
  08-running-broken.md
  09-the-model-you-copied.md
  09b-exploded-view-alis.md
  10-the-ironies-of-automation.md
  10a-what-if-swap-jobs.md
  11-specify-or-explain.md
  12-who-may-stop-the-line.md
  12a-what-if-stop-the-company.md
  12b-exploded-view-factory.md
  13-grow-it-dont-design-it.md
  14-the-organisations-operating-system.md
  15-your-own-operating-system.md
  15b-exploded-view-personal.md
  16-epilogue.md
  16b-acknowledgements.md
  17-appendices.md
  18-index.md
  19-about-the-author.md
)
python figures/rotate_ev.py >/dev/null
[ -f figures/cover.png ] || echo 'cover.png missing: run python figures/cover.py and render it' >&2
python build/make_index.py >/dev/null
OUT=EVERY-GOOD-REGULATOR-full-draft.md
{ cat front-matter.md; for f in "${FILES[@]}"; do if [ -f "$f" ]; then cat "$f"; printf '\n\n'; else echo "MISSING: $f" >&2; fi; done; } > "$OUT.tmp"
mv "$OUT.tmp" "$OUT"
COMMON=(-f markdown-yaml_metadata_block --metadata-file=build/meta.yaml --lua-filter=build/pagebreak.lua --toc --toc-depth=1 --resource-path=.)
pandoc "$OUT" "${COMMON[@]}" -t docx --reference-doc=build/reference.docx -o EVERY-GOOD-REGULATOR.docx
cp EVERY-GOOD-REGULATOR.docx EVERY-GOOD-REGULATOR-full-draft.docx
pandoc "$OUT" "${COMMON[@]}" -t epub3 --css=build/book.css --epub-cover-image=figures/cover.png --split-level=1 -o EVERY-GOOD-REGULATOR.epub
if [ "$1" = "pdf" ]; then
  pandoc "$OUT" "${COMMON[@]}" -t html5 --standalone --embed-resources --css=build/book.css --include-before-body=build/cover.html -o build/book.html
  EDGE="/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
  "$EDGE" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="$(cygpath -w "$PWD/EVERY-GOOD-REGULATOR.pdf")" "file:///$(cygpath -m "$PWD/build/book.html")" >/dev/null 2>&1
  ls -la EVERY-GOOD-REGULATOR.pdf
fi
pandoc "$OUT" -f markdown-yaml_metadata_block -t plain 2>/dev/null | wc -w | sed 's/$/ words (as read)/'
