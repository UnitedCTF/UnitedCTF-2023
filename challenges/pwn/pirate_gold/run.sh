#!/bin/sh

BINARY=/challenge/pirate_gold
PORT=1337

while :; do
    socat -dd -T60 tcp-l:$PORT,reuseaddr,fork,keepalive,su=nobody exec:$BINARY,stderr 2> /dev/null
done
