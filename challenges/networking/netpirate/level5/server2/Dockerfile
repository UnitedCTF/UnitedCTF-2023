FROM alpine:3.18.2

RUN apk add --no-cache \
      python3

COPY --chown=root:root ./root /

ENV PYTHONUNBUFFERED=1
STOPSIGNAL SIGKILL
ENTRYPOINT [ "/entrypoint.sh" ]
