FROM node:22-alpine

ENV LANG=zh
ENV HOST=0.0.0.0

RUN npm install -g bunyan gulp@4 \
    && apk add --no-cache git \
    && mkdir /js && cd /js \
    && git clone https://github.com/javascript-tutorial/server \
    && git clone https://github.com/javascript-tutorial/engine server/modules/engine \
    && git clone https://github.com/javascript-tutorial/$LANG.javascript.info server/repo/$LANG.javascript.info \
    && cd server && npm install

WORKDIR /js/server
EXPOSE 3000
CMD ["sh", "-c", "sh /js/server/edit $LANG"]
