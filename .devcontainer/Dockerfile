# ベースイメージとしてDebianのstable-slimを使用
FROM debian:stable-slim

# 作業ディレクトリを設定
WORKDIR /workspace

# 必要なパッケージをインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv curl git unzip vim ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Python仮想環境を作成
RUN python3 -m venv /workspace/venv

# 仮想環境を有効にし、pipをアップグレードしてAWS CDKをインストール
RUN /workspace/venv/bin/pip install --upgrade pip && \
    /workspace/venv/bin/pip install aws-cdk-lib

# 非rootユーザーを作成して開発環境で使用
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    chown -R $USERNAME:$USERNAME /workspace

# コンテナ内で使用するユーザーに切り替え
USER $USERNAME

# 必要なポートを開放
EXPOSE 3000 8080

# AWSのCDK CLI用の設定が必要な場合に環境変数を追加
ENV AWS_REGION=us-west-2

# 仮想環境を自動的にアクティベートするための設定
CMD ["/workspace/venv/bin/python3"]

