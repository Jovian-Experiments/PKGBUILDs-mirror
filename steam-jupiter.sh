#!/bin/bash

set -euo pipefail

STEAM_LINKS="$HOME"/.steam
STEAM_DIR="$HOME"/.local/share/Steam

(
  # On OOBE images we want to always start with a fresh steam per boot as we lack the proper steam overlay/repair code
  rm -rf --one-file-system "$STEAM_LINKS" "$STEAM_DIR"
)

# On OOBE images we prevent the bootstrapper from updating before starting steam
# Note that we still want the bootstrapper to run after startup so it can stage
# a client update for the next boot.
exec /usr/lib/steam/steam -steamdeck -skipinitialbootstrap "$@"
