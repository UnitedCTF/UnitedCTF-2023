FROM node:18

WORKDIR /app
COPY /src/ .

ENV ENVIRONMENT=production
ENV DEBUG=express:router

RUN npm i

USER node
STOPSIGNAL SIGKILL
ENTRYPOINT [ "node", "index.js" ]
