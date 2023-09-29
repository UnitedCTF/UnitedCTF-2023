FROM python:3.8.5-alpine

WORKDIR /app

COPY src/ .

RUN addgroup -S group && \
    adduser -S -G group johndoe && \
    chown root:group /app/*.txt && \
    chmod 644 /app/*.txt && \
    chmod 600 /app/app.py && \
    chown root:group /app && \
    chmod 750 /app


RUN pip install flask


EXPOSE 5000

CMD ["python", "app.py"]
