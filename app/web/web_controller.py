import time
import datetime
from flask import Flask, jsonify, Blueprint, render_template
from flask import request

blueprint = Blueprint('web_controller',__name__, static_url_path='/web/', static_folder='./static',template_folder = './templates' )

#this will be default method
@blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')
