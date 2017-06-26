# coding: utf-8

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def index():
    # 「templates/index.html」のテンプレートを使う
    # 「message」という変数に"Hello"と代入した状態で、テンプレート内で使う
    return render_template('index.html', message="Hello")

@app.route('/hello')
def hello():
    # request.argsにクエリパラメータが含まれている
    val = request.args.get("msg", "Not defined")
    return 'Hello World '  + val

## methodsにPOSTを指定すると、POSTリクエストを受けられる
#@app.route('/post_request', methods=['POST'])
#def post_request():
#    # request.formにPOSTデータがある
#    username = request.form["username"]
#    return 'Thank you ' + username

# パスにIDが含まれていることを指定すると、メソッドの引数で受け取れる
@app.route('/post/<postid>')
def post(postid):
    return 'Thanks post: id = %s' % postid

## 型も指定できる
#@app.route('/post2/<int:postid>')
#def post2(postid):
#    return 'Thanks post: id = %d' % postid

if __name__ == "__main__":
    app.run()
