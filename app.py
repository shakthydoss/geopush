import time
import datetime
from flask import Flask, jsonify
from elasticsearch import Elasticsearch
import es_helper
from flask import request

app = Flask(__name__)

es = Elasticsearch([
    'localhost:9200'
])

@app.route('/', methods=['GET'])
def index():
    return jsonify({'Welcome': 'GeoPush'})


#method update location of devices. 
@app.route('/ping', methods=['POST'])
def ping():
    data = request.json
    data['@timestamp']=getcts()
    #find city by lan and lon
    location = 'chennai'
    es_helper.write_to_es(es,'ping',location,data, data['device_mac'])
    return jsonify({'status':200})


@app.route('/push', methods=['POST'])
def push():
    data = request.json
    data['@timestamp']=getcts()
    print data
    #find city by lan and lon 
    location = 'chennai'
    es_helper.write_to_es(es,'data',location,data)
    res = es_helper.search_by_lat_lon(es,data['location']['lat'],data['location']['lon'],"1km")
    return jsonify({'status':'200', 'data':res})


def getcts():
    return int(round(time.time() * 1000))

if __name__ == '__main__':
    app.run(debug=True)
