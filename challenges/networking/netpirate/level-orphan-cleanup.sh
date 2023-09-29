#!/bin/sh
# This script removes all orphan levels
set -e

if [ "$(id -u)" -ne 0 ]; then
  sudo -ku root "$0" "$@"
  exit $?
fi

(
  cd "$(dirname -- "$(readlink -f "$0")")"

  if [ "$(docker compose ps -q | wc -l)" -ne 0 ]; then
    echo "Gateway is still running, please stop it before running this script!"
    exit 1
  fi

  for SESSION_ID in $(docker ps -af "label=com.docker.compose.project.environment_file=/levels/.env" --format "{{.Names}}" | cut -d"-" -f1-2 | sort -u); do
    echo "Found orphan session '$SESSION_ID', removing it.."
    LEVEL_NAME=$(echo -n "$SESSION_ID" | cut -d "-" -f1)
    (
      cd "$LEVEL_NAME"
      docker compose -p $SESSION_ID down -v -t0 &>/dev/null
    )
  done
)
