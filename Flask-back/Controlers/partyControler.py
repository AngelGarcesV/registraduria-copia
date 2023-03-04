from models.party import party
dict = [
            {"id":123,
             "name": "centro demoniaco",
             "motto": "supaisabra"
             },
            {"id":12,
             "name": "Derechasumprema",
             "motto": "supaisabra"
             },
            {"id":124,
             "name": "petrosky",
             "motto": "supaisabra"
             },
        ]
class partyControler():
    def __init__(self):
        print("controlador Partido")

    def create(self,infoParty):
        print("crear un candidato")
        partido = party(infoParty)
        dict.append(partido.__dict__)
        print(dict)
        return dict

    def index(self):
        print("Get all the candidates")
        return dict