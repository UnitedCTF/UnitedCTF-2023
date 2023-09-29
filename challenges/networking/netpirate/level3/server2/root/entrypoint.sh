#!/bin/ash
trap "exit" SIGTERM

echo "info: started receive loop"
while :; do
  echo "info: listening for flag"
  nc -w3 -u -l 1337 2>/dev/null | \
    while read line; do
      echo "info: got flag $line";
    done &
  wait "$!"
done
