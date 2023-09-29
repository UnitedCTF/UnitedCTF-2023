#!/bin/ash
trap "exit" SIGTERM

echo "info: started transmit loop"
while :; do
  echo "info: sending flag"
  echo "$FLAG" | nc -w3 entrypoint 1337 \
    || echo "warning: failed to send flag" &
  wait "$!"

  sleep "${FLAG_INTERVAL:-60}" &
  wait "$!"
done
