from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controlers.candidateControler import candidateControler

app = Flask(__name__)
cors = CORS(app)
candi = candidateControler()

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

@app.route("/",methods=['GET'])
def test():
    json = {
        "messaje": "server is running",
        "port":5000
    }
    return jsonify(json)

@app.route("/candidate",methods=['GET'])
def hola():
    json = candi.index()
    return json

@app.route("/candidate/<string:id>",methods=['GET'])
def getById(id):
    print(id)
    json = candi.show(id)
    return jsonify(json)

@app.route("/candidate",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=candi.create(data)
    return jsonify(json)

@app.route("/candidate/<string:id>",methods=['PUT'])
def editarCandidato(id):
    data = request.get_json()
    print(type(id))
    print(data)
    json=candi.update(id,data)
    return jsonify(json)

    return {"status": False}

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running: "+"http://"+dataConfig["url-backend"]+":"+str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])

