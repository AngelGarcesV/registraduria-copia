from models.party import party
from Repositories.repositorioParty import repositorioParty

class partyControler():
        def __init__(self):
            self.repositorioParty = repositorioParty()

        def index(self):
            print("Get all parties")
            return self.repositorioParty.getAll()

        def save(self,infoParty):
            print("Insert one party")
            try:
                if infoParty['name'] and infoParty['motto']:
                    theParty = party(infoParty)
                    response = self.repositorioParty.save(theParty)
                    return response
            except:
                return {
                    "message":"Los atributos enviados no corresponden a un partido",
                    "Code":403
                }
        def show(self,id):
            print("Showing party with id: ",id)
            return self.repositorioParty.getById(id)

        def update(self,id,infoParty):
            print("Updating a Party")
            newParty = party(infoParty)
            return self.repositorioParty.update(id,newParty)

        def delete(self,id):
            print("Deleting the party")
            return self.repositorioParty.delete(id)