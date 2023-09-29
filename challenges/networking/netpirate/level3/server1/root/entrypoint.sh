#!/bin/ash
trap "exit" SIGTERM

sleep 10 &
wait "$!"

echo "info: started transmit loop"
while :; do
  echo "info: sending flag"
  echo "$FLAG" | nc -w3 -u server2 1337 \
    || echo "warning: failed to send flag" &
  wait "$!"

  sleep "${FLAG_INTERVAL:-60}" &
  wait "$!"
done
