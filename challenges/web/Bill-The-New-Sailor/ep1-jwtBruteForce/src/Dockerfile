FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt update && apt install -y sqlite3

COPY . .

RUN sqlite3 users.db < schema.sql

CMD ["python", "app.py"]