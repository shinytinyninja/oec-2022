import collections
import queue
import threading
from plasticObject import plasticObject
from validator import *
from plasticObject import plasticObjec
# ==============================================================================
# Main Python File
# ==============================================================================
masterList = []
bestQOR = []

listID = 0
listLat = 1
listLong = 2
listType = 3
listValue = 4
listRisk = 5

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
    
def main():
    print("Hello World")
    
    filename = input("name of the file your would like to run: ")
    inputList = read_from_csv("test_cases/small/{}".format(filename))
    
    wastePlaces = []
    localSortPlaces = []
    regSortPlaces = []
    regRecPlaces = []
    
    #generating list destinations
    for item in inputList:
        #generating list of waste
        mapObject = plasticObject(item[listID], item[listLat], item[listLong], item[listType], item[listValue], item[listRisk])
        if mapObject.getObjectType() == "waste":
            wastePlaces.append(mapObject)
            masterList.append(mapObject)
            
        #generating list of waste
        elif mapObject.getObjectType() == "local_sorting_facility":
            localSortPlaces.append(mapObject)
        
        #generating list of waste
        elif  mapObject.getObjectType() == "regional_sorting_facility":
            regSortPlaces.append(mapObject)
        
        #generating list of waste
        else: #item[3] == "regional_recycling_facility"
            regRecPlaces.append(mapObject)


    #Collect Waste
    
    #Find Local Sorting
    findBest(masterList[-1], localSortPlaces)
    
    #Find Regional Sorting
    findBest(masterList[-1], regSortPlaces)
    
    #Find Regional Recycling
    findBest(masterList[-1], regRecPlaces)
    
    
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
    
if __name__ == "__main__":
    main()
    
