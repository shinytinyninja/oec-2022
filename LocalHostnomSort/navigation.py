from tkinter import *
from turtle import color
from router import *

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# ==============================================================================
# MAIN PY FILE OCEAN WASTE NAVIGATION PROGRAM
# ==============================================================================

def main():
    file = input("Name of file: ")
    mode = "N"

    # Initialize Router Class Object. To be used for calculations of path.
    rout = router(file, mode)

    # Perform Main Calculations
    rout.routeCalc()

    # Getting lists of all points
    waste = rout.getWaste()
    localSorters = rout.getLocalSort()
    regionalSorters = rout.getRegionalSort()
    recyclers = rout.getRegionalRec()

    # Get the desired boat route as a list
    routeList = rout.getMaster()

    biggie = waste + localSorters + regionalSorters + recyclers

   
    
    xList = []
    yList = []
    for dest in localSorters:
        xList.append(int(dest.getLongCord()))
        yList.append(int(dest.getLatCord()))
    xValues = np.array(xList)
    yValues = np.array(yList)
    plt.scatter(xValues, yValues, facecolors="none", edgecolors="yellow")
    
    xList = []
    yList = []
    for dest in regionalSorters:
        xList.append(int(dest.getLongCord()))
        yList.append(int(dest.getLatCord()))
    xValues = np.array(xList)
    yValues = np.array(yList)
    plt.scatter(xValues, yValues, facecolors="none", edgecolors="purple")
    
    xList = []
    yList = []
    for dest in recyclers:
        xList.append(int(dest.getLongCord()))
        yList.append(int(dest.getLatCord()))
    xValues = np.array(xList)
    yValues = np.array(yList)
    plt.scatter(xValues, yValues, facecolors="none", edgecolors="brown")
    
    xList = []
    yList = []
    for dest in routeList:
        xList.append(int(dest.getLongCord()))
        yList.append(int(dest.getLatCord()))
    xValues = np.array(xList)
    yValues = np.array(yList)
    plt.plot(xValues, yValues, color="black")
    
    xList = []
    yList = []
    
    for dest in waste:
        xList.append(int(dest.getLongCord()))
        yList.append(int(dest.getLatCord()))
    xValues = np.array(xList)
    yValues = np.array(yList)
    plt.scatter(xValues, yValues, color="green")
    
    
    start = patches.Rectangle((int(waste[0].getLongCord()) - 2.5, int(waste[0].getLatCord()) - 2.5), 5, 5, linewidth=1, edgecolor="r", facecolor="r")
    plt.xlabel("Latitude")
    ax = plt.axes()
    ax.set_facecolor("#87ceeb")
    ax.add_patch(start)
    
    plt.ylabel("Longtitude")
    plt.title("Open Sea Navigation")
    
    plt.axhline(0, color='white')
    plt.axvline(0, color='white')

    
    path = os.path.dirname(os.path.abspath(__file__))
    # plotName = "map.svg"
    # plt.savefig(os.path.join(path, plotName))
    
    figure = plt.gcf()
    figure.set_size_inches(16, 9)
    
    # p = Path(os.getcwd())
    # os.chdir(p.parent)
    # p = str(p) + "/LocalHostnomSort/maps/{}.svg".format(file)
    plt.savefig("oec-2022/LocalHostnomSort/maps/{}.svg".format(file), dpi = 700, bbox_inches='tight')
    
    # plt.show()
    
if __name__ == "__main__":
    main()
