from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/calculate')
def calculate():
    return render_template("calculate.html")


@app.route("/history")
def history():
    return render_template("history.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5555, debug=True)