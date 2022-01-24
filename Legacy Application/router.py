from audioop import mul
import multiprocessing
from plasticObject import plasticObject
from validator import *
from plasticObject import plasticObject
from pathThread import pathThread
from pathProcess import pathProcess
from worker import worker
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

        winners = []

        size = len(bigList)
        halfway = size/2
        halfway = int(halfway)

        quarter = halfway/2
        quarter = int(quarter)

        eighth = quarter/2
        eighth = int(eighth)

        list1 = bigList[0:eighth]
        list2 = bigList[eighth:quarter]
        list3 = bigList[quarter:quarter+eighth]
        list4 = bigList[quarter+eighth:halfway]
        list5 = bigList[halfway:halfway+eighth]
        list6 = bigList[halfway+eighth:halfway+quarter]
        list7 = bigList[halfway+quarter:halfway+quarter+eighth]
        list8 = bigList[halfway+quarter+eighth:size]
        # one = pathProcess(1, current, bigList)

        # one = pathThread(1, current, bigList)
        # two = pathThread(2, current, list2)
        # three = pathThread(3, current, list3)
        # four = pathThread(4, current, list4)

        # five = pathThread(1, current, list5)
        # six = pathThread(1, current, list6)
        # seven = pathThread(1, current, list7)
        # eight = pathThread(1, current, list8)

        myList = [
            bigList[0:eighth], bigList[eighth:quarter],
            bigList[quarter:quarter+eighth],
            bigList[quarter+eighth:halfway],
            bigList[halfway:halfway + eighth],
            bigList[halfway+eighth:halfway+quarter],
            bigList[halfway+quarter:halfway+quarter+eighth],
            bigList[halfway+quarter+eighth:size]
        ]
        
        myList = [
            bigList[0:halfway], 
            bigList[halfway:size]
        ]

        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        listOfProc = []
        for i in range(2):
            thd = multiprocessing.Process(
                target=worker, args=(i, current, myList[i], return_dict))
            thd.start()
            listOfProc.append(thd)
        
        for proc in listOfProc:
            proc.join()
            
        # one = pathProcess(1, current, list1, winners)
        # two = pathProcess(2, current, list2, winners)
        # three = pathProcess(3, current, list3, winners)
        # four = pathProcess(4, current, list4, winners)

        # five = pathProcess(1, current, list5, winners)
        # six = pathProcess(1, current, list6, winners)
        # seven = pathProcess(1, current, list7, winners)
        # eight = pathProcess(1, current, list8, winners)

        # one.start()
        # two.start()
        # three.start()
        # four.start()

        # five.start()
        # six.start()
        # seven.start()
        # eight.start()

        # one.join()
        # two.join()
        # three.join()
        # four.join()

        # five.join()
        # six.join()
        # seven.join()
        # eight.join()

        # winners = [one.getWinner(), two.getWinner(), three.getWinner(), four.getWinner(), five.getWinner(), six.getWinner(), seven.getWinner(), eight.getWinner()]
        lowest = 0

        # print(winners)
        
        # return_dict
        
        for key in return_dict:
            if len(return_dict[key]) == 0:
                pass
            else:
                if lowest == 0:
                    lowest = return_dict[key][1]
                    lowestDest = return_dict[key][0]
                elif return_dict[key][1] < lowest:
                    lowest = return_dict[key][1]
                    lowestDest = return_dict[key][0]
                    
        # for win in winners:
        #     if len(win) == 0:
        #         pass
        #     else:
        #         if lowest == 0:
        #             lowest = win[1]
        #             lowestDest = win[0]
        #         elif win[1] < lowest:
        #             lowest = win[1]
        #             lowestDest = win[0]

        self.masterList.append(lowestDest)

    def routeCalc(self):
        if self.mode == "Y":
            print("Reading CSV")
        try:
            self.inputList = read_from_csv(
                "test_cases/{}".format(self.fileName))

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
