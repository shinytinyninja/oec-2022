import os
from plasticObject import plasticObject

# STATIC VARIABLES, NOT TO BE CHANGED
listID = 0
listLat = 1
listLong = 2
listType = 3
listValue = 4
listRisk = 5

class quadSplit():
    def __init__(self, fileName):
        self.fileName = fileName
        self.matrix = []
        self.allDest = []
        
        self.wasteDest = []
        self.wastePlacesDict = {}
        
        self.localSortPlaces = []
        self.regSortPlaces = []
        self.regRecPlaces = []
    
    def readCSV(self):
        temp = []
        try:
            
            self.fileName = (os.getcwd() + "/test_cases/") + self.fileName + (".csv")
            print(self.fileName)
            
            with open(self.fileName) as csv_file:
                node = [line.split(",") for line in csv_file]
                for i, info in enumerate(node):
                    temp.append(info)
            self.matrix = temp
            print("CSV Read")
        except:
            print("CSV Error")
            
    def processData(self):
        # Generating list of all destinations
        for item in self.matrix:
            
            # Mapping each line of CSV to a Plastic Object
            mapObject = plasticObject(
                item[listID], item[listType], item[listLat], item[listLong], item[listValue], item[listRisk])

            # Generating list of waste sites
            if mapObject.getObjectType() == "waste":
                self.wastePlacesDict[mapObject.getCode()] = mapObject
                self.wasteDest.append(mapObject)

            # generating list of waste
            elif mapObject.getObjectType() == "local_sorting_facility":
                self.localSortPlaces.append(mapObject)

            # generating list of waste
            elif mapObject.getObjectType() == "regional_sorting_facility":
                self.regSortPlaces.append(mapObject)

            # generating list of waste
            else:  # item[3] == "regional_recycling_facility"
                self.regRecPlaces.append(mapObject)
            
    def getAllDest(self):
        return self.wasteDest + self.regSortPlaces + self.regRecPlaces
    
    def getWasteDest(self):
        return self.wasteDest

    def getWasteDestDict(self):
        return self.wastePlacesDict
    
    def getLocalSortDest(self):
        return self.localSortPlaces
        
    def getRegionalSortDest(self):
        return self.regSortPlaces
        
    def getRegionalRecDest(self):
        return self.regRecPlaces