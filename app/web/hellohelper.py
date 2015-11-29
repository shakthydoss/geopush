from flask import Flask,Blueprint, jsonify

app = Blueprint('hellohelper',__name__)

@app.route('/index')
def hello_world():
    return jsonify({'message':'hello world-abc'})

