FROM ubuntu:18.04

LABEL maintainer="ovior <dany.gagnon.2@ens.etsmtl.ca>"
LABEL description="Default buffer overflow challenge"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    gcc \
    libc6-dev \
    libc6-dev-i386 \
    make \
    socat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /challenge

COPY precise_map.c /challenge/
COPY flag.txt /challenge/
COPY run.sh /challenge/

RUN gcc precise_map.c -o precise_map -fno-stack-protector -m32
RUN chmod +x run.sh

RUN chown root:root precise_map 
RUN chown root:nogroup flag.txt

RUN chmod 711 precise_map
RUN chmod 440 flag.txt

EXPOSE 1337

CMD ["./run.sh"]
