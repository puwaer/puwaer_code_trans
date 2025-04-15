# ベースイメージとしてUbuntu 22.04を使用
FROM nvidia/cuda:12.4.1-devel-ubuntu22.04

# 必要なツールとライブラリをインストール
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3.11-dev \
    build-essential \
    gcc \
    python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Pythonバージョンの確認（オプション）
RUN python3 --version

# 作業ディレクトリを設定
WORKDIR /app

# スクリプトファイルをコピー
COPY ./ /app/

# 環境変数設定（CUDA関連）
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
ENV PATH=/usr/local/cuda/bin:$PATH

# 実行コマンド
#CMD ["python3", "your_script.py"]
CMD ["/bin/bash"]
