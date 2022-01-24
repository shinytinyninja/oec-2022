# ==============================================================================
# PlasticObject
# Used as a general object to hold data regarding any object on our map
# Waste, LocalSort, Regional Sort, Regional Recycling
# ==============================================================================
class plasticObject:
    def __init__(self, objectID, objectType, latCord, longCord, plasticAmount, risk):
        self.objectID = objectID
        self.objectType = objectType
        self.latCord = latCord
        self.longCord = longCord
        self.plasticAmount = plasticAmount
        self.risk = risk
        
    def getID(self):
        return self.objectID
    
    def setID(self, id):
        self.objectID = id
    
    def getObjectType(self):
        return self.objectType

    def setObjectType(self, myObjectType):
        self.objectType = myObjectType

    def getLatCord(self):
        return self.latCord

    def setLatCord(self, myLatCord):
        self.latCord = myLatCord

    def getLongCord(self):
        return self.longCord

    def setLongCord(self, myLongCord):
        self.longCord = myLongCord

    def getPlasticAmount(self):
        return self.plasticAmount

    def setPlasticAmount(self, myPlasticAmount):
        self.plasticAmount = myPlasticAmount

    def getRisk(self):
        return self.risk

    def setRisk(self, myRisk):
        self.risk = myRisk