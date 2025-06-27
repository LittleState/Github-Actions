# 使用官方 Python 基础镜像（可根据需要调整版本）
FROM python:3.10-slim

# 设置工作目录
WORKDIR /workspace

# 安装系统依赖 + 清理缓存减小镜像体积
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    file \
    binutils \
    git \
    && rm -rf /var/lib/apt/lists/*

# 安装 Python 反编译工具
RUN pip install --no-cache-dir uncompyle6 pyinstaller

# 克隆 pyinstxtractor 工具
RUN git clone https://github.com/extremecoders-re/pyinstxtractor.git

# 创建便捷脚本
RUN echo '#!/bin/bash\n' \
    'python /workspace/pyinstxtractor/pyinstxtractor.py "$1" && \' \
    'echo -e "\n\033[32m[SUCCESS] 文件解包到: $(basename "$1")_extracted/\033[0m"' > /usr/bin/extract-py \
    && chmod +x /usr/bin/extract-py

RUN echo '#!/bin/bash\n' \
    'if [ -f "$1" ]; then' \
    '  uncompyle6 "$1" > "${1%.*}.py";' \
    '  echo -e "\n\033[32m[SUCCESS] 反编译完成: ${1%.*}.py\033[0m";' \
    'else' \
    '  echo -e "\033[31m[ERROR] 文件不存在: $1\033[0m";' \
    'fi' > /usr/bin/decompile \
    && chmod +x /usr/bin/decompile

# 设置容器启动命令（保持运行）
CMD ["tail", "-f", "/dev/null"]