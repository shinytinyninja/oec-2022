import collections
import queue
import threading
from turtle import towards
from plasticObject import plasticObject
from validator import *
from plasticObject import plasticObject
from pathThread import pathThread

masterList = []
bestQOR = []

testing = 0

listID = 0
listLat = 1
listLong = 2
listType = 3
listValue = 4
listRisk = 5

# ==============================================================================
# Route Calculation File
# ==============================================================================
class router:

    def __init__(self, fileName, mode):
        self.fileName = fileName
        self.inputList = []
        self.wastePlaces = []
        self.localSortPlaces = []
        self.regSortPlaces = []
        self.regRecPlaces = []
        self.mode = mode
    
    def findBest(self, current, bigList):
        size = len(bigList)
        halfway = size/2
        halfway = int(halfway)
        
        quarter = halfway/2
        quarter = int(quarter)
        
        list1 = bigList[0:quarter]
        list2 = bigList[quarter:halfway]
        list3 = bigList[halfway:halfway+quarter]
        list4 = bigList[halfway+quarter:size]
        
        print("Half = {} and Quarter = {}".format(halfway, quarter))
        
        one = pathThread(1, current, list1)
        two = pathThread(2, current, list2)
        three = pathThread(3, current, list3)
        four = pathThread(4, current, list4)
        
        one.start()
        two.start()
        three.start()
        four.start()
        
        one.join()  
        two.join() 
        three.join()
        four.join()
        
        winners = [one.getWinner(), two.getWinner(), three.getWinner(), four.getWinner()]
        lowest = 0
        
        print("Winners")
        print (winners)
        for win in winners:
            if lowest == 0:
                lowest = win[1]
            elif win[1] < lowest:
                lowest = win[1]  
                lowestDest = win[0]
        
        masterList.append(lowestDest)
        
    def routeCalc(self):
        if self.mode == "Y":
            print("Reading CSV")
        try:
            self.inputList = read_from_csv("test_cases/small/{}".format(self.fileName))
        except:
            print("CSV Error")
            exit()
        
        #Giving access to routeCalc to modify masterList.
        #Adds inital waste sites as they are to be visited
        global masterList
        
        #Generating list of all destinations
        for item in self.inputList:
            #Mapping each line of CSV to a Plastic Object
            mapObject = plasticObject(item[listID], item[listType], item[listLat], item[listLong], item[listValue], item[listRisk])
            
            #Generating list of waste sites
            if mapObject.getObjectType() == "waste":
                self.wastePlaces.append(mapObject)
                masterList.append(mapObject)
                
            #generating list of waste
            elif mapObject.getObjectType() == "local_sorting_facility":
                self.localSortPlaces.append(mapObject)
            
            #generating list of waste
            elif  mapObject.getObjectType() == "regional_sorting_facility":
                self.regSortPlaces.append(mapObject)
            
            #generating list of waste
            else: #item[3] == "regional_recycling_facility"
                self.regRecPlaces.append(mapObject)

        #Collect Waste
        # ======================================================================
        # Waste is already collected as it has been appended to master list
        # ======================================================================
        
        print(masterList[-1].getObjectType())
        
        #Find Local Sorting
        self.findBest(masterList[-1], self.localSortPlaces)
        
        #Find Regional Sorting
        self.findBest(masterList[-1], self.regSortPlaces)
        
        #Find Regional Recycling
        self.findBest(masterList[-1], self.regRecPlaces)
        
        
        # minQor = 100
        # for pair in masterList:
        #     if(pair[0] < minQor):
        #         minQor == pair[0]
        
        #Writing to final CSV
        idDesignation = 0
        finalFile = open("finalFile.csv", "w")
        for item in masterList:
            finalFile.write("{},{},{},{},{},{}\n".format(idDesignation, item.getLatCord(), item.getLongCord(), item.getObjectType(), item.getPlasticAmount(), item.getRisk()))
            idDesignation = idDesignation + 1
        finalFile.close()
        
    def getWaste(self):
        return self.wastePlaces
    
    def getLocalSort(self):
        return self.localSortPlaces
    
    def getRegionalSort(self):
        return self.regSortPlaces
    
    def getRegionalRec(self):
        return self.regRecPlaces