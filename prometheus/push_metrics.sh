#!/bin/bash

NODE_EXPORTER_URL="http://localhost:9100/metrics"
JOB_NAME="node_exporter"
INSTANCE_NAME="oracle-amd-1c1g"
PUSHGATEWAY_URL="https://xxx/metrics/job/${JOB_NAME}/instance/${INSTANCE_NAME}"
USERNAME='xxx'
PASSWORD='xxx'

while true; do
  # 获取 node_exporter 的指标数据
  metrics=$(curl -s $NODE_EXPORTER_URL)

  # 推送数据到 Pushgateway，并获取 HTTP 响应代码
  response=$(echo "$metrics" | curl --write-out "%{http_code}" -u ${USERNAME}:${PASSWORD} --silent --output /dev/null --data-binary @- $PUSHGATEWAY_URL)

  # 打印 HTTP 响应代码
  echo "Push response code: $response"

  sleep 5
done
