FROM python:3.10-slim-bullseye

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY src /app
COPY run.sh /

RUN chmod +x run.sh

ENTRYPOINT ["./run.sh"]