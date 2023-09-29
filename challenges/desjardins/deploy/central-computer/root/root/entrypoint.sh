#!/bin/bash
for f in /root/entrypoint-init.d/*; do
    case "$f" in
       *.sh)     echo "$0: running $f"; . "$f" ;;
       *)        echo "$0: ignoring $f" ;;
    esac
    echo
done

sleep infinity
