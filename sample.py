# 必要なモジュールをインポート
from flask import Flask

# Flask をインスタンス化
app = Flask(__name__)

# ルートディレクトリにアクセスがあっった時の処理
@app.route("/")
def hello():
    return "Hello World"

# エントリーポイント
if __name__ == "__main__":
    app.run()
    
