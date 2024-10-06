FROM debian:stable-slim

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    python3 \
    python3-pip \
    npm \
    vim \
    && rm -rf /var/lib/apt/lists/*

# 最新のAWS CLIをインストール
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip aws

# 最新のAWS CDK（Python版）をインストール
RUN pip3 install --upgrade aws-cdk-lib --break-system-packages

RUN npm install -g aws-cdk

# デフォルトのユーザーをrootに設定
USER root