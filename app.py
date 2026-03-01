from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def register():
    return "register"


@app.route("/login")
def login():
    return "login"


@app.route('/calculate')
def calculate():
    return "calculate"


@app.route("/history")
def history():
    return "history"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5555, debug=True)