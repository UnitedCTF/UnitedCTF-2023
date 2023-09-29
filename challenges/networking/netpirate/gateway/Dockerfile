FROM alpine:3.18.2

RUN apk add --no-cache \
      openssh sudo \
      docker-cli docker-compose \
      curl jq

COPY --chown=root:root ./root /

STOPSIGNAL SIGTERM
ENTRYPOINT [ "/entrypoint.sh" ]
