#cording: utf-8

from flask import Flask, render_template

# appという名前で Flask オブジェクトをインスタンス化
app = Flask(__name__)

# --- view 側の設定---
# ルートディレクトリにアクセスした場合の挙動
@app.route("/")
def index():
    # return "Hello World"
    return render_template("index.html")

# エントリーポイント
if __name__ == "__main__":
    app.run()


