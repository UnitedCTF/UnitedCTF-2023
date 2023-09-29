#!/bin/sh

while :; do
    socat -dd -T1800 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:"python3 /app/main.py",stderr
done