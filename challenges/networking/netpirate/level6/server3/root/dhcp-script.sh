#!/bin/sh

case "$1" in
  add)
    echo "info: locking $3 to $2"
    arp -s "$3" "$2" 2>/dev/null || true
  ;;
  del)
    echo "info: freeing $3"
    arp -d "$3" 2>/dev/null || true
  ;;
esac
