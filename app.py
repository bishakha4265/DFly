from flask import Flask  # import flask

app = Flask(__name__)  # create an app instance


@app.route("/")  # at the end point /
def wlcm_mesaage():  # call method hello
    return "Welcome to Dragonfly"  # which returns "hello world"


if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app
