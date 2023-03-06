from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import datetime
import requests
import re

app = Flask(__name__)
cors = CORS(app)
from flask_jwt_extended import create_access_token, verify_jwt_in_request, get_jwt, unset_jwt_cookies, \
    set_access_cookies
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app.config["JWT_SECRET_KEY"] = "super-secret"  # Cambiar por el que se conveniente
jwt = JWTManager(app)


@app.route("/login", methods=["POST"])
def create_token():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/usuarios/validar'
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print(type(response))
        user = response.json()
        print(type(user))
        expires = datetime.timedelta(seconds=60 * 60 * 24)
        access_token = create_access_token(identity=user, expires_delta=expires)


        urlpermiso = dataConfig["url-backend-security"] + '/permisos-roles/permisos/' + user['rol']['_id']
        response = requests.get(urlpermiso, headers=headers)

        json = response.json()

        print(json)
        return jsonify({"token": access_token, "user_id": user["_id"],"permisos":json})
    else:
        return jsonify({"msg": "Bad username or password"}), 401


@app.before_request
def before_request_callback():
    endPoint = limpiarURL(request.path)
    print(endPoint)
    excludedRoutes = ["/login",]
    if excludedRoutes.__contains__(request.path):
        pass
    elif verify_jwt_in_request():
        usuario = get_jwt_identity()
        print(usuario)
        if usuario["rol"] is not None:
            tienePersmiso = validarPermiso(endPoint, request.method, usuario["rol"]["_id"])
            print(tienePersmiso)
            if not tienePersmiso:
                return jsonify({"message": "Permission denied"}), 401
        else:
            return jsonify({"message": "Permission denied"}), 401


def limpiarURL(url):
    print("valida url")
    partes = url.split("/")
    for laParte in partes:
        if re.search('\\d', laParte):
            url = url.replace(laParte, "?")
    return url


def validarPermiso(endPoint, metodo, idRol):
    print(metodo)
    url = dataConfig["url-backend-security"] + "/permisos-roles/validar-permiso/rol/" + str(idRol)
    tienePermiso = False
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url": endPoint,
        "metodo": metodo
    }
    response = requests.get(url, json=body, headers=headers)

    try:
        data = response.json()
        if "_id" in data:
            tienePermiso = True
        else:
            tienePermiso = False
    except:
        pass
    return tienePermiso

@app.route("/logout", methods=["POST"])
@jwt_required(verify_type=False)
def logout():

    res=jsonify(msg="token successfully revoked")
    unset_jwt_cookies(res)

    # Returns "Access token revoked" or "Refresh token revoked"
    return res


@app.route("/usuarios", methods=['GET'])
def getUsers():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/usuarios'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/usuarios", methods=['POST'])
def crearUsuario():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    petRes = []
    try:
        infoMesa = data['mesa']

        if infoMesa != None:
            print(infoMesa)
            urlT = dataConfig["url-backend-result"] + '/gettableid'
            dict = {"mesa": infoMesa}
            response = requests.get(urlT, headers=headers, json=dict)
            json = response.json()
            rta = json.pop(0)
            status = rta['status']
        if status is True:
            urlUser = dataConfig["url-backend-security"] + '/usuarios'
            responseNewUser = requests.post(urlUser, headers=headers, json=data)
            rta2 = responseNewUser.json()
            petRes.append(rta2)
            try:
                iduser = rta2['_id']
                print(iduser)
                urlroluser = dataConfig["url-backend-security"] + '/usuarios/' + iduser + '/rol/63267b7d15e8cc6bf8e55b9d'
                responseroluser = requests.put(urlroluser, headers=headers)
                rta3 = responseroluser.json()
                petRes.append(rta3)
            except KeyError:
                message = "El usuario no pudo ser creado"
                petRes.append(message)
        else:
            petRes.append(json)
    except KeyError:
        urlUser = dataConfig["url-backend-security"] + '/usuarios'
        responseNewUser = requests.post(urlUser, headers=headers, json=data)
        rta2 = responseNewUser.json()
        petRes.append(rta2)

    return jsonify(petRes)


@app.route("/usuarios/<string:id>", methods=['GET'])
def getUser(id):
    print(id)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/usuarios/' + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/usuarios/<string:id>", methods=['PUT'])
def updateUser(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/usuarios/' + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/usuarios/<string:id>", methods=['DELETE'])
def deleteUser(id):
    print('borrando' + id)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/usuarios/' + id
    response = requests.delete(url, headers=headers)
    print(type(response))
    print(response)
    json = response.json()
    return jsonify(json)


####ROLES


@app.route("/roles", methods=['GET'])
def getRoles():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/usuarios'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/roles", methods=['POST'])
def crearRol():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/roles'
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/roles/<string:id>", methods=['GET'])
def getRol(id):
    print(id)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/roles/' + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/roles/<string:id>", methods=['PUT'])
def updateRol(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/roles/' + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/roles/<string:id>", methods=['DELETE'])
def deleteRol(id):
    print('borrando' + id)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/roles/' + id
    response = requests.delete(url, headers=headers)
    print(type(response))
    print(response)
    json = response.json()
    return jsonify(json)


####ROLES-PERMISOS


@app.route("/permisos-roles", methods=['GET'])
def getRolesPermisos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/permisos-roles'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/permisos-roles/rol/<string:id_rol>/permiso/<string:id_permiso>", methods=['POST'])
def crearRolPermisos(id_rol, id_permiso):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/permisos-roles/rol/' + id_rol + '/permiso/' + id_permiso
    print(url)
    response = requests.post(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/permisos-roles/rol/<string:id>", methods=['POST'])
def crearRolMultoPermiso(id):
    data = request.get_json()
    print(data)
    headers = {"Content-Type": "application/json; charset=utf-8"}

    result = []
    for permiso in data:
        url = dataConfig["url-backend-security"] + '/permisos-roles/rol/' + id + '/permiso/' + permiso['permiso']
        print(url)
        response = requests.post(url, headers=headers, json=data)
        result.append(response.json())

    print(result)

    json = result
    return jsonify(json)


@app.route("/permisos-roles/newrol-multiper", methods=['POST'])
def postNewRol_MultiPer():
    result = []
    data = request.get_json()
    datarol = data.pop(0)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/roles'
    response = requests.post(url,headers=headers,json=datarol)
    rolinfo = response.json()
    idrol = rolinfo['_id']
    result.append(rolinfo)
    for permiso in data:
        url = dataConfig["url-backend-security"] + '/permisos-roles/rol/' + idrol+ '/permiso/' + permiso['permiso']
        response = requests.post(url, headers=headers, json=data)
        result.append(response.json())

    json = result
    return jsonify(json)


@app.route("/permisos-roles/<string:id>", methods=['GET'])
def getRolPermisos(id):
    print(id)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/permisos-roles/' + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/permisos-roles/<string:id>", methods=['PUT'])
def updateRolPermisos(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/permisos-roles/' + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/permisos-roles/<string:id>", methods=['DELETE'])
def deleteRolPermisos(id):
    print('borrando' + id)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/permisos-roles/' + id
    response = requests.delete(url, headers=headers)
    print(type(response))
    print(response)
    json = response.json()
    return jsonify(json)


@app.route("/createparty", methods=['POST'])
def creaateParty():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/createparty'
    response = requests.post(url, headers=headers,json=data)
    print(data)
    json = response.json()
    return jsonify(json)

@app.route("/getallparty", methods=['GET'])
def getAllParty():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + "/party"
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

## crud de resultados
@app.route("/getResult", methods=['GET'])
def getResult():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/result'

    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/updateparty", methods=['PUT'])
def updateParty():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + "/updateparty"
    response = requests.put(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)
@app.route("/deleteparty", methods=['DELETE'])
def deleteParty():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + "/deleteparty"
    response = requests.delete(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

@app.route("/getResultByTable",methods=["GET"])
def getResultByTable():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/getResultbyTable'
    response=requests.get(url, headers=headers)
    json=response.json()
    return jsonify(json)

@app.route("/getResultByParty",methods=["GET"])
def getResultByParty():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/getResultbyParty'
    response=requests.get(url, headers=headers)
    json=response.json()
    return jsonify(json)

@app.route("/getResultByCandidate",methods=["GET"])
def getResultByCandidate():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/getresultbycandidate'
    response=requests.get(url, headers=headers)
    json=response.json()
    return jsonify(json)

@app.route("/getNewCongress",methods=["GET"])
def getNewCongress():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/getNewCongress'
    response=requests.get(url, headers=headers)
    json=response.json()
    return jsonify(json)


@app.route("/updateResult", methods=["PUT"])
def updateResult():
    data=request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/updateresult'
    response=requests.put(url, headers=headers,json=data)
    json=response.json()
    return jsonify(json)

@app.route("/deleteResult", methods=["DELETE"])
def deleteResult():
    data=request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/deleteresult'
    response=requests.delete(url, headers=headers,json=data)
    json=response.json()
    return jsonify(json)

@app.route("/getResult-party-ByTable/<mesa>", methods=["GET"])
def getResultPartyByTable(mesa):
    print(mesa)
    data={"table_Id": mesa}
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"]+'/getResult-party-ByTable'
    response = requests.get(url,headers=headers,json = data)
    json = response.json()
    return jsonify(json)

@app.route("/createResult", methods=['POST'])
def createResult():
    data=request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/createresult'
    print(data)
    response=requests.post(url, headers=headers, json=data)
    json=response.json()
    return jsonify(json)

## crud de candidatos

@app.route("/createcandidate", methods=["POST"])
def createCandidate():
    data=request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/createcandidate'
    response=requests.post(url,headers=headers,json=data)
    json=response.json()
    return jsonify(json)

@app.route("/updatecandidate",methods=["PUT"])
def updatecandidate():
    data=request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/updatecandidate'
    response=requests.put(url,headers=headers,json=data)
    json=response.json()
    return jsonify(json)

@app.route("/getallcandidate", methods=["GET"])
def getallcandidate():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/Candidate'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/deletecandidate", methods=["DELETE"])
def deletecandidate():
    data=request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/deletecandidate'
    response = requests.delete(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)



@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


###mesas


@app.route("/updatetable", methods=['PUT'])
def updateMesa():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + "/updatetable"
    response = requests.put(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)
@app.route("/deletetable", methods=['DELETE'])
def deleteMesa():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + "/deletetable"
    response = requests.delete(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)
@app.route("/createtable", methods=['POST'])
def creaateMesa():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + '/createtable'
    response = requests.post(url, headers=headers,json=data)
    print(data)
    json = response.json()
    return jsonify(json)

@app.route("/getalltable", methods=['GET'])
def getAllMesa():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-result"] + "/table"
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
