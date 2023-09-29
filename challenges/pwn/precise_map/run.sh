#!/bin/sh

BINARY=/challenge/precise_map
PORT=1337

while :; do
    socat -dd -T60 tcp-l:$PORT,reuseaddr,fork,keepalive,su=nobody exec:$BINARY,stderr 2> /dev/null
done
