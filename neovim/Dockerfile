# 使用适用于 ARM64 的基础镜像
FROM ubuntu:22.04

# 设置环境变量
ENV DEBIAN_FRONTEND=noninteractive

# 安装必要的依赖
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    ninja-build \
    gettext \
    libtool \
    libtool-bin \
    autoconf \
    automake \
    cmake \
    g++ \
    pkg-config \
    unzip \
    curl \
    git \
    python3 \
    python3-pip && \
    apt-get clean

# 克隆 Neovim 源码
RUN git clone https://github.com/neovim/neovim.git /neovim

# 设置工作目录
WORKDIR /neovim

# 检出最新的稳定版本（可根据需要更改分支）
RUN git checkout stable

# 构建 Neovim
RUN make CMAKE_BUILD_TYPE=RelWithDebInfo

RUN cd build && cpack -G DEB && dpkg -i nvim-linux64.deb

# 设置默认启动命令
CMD ["cp", "*.deb", "/output"]

# steps:
# 1. docker build -t neovim-deb-builder .
# 2. docker run --rm -it -v ./output:/output neovim-deb-builder