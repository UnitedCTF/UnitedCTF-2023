FROM alpine:3.18.2 AS base

RUN apk add --no-cache \
      vim nano tmux screen bash \
      tshark tcpdump nmap bind-tools \
      python3 ipython py3-pip

RUN python3 -m pip install --no-cache-dir scapy

# Build and install netfilterqueue
RUN apk add --no-cache \
      iptables libnetfilter_queue \
      gcc python3-dev musl-dev libnetfilter_queue-dev linux-headers
RUN python3 -m pip install --no-cache-dir netfilterqueue
RUN apk del --purge \
      gcc python3-dev musl-dev libnetfilter_queue-dev linux-headers

RUN rm -rf /root/.cache

FROM base

COPY --chown=root:root ./root /

WORKDIR /root
ENTRYPOINT [ "/entrypoint.sh" ]
