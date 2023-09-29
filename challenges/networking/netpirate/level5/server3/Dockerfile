FROM alpine:3.18.2

RUN apk add --no-cache \
      dnsmasq

COPY --chown=root:root ./root /

ENTRYPOINT [ "/entrypoint.sh" ]
