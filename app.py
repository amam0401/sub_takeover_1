from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Poc by subx0x and Elmou"
