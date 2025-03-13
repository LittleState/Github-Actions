FROM node:18-alpine

RUN apk add --no-cache git imagemagick

WORKDIR /js
RUN npm install -g bunyan gulp@4

RUN git clone https://github.com/javascript-tutorial/server && \
    git clone https://github.com/javascript-tutorial/engine server/modules/engine && \
    cd /js/server/repo && git clone https://github.com/javascript-tutorial/zh.javascript.info

WORKDIR /js/server
RUN npm install
