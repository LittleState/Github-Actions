#!/usr/bin/env bash
# https://stackoverflow.com/a/76533956/15329708

if [ -n "${GITHUB_WORKSPACE}" ]; then

echo ${GITHUB_WORKSPACE}

docker run --rm -i \
  -v $GITHUB_WORKSPACE/../../:/workspace \
  busybox:latest \
  /bin/sh -c "chown -R $(id -u):$(id -g) /workspace"

  rm -rf ${GITHUB_WORKSPACE}/{.??*,*} || true
fi
