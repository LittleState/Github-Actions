FROM node:18

ENV HOST=0.0.0.0
USER root

RUN npm_config_user=root npm install -g bunyan gulp@4 \
    && mkdir /js && cd /js \
    && git clone https://github.com/javascript-tutorial/server --depth=1 \
    && git clone https://github.com/javascript-tutorial/engine server/modules/engine --depth=1 \
    && git clone https://github.com/javascript-tutorial/zh.javascript.info server/repo/zh.javascript.info --depth=1 \
    && cd server && npm install

WORKDIR /js/server
EXPOSE 3000
CMD ["./edit", "zh", "zh"]
