from tkinter import *
from router import *


file = input("Name of file: ")

# file = "test_10_equal"
# file = "small/test_10_equal"

print(file)

mode = "N"
rout = router(file, mode)

# main calculations
rout.routeCalc()

# get all items to place
waste = rout.getWaste()
localSorters = rout.getLocalSort()
regionalSorters = rout.getRegionalSort()
recyclers = rout.getRegionalRec()

routeList = rout.getMaster()

# create application window
app = Tk("OEC-2022")
app.geometry("800x850")

# create legend
topFrame = Frame(app)
topFrame.pack(side ="top")

label = Label(topFrame, text = "Plastic Recycler and Sorter", font=(50))
label.pack()

legendLabel = Label(topFrame, text = "Legend:")
legendLabel.pack()

wasteText = Label(topFrame, text = "Plastic Waste -")
wasteText.pack(side="left")

wasteLabel = Label(topFrame, text="Green", bg="green")
wasteLabel.pack(side="left")

localSorterText = Label(topFrame, text = "Local Sorter -")
localSorterText.pack(side="left")

localSorterLabel = Label(topFrame, text="Yellow", bg = "yellow")
localSorterLabel.pack(side="left")

regionSortText = Label(topFrame, text="Regional Sorter -")
regionSortText.pack(side="left")

regionSortLabel = Label(topFrame, text="Orange", bg="orange")
regionSortLabel.pack(side="left")

recyclerText = Label(topFrame, text="Recycler -")
recyclerText.pack(side="left")

recyclerLabel = Label(topFrame, text="Red", bg="red")
recyclerLabel.pack(side="left")

# create map
canvas = Canvas(app, bg="#86bdd6", height=800, width=800)
canvas.pack(side="bottom")

# get waste objects

biggie = []
biggie = waste + localSorters + recyclers

for obi in biggie:
    if(obi.getObjectType() == "waste"):
        cdawg = "green"
    elif(obi.getObjectType() == "local_sorting_facility"):
        cdawg = "yellow"
    elif(obi.getObjectType() == "regional_sorting_facility"):
        cdawg = "orange"
    elif(obi.getObjectType() == "regional_recycling_facility"):
        cdawg = "red"
    
    canvas.create_oval((  ((int(obi.getLatCord())+200)*2)-2, ((int(obi.getLongCord())+200)*2)-2, ((int(obi.getLatCord())+200)*2)+3, ((int(obi.getLongCord())+200)*2)+3), fill=cdawg)


# direct path
for route in range(0, len(routeList)):
    try:
        tempObject = routeList[route + 1]
    except IndexError:
        print("")
    canvas.create_line((  ((int(routeList[route].getLatCord())+200)*2)-2, ((int(routeList[route].getLongCord())+200)*2)-2, ((int(tempObject.getLatCord())+200)*2)+3, ((int(tempObject.getLongCord())+200)*2)+3), fill='black', width="1")

app.mainloop()






