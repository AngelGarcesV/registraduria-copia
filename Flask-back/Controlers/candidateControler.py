from Repositories.repositorioCandidate import repositorioCandidate
from models.Candidate import Candidate

class candidateControler():
    def __init__(self):
        self.repositorioCandidate = repositorioCandidate()

    def index(self):
        print("Get all candidates")
        return self.repositorioCandidate.getAll()

    def create(self, infoCandidate):
        try:
            print("Create a candidate")
            if infoCandidate['name'] and infoCandidate['lastName'] and infoCandidate['partyId'] and infoCandidate['partyId']:
                elCandidato = Candidate(infoCandidate)
                print(elCandidato.__dict__)
                response = self.repositorioCandidate.save(elCandidato)
                return response
        except:
            return {"message": "los atributos enviados no corresponden a un candidato"}

    def show(self,id):
        print("mostrando candidato con id:",id)
        return  self.repositorioCandidate.getById(id)


    def update(self,_id,infoCandidate):
        print("Update a candidate")
        if infoCandidate['name'] and infoCandidate['lastName'] and infoCandidate['partyId'] and infoCandidate['partyId']:
            return self.repositorioCandidate.update(_id,Candidate(infoCandidate))

    def delete(self,_id):
        print("Delete a candidate")
        return self.repositorioCandidate.delete(_id)
