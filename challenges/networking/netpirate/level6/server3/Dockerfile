FROM alpine:3.18.2

RUN apk add --no-cache \
      dnsmasq ipcalc iptables

COPY --chown=root:root ./root /

ENTRYPOINT [ "/entrypoint.sh" ]
