from models.Candidate import Candidate
dict = [
            {"id":123,
             "name": "angel",
             "party": "supaisabra"
             },
            {"id":12,
             "name": "angel",
             "party": "supaisabra"
             },
            {"id":124,
             "name": "angel",
             "party": "supaisabra"
             },
        ]
class candidateControler():
    def __init__(self):
        print("creando el controlador xd")

    def index(self):
        print("acá se imprimiran los estudiantes")

        return dict

    def create(self, infoCandidate):
        print("Crear un candidato")
        elCandidato = Candidate(infoCandidate)
        dict.append(elCandidato.__dict__)
        print(dict)
        return dict


    def show(self,id):
        print("mostrando candidato con id:",id)
        for cand in dict:
            print(cand['id'])
            if cand['id'] == int(id):
                print("True")
                return cand
            else:
                pass

    def update(self,_id,infoCandidate):
        cont = 0
        for cand in dict:
            if cand['id'] ==int(_id):
                dict.pop(cont)
                print(infoCandidate)
                candi = Candidate(infoCandidate)
                dict.append(candi.__dict__)
                return dict
            else:
                cont*=1
                pass
        return {"message":False}