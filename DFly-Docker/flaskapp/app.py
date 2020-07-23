from flask import Flask, render_template # import flask

app = Flask(__name__)  # create an app instance


@app.route("/")
def index():
    return render_template("home.html")


