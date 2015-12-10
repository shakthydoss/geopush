import time
import datetime
from flask import Flask, jsonify, Blueprint
from flask import request

blueprint = Blueprint('rest_controller',__name__)

#this will be default method
@blueprint.route('/', methods=['GET'])
def index():
    return jsonify({'Welcome': 'GeoPush'})

#method to update location of devices.
@blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status':200,'method':'ping'})

#method to push the message to near devices.
@blueprint.route('/push', methods=['GET'])
def push():
    return jsonify({'status':'200', 'method':'push'})

