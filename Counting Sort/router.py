import os
from plasticObject import plasticObject
from validator import *
from plasticObject import plasticObject
from pathThread import pathThread

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
        one = pathThread(1, current, bigList)
        one.start()
        one.join()
        
        self.masterList.append(one.getWinner())

    def routeCalc(self):
        if self.mode == "Y":
            print("Reading CSV")
        try:
            self.inputList = read_from_csv(
                os.getcwd() + "test_cases/{}".format(self.fileName))

        except:
            print("CSV Error")
            exit()

        # Giving access to routeCalc to modify masterList.
        # Adds inital waste sites as they are to be visited

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

        # Writing to final CSV
        idDesignation = 0
        finalFile = open("finalFile.csv", "w")
        for item in self.masterList:
            finalFile.write("{},{},{},{},{},{}\n".format(idDesignation, item.getLatCord(
            ), item.getLongCord(), item.getObjectType(), item.getPlasticAmount(), item.getRisk()))
            idDesignation = idDesignation + 1
        finalFile.close()

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
