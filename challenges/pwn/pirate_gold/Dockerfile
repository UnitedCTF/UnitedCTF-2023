FROM ubuntu:18.04

LABEL maintainer="ovior <dany.gagnon.2@ens.etsmtl.ca>"
LABEL description="pirate_gold challenge"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    gcc \
    make \
    socat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /challenge

COPY pirate_gold.c /challenge/
COPY flag.txt /challenge/
COPY run.sh /challenge/

RUN gcc pirate_gold.c -o pirate_gold
RUN chmod +x run.sh

RUN chown root:root pirate_gold 
RUN chown root:nogroup flag.txt

RUN chmod 711 pirate_gold
RUN chmod 440 flag.txt

EXPOSE 1337

CMD ["./run.sh"]
