from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
import pymongo
import certifi

from waitress import serve
from Controlers.candidateControler import candidateControler
from Controlers.partyControler import partyControler
from Controlers.resultControler import resultControler
from Controlers.tableControler import tableControler


app = Flask(__name__)
cors = CORS(app)
candi = candidateControler()
party = partyControler()
result = resultControler()
table = tableControler()


#print(baseDatos.list_collection_names())

#-----------Candidate Roots-----------#
#Get all the candidates
@app.route("/candidate",methods=['GET'])
def getAll():
    json = candi.index()
    return json
#Get candidate by Id
@app.route("/candidate/<string:id>",methods=['GET'])
def getById(id):
    print(id)
    json = candi.show(id)
    return jsonify(json)
#Create a new candidate
@app.route("/candidate",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = candi.create(data)
    return jsonify(json)
#edit a Candidate
@app.route("/candidate/<string:id>",methods=['PUT'])
def editarCandidato(id):
    print(id)
    data = request.get_json()

    json=candi.update(id,data)
    return jsonify(json)

    return {"status": False}

#Delete a Candidate
@app.route("/candidate/<string:id>",methods=['DELETE'])
def deleteCandidate(id):
    json = candi.delete(id)
    return jsonify(json)

#-----------Party Roots-----------#
@app.route("/party",methods=['GET'])
def getallParty():
    dict = [
        {"message:": True}
    ]
    response = party.index()
    dict.append(response.__dict__)
    return jsonify(dict)


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

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running: "+"http://"+dataConfig["url-backend"]+":"+str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])

