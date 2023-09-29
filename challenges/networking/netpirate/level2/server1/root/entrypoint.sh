#!/bin/ash
trap "exit" SIGTERM

echo "info: started transmit loop"
while :; do
  PORT=$(shuf -n1 -i 49152-65535)

  echo "info: sending flag on port $PORT"
  echo "$FLAG" | nc -w3 -u entrypoint "$PORT" \
    || echo "warning: failed to send flag" &
  wait "$!"

  sleep "${FLAG_INTERVAL:-60}" & 
  wait "$!"
done
