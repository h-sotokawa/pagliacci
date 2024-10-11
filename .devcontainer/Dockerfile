FROM debian:stable-slim

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    python3 \
    python3-pip \
    npm \
    vim \
#     locales \
#     console-setup \
#     keyboard-configuration \
    && rm -rf /var/lib/apt/lists/*

# # ロケールを設定
# RUN sed -i 's/# ja_JP.UTF-8 UTF-8/ja_JP.UTF-8 UTF-8/' /etc/locale.gen
# RUN locale-gen

# # デフォルトロケールを設定
# RUN update-locale LANG=ja_JP.UTF-8

# RUN echo 'keyboard-configuration  keyboard-configuration/layout  select  Japanese' | debconf-set-selections
# RUN dpkg-reconfigure -f noninteractive keyboard-configuration


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