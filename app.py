from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Lab AWS - Anne"

@app.route("/ping")
def ping():
    return "pong"

if __name__ == "__main__":
    app.run()


