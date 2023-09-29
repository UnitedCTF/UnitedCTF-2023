FROM python:3.9-slim
RUN pip install flask python-dotenv timeout_decorator
COPY app /app
WORKDIR /app
RUN groupadd -r group
RUN useradd -r -m -g group username
RUN chown root:group /app/flag.txt
RUN chmod 644 /app/flag.txt
RUN chown root:group /app
RUN chmod 750 /app
USER username
EXPOSE 8080
ENTRYPOINT ["flask", "run"]