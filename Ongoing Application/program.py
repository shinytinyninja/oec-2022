from graphics import *
from quadSplit import quadSplit
from listSplit import *
import math
import multiprocessing


def worker(current, listOfDests, winnerQ):
    x1_lat, y1_lon = current.getLatCord(), current.getLongCord()
    bestQOR = ()
    
    for dest in listOfDests:
        x2_lat, y2_lon = dest.getLatCord(), dest.getLongCord()
        R = 6371 
        latavg = (int(x1_lat) + int(x2_lat))/2
        x1 = R * int(y1_lon) * math.cos(latavg)
        y1 = R * int(x1_lat)
        x2 = R * int(y2_lon) * math.cos(latavg)
        y2 = R * int(x2_lat)
        hypo = math.hypot(abs(x1-x2), abs(y1-y2))/1000
        riskLevel = float(dest.getRisk()) if float(dest.getRisk()) > 0 else 1
        QOR = float(hypo) * riskLevel
        
        if len(bestQOR) == 0:
            bestQOR = (dest, QOR)
        elif (QOR < bestQOR[1]):
            bestQOR = (dest, QOR)
    winnerQ.put(bestQOR)
    
def main():
    fileName = input("Name of file: ")
    mode = "N"
    masterList = []
    
    # Initialize Quad Split Class Object. Used to divvy up csv data
    quad = quadSplit(fileName)

    # Waste, LocalSort, RegionalSort, RegionalRecycle
    quadSplit.readCSV(quad)
    quadSplit.processData(quad)

    # processedList = [
    #     quadSplit.getWasteDest(quad),
    #     quadSplit.getLocalSortDest(quad),
    #     quadSplit.getRegionalSortDest(quad),
    #     quadSplit.getRegionalRecDest(quad)
    # ]
    
    wasteDict = quadSplit.getWasteDestDict(quad)

    # Number of workers you want
    numWorkers = 4
    numWasteDest = len(wasteDict)
    
    key = list(wasteDict.keys())[0]
    masterList.append(wasteDict.pop(key))
    
    # Waste For-Loop
    for i in range(numWasteDest - 2):
        # Find Waste Location
        jobs = []
        taste = []
        multiQueue = multiprocessing.Queue()
        workerData = list(listSplit(list(wasteDict.values()), numWorkers))
        print(workerData)
        
        for i in range(numWorkers):
            p = multiprocessing.Process(target=worker, args=(masterList[-1], workerData[i], multiQueue,))
            jobs.append(p)
            p.start()

        for proc in jobs:
            proc.join()

        # Add Something to master list here
        lowestQOR = 0
        
        while multiQueue.qsize() != 0:
            winner = multiQueue.get()
            if len(winner) == 0:
                pass
            else:
                if lowestQOR == 0:
                    lowestOQR = winner[1]
                    lowestDest = winner[0]
                elif winner[1] < lowestOQR:
                    lowestOQR = winner[1]
                    lowestDest = winner[0]
    
        masterList.append(lowestDest)
        wasteDict.pop(masterList[-1].getCode())

    # Pop last waste location left as final waste destination
    print("___________________________")
    print(list(wasteDict.keys()))
    key = list(wasteDict.keys())[0]
    masterList.append(wasteDict.pop(key))
    
    for i in masterList:
        print(i.getCode())
    # for dest in waste:
    #     for workerID in range(numWorkers):
            # graphics()

if __name__ == "__main__":
    main()
