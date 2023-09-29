#!/bin/sh

while :; do
    socat -dd -T2 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:"python3 /app/chal1-intro-traitement_de_signaux.py",stderr
done