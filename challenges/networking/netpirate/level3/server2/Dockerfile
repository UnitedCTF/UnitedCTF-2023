FROM alpine:3.18.2

RUN apk add --no-cache \
      netcat-openbsd

COPY --chown=root:root ./root /

ENTRYPOINT [ "/entrypoint.sh" ]
