from doctest import master
import threading
from unittest.util import three_way_cmp
from validator import *

masterList = []

def getBestQOR( currentLocation, listofDestinations):
    print(id)
    global masterList
    
def startThreading(current, list1, list2, list3, list4):
    one = threading.Thread(target=getBestQOR, args=(current, list1,))
    two = threading.Thread(target=getBestQOR, args=(current, list2, ))
    three = threading.Thread(target=getBestQOR, args=(current, list3, ))
    four = threading.Thread(target=getBestQOR, args=(current, list4, ))
    
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
        if item[3] == "waste":
            wastePlaces.append((item[1], item[2]))
        #generating list of waste
        elif item[3] == "local_sorting_facility":
            localSortPlaces.append((item[1], item[2]))
        #generating list of waste
        elif  item[3] == "regional_sorting_facility":
            regSortPlaces.append((item[1], item[2]))
        #generating list of waste
        else: #item[3] == "regional_recycling_facility"
            regRecPlaces.append((item[1], item[2]))

    #Collect Waste
    
    #Find Local Sorting
    startThreading()
    
    #Find Regional Sorting
    startThreading()
    
    #Find Regional Recycling
    startThreading()
    
    
    # minQor = 100
    # for pair in masterList:
    #     if(pair[0] < minQor):
    #         minQor == pair[0]
    
    #Writing to final CSV
    finalFile = open("finalFile.csv", "w")
    for item in masterList:
        finalFile.write()
    finalFile.close()
    
if __name__ == "__main__":
    main()
    
