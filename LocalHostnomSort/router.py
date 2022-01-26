import os
from pathlib import Path
from time import sleep
from plasticObject import plasticObject
from validator import read_from_csv
from plasticObject import plasticObject
import math
# STATIC VARIABLES, NOT TO BE CHANGED
listID = 0
listLat = 1
listLong = 2
listType = 3
listValue = 4
listRisk = 5

# ==============================================================================
# Route Calculation Function
# This will, using multi-threading computer the path of lowest QOR Score
# ==============================================================================

class router:
    # Constructor of class.
    # Establishing the destinations of sorting and variables to be used later on
    # mode is for debugging
    def __init__(self, fileName, mode):
        self.fileName = fileName
        self.inputList = []
        self.wastePlaces = []
        self.wastePlacesDict = {}
        self.fullWastePlaces = []
        self.localSortPlaces = []
        self.regSortPlaces = []
        self.regRecPlaces = []
        self.mode = mode
        self.masterList = []

    # Function for finding the best next destination
    # Using the "current" position of our boat, find the next best distination with lowest QOR score
    def findBest(self, current, bigList):
        bestQOR = ()
        x1_lat, y1_lon = int(current.getLatCord()), int(current.getLongCord())
        
        for dest in bigList:  
            x2_lat, y2_lon = int(dest.getLatCord()), int(dest.getLongCord())
            distance = ((((x2_lat-x1_lat)**2) + ((y2_lon-y1_lon)**2)) **0.5 )
  
            riskLevel = float(dest.getRisk()) if float(dest.getRisk()) > 0 else 1
            QOR = float(distance) * riskLevel
            
            if len(bestQOR) == 0:
                bestQOR = (dest, QOR)
            elif (QOR < bestQOR[1]):
                bestQOR = (dest, QOR)
        
        self.masterList.append(bestQOR[0])

    def routeCalc(self):
        p = Path(os.getcwd())
        os.chdir(p.parent)
            
        try:
            print("FILENAME: {}".format(self.fileName))
            file = str(p) + "/test_cases/{}.csv".format(self.fileName)
                
            res = []
            with open(file) as csv_file:
                node = [line.split(",") for line in csv_file]
                for i, info in enumerate(node):
                    res.append(info) 
            self.inputList = res   
        except:
            print("CSV Error")
            exit()

        # Generating list of all destinations
        for item in self.inputList:
            # Mapping each line of CSV to a Plastic Object
            mapObject = plasticObject(
                item[listID], item[listType], item[listLat], item[listLong], item[listValue], item[listRisk])

            # Generating list of waste sites
            if mapObject.getObjectType() == "waste":
                self.wastePlaces.append(mapObject)
                self.wastePlacesDict[mapObject.getCode()] = mapObject
                self.fullWastePlaces.append(mapObject)

            # generating list of waste
            elif mapObject.getObjectType() == "local_sorting_facility":
                self.localSortPlaces.append(mapObject)

            # generating list of waste
            elif mapObject.getObjectType() == "regional_sorting_facility":
                self.regSortPlaces.append(mapObject)

            # generating list of waste
            else:  # item[3] == "regional_recycling_facility"
                self.regRecPlaces.append(mapObject)

        # Collect Waste
        # ======================================================================
        # Waste is already collected as it has been appended to master list
        # ======================================================================

        # Removes the First Waste and Adds it to Master List
        key = list(self.wastePlacesDict.keys())[0]
        self.masterList.append(self.wastePlacesDict.pop(key))

        for i in range(0, len(self.wastePlacesDict) - 1):
            # Find Waste Location
            self.findBest(self.masterList[-1],
                          list(self.wastePlacesDict.values()))
            # print(self.wastePlacesDict.keys())
            self.wastePlacesDict.pop(self.masterList[-1].getCode())

        key = list(self.wastePlacesDict.keys())[0]
        self.masterList.append(self.wastePlacesDict.pop(key))

        # Find Local Sorting
        self.findBest(self.masterList[-1], self.localSortPlaces)

        # Find Regional Sorting
        self.findBest(self.masterList[-1], self.regSortPlaces)

        # Find Regional Recycling
        self.findBest(self.masterList[-1], self.regRecPlaces)

    def getWaste(self):
        return self.fullWastePlaces

    def getLocalSort(self):
        return self.localSortPlaces

    def getRegionalSort(self):
        return self.regSortPlaces

    def getRegionalRec(self):
        return self.regRecPlaces

    def getMaster(self):
        return self.masterList
