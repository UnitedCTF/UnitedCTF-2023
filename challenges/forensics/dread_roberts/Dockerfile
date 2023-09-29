FROM python:3.11
WORKDIR /code

RUN apt-get update && apt-get install tor -y
RUN python -m pip install --upgrade pip
COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./src .
COPY /src/.env .env
RUN chmod 777 /tmp
EXPOSE 9802
 
CMD [ "python", "app.py" ]

