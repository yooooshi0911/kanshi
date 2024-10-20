# ベースイメージとしてPython 3.9を使用
FROM python:3.9

# 作業ディレクトリを/appに設定
WORKDIR /app

# requirements.txtをコンテナにコピー
COPY requirements.txt ./

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# 残りのアプリケーションファイルをコンテナにコピー
COPY . .

# アプリケーションを起動するコマンド
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]