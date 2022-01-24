def listSplit(wasteList, numWorker):
    return (wasteList[i::numWorker] for i in range(numWorker))