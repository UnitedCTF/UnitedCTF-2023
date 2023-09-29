FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN groupadd -r flask_user && useradd -r -g flask_user flask_user

COPY . .

RUN chown -R flask_user:flask_user /app
RUN chmod 400 /app/flag.txt
RUN chmod 500 /app

USER flask_user

CMD ["python", "app.py"]