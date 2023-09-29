#!/bin/bash
# Please dont kill me.. or you will lose your session
trap "exit" SIGTERM

# and it is useless to run me unless your are init
if [ "$$" -ne 1 ]; then
  exit 0
fi

while :; do
  sleep 300 &
  wait "$!"

  if [ "$(ps -o pid | wc -l)" -eq 5 ]; then
    exit 99
  fi
done
