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
def getAllCandidate():
    json = candi.index()
    return json

#Get candidate by Id
@app.route("/candidate/<string:id>",methods=['GET'])
def getCandidateById(id):
    json = candi.show(id)
    return jsonify(json)

#Create a new candidate
@app.route("/candidate",methods=['POST'])
def createCandidate():
    data = request.get_json()
    json = candi.create(data)
    return jsonify(json)

#edit a Candidate
@app.route("/candidate/<string:id>",methods=['PUT'])
def updateCandidate(id):
    print(id)
    data = request.get_json()
    json=candi.update(id,data)
    return jsonify(json)

#Delete a Candidate
@app.route("/candidate/<string:id>",methods=['DELETE'])
def deleteCandidate(id):
    json = candi.delete(id)
    return jsonify(json)



#-----------Party Roots-----------#


# Get all the parties
@app.route("/party",methods=['GET'])
def getAllParty():
    response = party.index()
    return jsonify(response)

# Get party by id
@app.route("/party/<string:id>",methods =['GET'])
def getPartyById(id):
    response = party.show(id)
    return jsonify(response)

# Create a party
@app.route("/party",methods=['POST'])
def createParty():
    infoParty = request.get_json()
    response = party.save(infoParty)
    return jsonify(response)

# Update a party
@app.route("/party/<string:id>",methods=['PUT'])
def updateParty(id):
    newParty = request.get_json()
    response = party.update(id,newParty)
    return jsonify(response)

# Delete a party
@app.route("/party/<string:id>",methods=['DELETE'])
def deleteParty(id):
    response = party.delete(id)
    return jsonify(response)

#-----------Table Roots-----------#


#get all tables
@app.route("/table",methods=['GET'])
def getAllTable():
    response = table.index()
    return jsonify(response)

#get table by id
@app.route("/table/<string:id>",methods=['GET'])
def getTableById(id):
    response = table.show(id)
    return jsonify(response)

#insert a table
@app.route("/table",methods=['POST'])
def createTable():
    infoTable = request.get_json()
    response = table.save(infoTable)
    return jsonify(response)

#update a table
@app.route("/table/<string:id>",methods=['PUT'])
def updateTable(id):
    newTable = request.get_json()
    response = table.update(id,newTable)
    return jsonify(response)

#delete a table
@app.route("/table/<string:id>",methods=['DELETE'])
def deleteTable(id):
    response = table.delete(id)
    return jsonify(response)

#-----------Result Routes-----------#


#get all results
@app.route("/result",methods=['GET'])
def getAllResult():
    response = result.index()
    return jsonify(response)

#get result by id
@app.route("/result/<string:id>",methods=['GET'])
def getResultById(id):
    response = result.show(id)
    return jsonify(response)

#insert a result
@app.route("/result",methods=['POST'])
def createResult():
    infoResult = request.get_json()
    response = result.save(infoResult)
    return jsonify(response)

#update a result
@app.route("/result/<string:id>",methods=['PUT'])
def updateResult(id):
    newResult = request.get_json()
    response = result.update(id,newResult)
    return jsonify(response)

#delete a result
@app.route("/result/<string:id>",methods=['DELETE'])
def deleteResult(id):
    response = result.delete(id)
    return jsonify(response)


#-----------CONFIG AND MAIN ROOT-----------#


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

