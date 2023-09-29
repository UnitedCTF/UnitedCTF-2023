FROM php:8

RUN apt update && apt install -y git

WORKDIR /app
COPY src/* /app/

RUN git init

RUN git add -A
RUN git config user.email "robert@example.com"
RUN git config user.name "robert"
RUN git commit -a -m "What a nice boat! I hope nobody steals our flag :)"

RUN sed 's/~flag-[0-9a-f]*/<!-- stole the flag -->/' -i index.php
RUN git add -A
RUN git config user.email "evilbob@example.com"
RUN git config user.name "evilbob"
RUN git commit -a -m "Stole the flag, muhahah >:)"

EXPOSE 8000
STOPSIGNAL SIGKILL
ENTRYPOINT [ "php", "-S", "0.0.0.0:8000" ]
