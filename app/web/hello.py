from flask import Flask, Blueprint,jsonify
import hellohelper

app = Flask(__name__)
app.register_blueprint(hellohelper.app,url_prefix="/abc")

if __name__ == '__main__':
    app.run()
