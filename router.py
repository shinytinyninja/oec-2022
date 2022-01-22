import collections
import queue
import threading
from plasticObject import plasticObject
from validator import *
from plasticObject import plasticObject
 
masterList = []
bestQOR = []

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
  
    def __init__(self, fileName):
        self.fileName = fileName
        self.inputList = []
        self.wastePlaces = []
        self.localSortPlaces = []
        self.regSortPlaces = []
        self.regRecPlaces = []
    
    def getBestQOR( threadID, currentLocation, listofDestinations):
        print(threadID)  
        global masterList
        global bestQOR
        
        # Non Path Avoidence
        mapHeight = 400
        mapWidth = 400
        ##########################
        start = (currentLocation.get(),currentLocation.get)
        
        for dest in listofDestinations:  
            stop = (dest.get(), dest.get())
            
            que = collections.deque()
            visited = set([start])
            
            while queue:
                path = queue.popleft()
                x, y = path[-1]
                if (x,y) == stop:
                    print("Found a Path")
                    ## QOR calculator
                    QOR = len(path) * dest.getRisk()
                    
                    # IF Empty == store it
                    if (bestQOR[threadID] == None):
                        bestQOR[threadID] = (dest, QOR)
                    #else if better value, then add
                    elif (bestQOR[threadID][1] > QOR):
                        bestQOR[threadID] = (dest, QOR)
                    
                for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                    if 0 <= x2 < mapWidth and 0 <= y2 < mapHeight and (x2, y2) not in visited:
                        que.append(path + [(x2, y2)])
                        visited.add((x2, y2))
                      
    def findBest(current, bigList):
        size = len(bigList)
        halfway = size/2
        
        if halfway.is_integer():
            halfway = int(halfway)
        
        quarter = halfway/2
        if quarter.is_integer():
            quarter = int(halfway)
        
        list1 = bigList[0:quarter]
        list2 = bigList[quarter:halfway]
        list3 = bigList[halfway:halfway+quarter]
        list4 = bigList[halfway+quarter:size]
        
        one = threading.Thread(target=getBestQOR, args=(1, current, list1,))
        two = threading.Thread(target=getBestQOR, args=(2, current, list2, ))
        three = threading.Thread(target=getBestQOR, args=(3, current, list3, ))
        four = threading.Thread(target=getBestQOR, args=(4, current, list4, ))
        
        one.start()
        two.start()
        three.start()
        four.start()
        
        one.join()
        two.join()
        three.join()
        four.join()
        
    def routeCalc(self):
        self.inputList = read_from_csv("test_cases/small/{}".format(self.filename))
        
        #generating list destinations
        for item in self.inputList:
            #generating list of waste
            mapObject = plasticObject(item[listID], item[listLat], item[listLong], item[listType], item[listValue], item[listRisk])
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
            finalFile.write("{},{},{},{},{},{}\n".format(idDesignation, item.getLatCord, item.getLongCord, item.getObjectType, item.getPlasticAmount, item.getRisk))
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