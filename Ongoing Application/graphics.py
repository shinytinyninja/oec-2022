from tkinter import *
# ==============================================================================
# MAIN PY FILE OCEAN WASTE NAVIGATION PROGRAM
# ==============================================================================
def graphics(waste, localSorters,regionalSorters, recyclers, routeList):
    # Create application window
    app = Tk("OEC-2022")
    app.geometry("850x950")

    # Defining font types as styles
    comicTitle = ("Comic Sans MS", 25)
    comicSub = ("Comic Sans MS", 15)
    comicText = ("Comic Sans MS", 10)

    # Create container for title & legend data
    topFrame = Frame(app)
    topFrame.pack(side="top")

    # Create Title
    label = Label(topFrame, text="Ocean Waste Navigation System",
                  font=comicTitle)
    label.pack()

    # Create Legend
    legendLabel = Label(topFrame, text="Legend", font=comicSub)
    legendLabel.pack()

    # Start Create Legend Data =================================================
    wasteText = Label(topFrame, text="Plastic Waste -", font=comicText)
    wasteText.pack(side="left")

    wasteLabel = Label(topFrame, text="Green", bg="green", font=comicText)
    wasteLabel.pack(side="left")

    localSorterText = Label(topFrame, text="Local Sorter -", font=comicText)
    localSorterText.pack(side="left")

    localSorterLabel = Label(topFrame, text="Yellow",
                             bg="yellow", font=comicText)
    localSorterLabel.pack(side="left")

    regionSortText = Label(topFrame, text="Regional Sorter -", font=comicText)
    regionSortText.pack(side="left")

    regionSortLabel = Label(topFrame, text="Orange",
                            bg="orange", font=comicText)
    regionSortLabel.pack(side="left")

    recyclerText = Label(topFrame, text="Recycler -", font=comicText)
    recyclerText.pack(side="left")

    recyclerLabel = Label(topFrame, text="Red", bg="red", font=comicText)
    recyclerLabel.pack(side="left")
    # End Create Legend Data ===================================================

    # Create buffer frame for spacing text
    buffer = Frame(app)
    buffer.pack(side="top")
    recyclerLabel = Label(buffer, text="")
    recyclerLabel.pack(side="left")

    # Create container for housing stats
    stats = Frame(app)
    stats.pack(side="top")
    recyclerLabel = Label(
        stats, text="Distance Driven: Baree Miles", font=comicText)
    recyclerLabel.pack(side="left")

    recyclerLabel = Label(
        stats, text="Trash Picked Up: {}".format(len(waste)), font=comicText)
    recyclerLabel.pack(side="left")

    recyclerLabel = Label(
        stats, text="Estimated Time:  2Hr 30Min", font=comicText)
    recyclerLabel.pack(side="left")

    # Create Map
    canvas = Canvas(app, bg="#86bdd6", height=800, width=800)
    canvas.pack(side="bottom")

    # Get all objects
    biggie = []
    biggie = waste + localSorters + regionalSorters + recyclers
    itemCount = 0

    for obi in biggie:
        if(obi.getObjectType() == "waste"):
            cdawg = "yellow" if itemCount == 0 else "green"
        elif(obi.getObjectType() == "local_sorting_facility"):
            cdawg = "purple"
        elif(obi.getObjectType() == "regional_sorting_facility"):
            cdawg = "black"
        elif(obi.getObjectType() == "regional_recycling_facility"):
            cdawg = "red"

        canvas.create_oval(
            (((obi.getLatCord()+200)*2)-1,
             ((obi.getLongCord()+200)*2)-2,
             ((obi.getLatCord()+200)*2)+2,
             ((obi.getLongCord()+200)*2)+2),
            fill=cdawg
        )

        itemCount = itemCount + 1

    # Draws the direct path between destinations
    for counter in range(0, len(routeList) - 1):
        nextDest = routeList[counter + 1]
        canvas.create_line(
            (((routeList[counter].getLatCord()+200)*2)-1,
             ((routeList[counter].getLongCord()+200)*2)-1,
             ((nextDest.getLatCord()+200)*2)+1,
             ((nextDest.getLongCord()+200)*2)+1),
            fill='black', width="1"
        )

    # Starts this bad boy up
    print("done")
    app.mainloop()
