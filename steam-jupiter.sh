#!/bin/bash

set -euo pipefail

STEAM_LINKS="$HOME"/.steam
STEAM_DIR="$HOME"/.local/share/Steam

(
  # On OOBE images we want to always start with a fresh steam per boot as we lack the proper steam overlay/repair code
  rm -rf --one-file-system "$STEAM_LINKS" "$STEAM_DIR"

  # Similarly, on OOBE in this mode, always inhibit the bootstrapper
  # Also see steam-jupiter-stable's variant of this script, which looks for this marker
  mkdir -pv "$STEAM_DIR"
  echo -e "# OOBE Inhibit\nBootStrapperInhibitAll = enable" > "$STEAM_DIR"/Steam.cfg
)

exec /usr/lib/steam/steam -steamdeck "$@"
