# 1. 使用官方 PyTorch GPU base image
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# 2. 基本環境設定
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y git python3-pip && \
    pip install --upgrade pip

# 3. 安裝 mmsegmentation 相關依賴
RUN pip install openmim
RUN mim install mmcv-full
RUN mim install mmengine
RUN mim install "mmsegmentation>=1.0.0"

# 4. 工作目錄與專案檔案
WORKDIR /workspace

COPY mmsegmentation/ ./mmsegmentation/
COPY tongue/ ./tongue/
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt || true

WORKDIR /workspace/mmsegmentation

CMD ["/bin/bash"]
