from models.table import table
from Repositories.repositorioTable import repositorioTable

class tableControler():
        def __init__(self):
            self.repositorioTable = repositorioTable()

        def index(self):
            print("Get all tables")
            return self.repositorioTable.getAll()

        def save(self,infoTable):
            print("Insert one table")
            try:
                if infoTable['num_inscribed']:
                    theResult = table(infoTable)
                    response = self.repositorioTable.save(theResult)
                    return response
            except:
                return {
                    "message":"Los atributos enviados no corresponden a una mesa",
                    "Code":403
                }
        def show(self,id):
            print("Showing table with id: ",id)
            return self.repositorioTable.getById(id)

        def update(self,id,infoTable):
            print("Updating a table")
            newResult = table(infoTable)
            return self.repositorioTable.update(id,newResult)

        def delete(self,id):
            print("Deleting the table")
            return self.repositorioTable.delete(id)