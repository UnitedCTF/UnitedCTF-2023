FROM python:3.8.5-alpine

WORKDIR /app

COPY src/ .

RUN addgroup -S group && \
    adduser -S -G group johndoe && \
    chmod 600 /app/app.py && \
    chown root:group /app && \
    chmod 750 /app

RUN pip install flask timeout_decorator

EXPOSE 5000

CMD ["python", "app.py"]