import os
import json
import redis
from flask import Flask,request,jsonify

app = Flask(__name__)
db = redis.StrictRedis(
        host='10.100.2.131',
        port=6379,
        password='ICLmps27364'
        ,decode_responses=True)


@app.route('/',methods=['GET'])
def show():
    name=db.keys()
    name.sort()
    req = []
    for z in name :
        req.append(db.hgetall(z))
    return jsonify(req)
    #return 'Hello %s!' % name



# Get Single Key
@app.route('/<Key>',methods=['GET'])
def get_key(Key):
    result = db.hgetall(Key)
    return jsonify(result)

# DELETE Key
@app.route('/Refrig/<Key>',methods=['DELETE'])
def DELETE_key(Key):
    result = db.delete(Key)
    return jsonify(result)

 # Post Key
@app.route('/Refrig/',methods=['POST'])
def Post_key():
    brand = request.json['brand']
    color = request.json['color']
    size = request.json['size']
    windows = request.json['windows']
    data = {"brand":brand, "color":color, "size":size , "windows":windows}

    db.hmset(windows,data)
    
    return jsonify(data)

# update Key
@app.route('/Refrig/<Key>',methods=['PUT'])
def PUT_key(Key):

    brand = request.json['brand']
    color = request.json['color']
    size = request.json['size']
    windows = request.json['windows']
    data = {"brand":brand,  "color":color, "size":size, "windows":windows}

    db.hmset(Key,data)
    return jsonify(data)




#@app.route('/setname/<name>')
#def setname(name):
#    db.set('name',name)
#   return 'Name updated.'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)