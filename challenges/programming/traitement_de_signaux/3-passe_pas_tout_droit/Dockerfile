FROM python:3.10-slim-bullseye

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install scipy

COPY src/chal3-traitement_de_signaux.py /app/chal3-traitement_de_signaux.py
COPY chemin.wav /chemin.wav
COPY run.sh /


RUN chmod +x run.sh

ENTRYPOINT ["./run.sh"]