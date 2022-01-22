from webbrowser import get


class plasticObject:
    def __init__(self, objectID, objectType, cord, plasticAmount, risk):
        self.id = objectID
        self.type = objectType
        self.cord = cord
        self.plasticAmount = plasticAmount
        self.risk = risk
        
    def getID(self):
        return self.id
    
    def setID(self, id):
        self.id = id
    
    def getType(self, type)
    
    def set