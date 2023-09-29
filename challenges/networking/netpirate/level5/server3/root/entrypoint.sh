#!/bin/ash

exec \
  dnsmasq \
    --no-daemon \
    --no-hosts \
    --no-negcache \
    --cache-size=0
