#cording: utf-8

from flask import Flask, render_template

# appという名前で Flask オブジェクトをインスタンス化
app = Flask(__name__)

# --- view 側の設定---
# ルートディレクトリにアクセスした場合の挙動
@app.route("/")
def index():
    # DBから以下の変数を読み込んできたと仮定
    title_ = "ようこそ"
    message_ = "MTV デザインパターンで Webアプリ作成"
    
    return render_template("index.html", title=title_, message=message_)

# エントリーポイント
if __name__ == "__main__":
    app.run()
    