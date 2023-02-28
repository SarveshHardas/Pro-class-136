from flask import Flask,jsonify,request
from data import data

app = Flask(__name__)

@app.route("/")

def index():
    return jsonify({
        "data":data,
        "message":"success"
    }),200

if __name__ == "_main_":
    app.run()
