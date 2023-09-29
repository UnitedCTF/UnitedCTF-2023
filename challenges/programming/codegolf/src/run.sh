
while :; do
    socat -dd -T300 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:"python3 app.py",stderr
done