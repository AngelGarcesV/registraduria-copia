from models.result import result
from Repositories.repositorioResult import repositorioResult

class resultControler():
        def __init__(self):
            self.repositorioResult = repositorioResult()

        def index(self):
            print("Get all results")
            return self.repositorioResult.getAll()

        def save(self,infoResult):
            print("Insert one result")
            try:
                if infoResult['candidateId'] and infoResult['tableId'] and infoResult['vote']:
                    theResult = result(infoResult)
                    response = self.repositorioResult.save(theResult)
                    return response
            except:
                return {
                    "message":"Los atributos enviados no corresponden a un resultado",
                    "Code":403
                }
        def show(self,id):
            print("Showing result with id: ",id)
            return self.repositorioResult.getById(id)

        def update(self,id,infoResult):
            print("Updating a result")
            newResult = result(infoResult)
            return self.repositorioResult.update(id,newResult)

        def delete(self,id):
            print("Deleting the result")
            return self.repositorioResult.delete(id)