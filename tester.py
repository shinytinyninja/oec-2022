from tkinter import *
from router import *

# file = input("Name of file: ")

file = "test_10_equal"

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

# create application window
app = Tk("OEC-2022")
app.geometry("800x850")

# def get_x_and_y(event):
#     global lasx, lasy
#     lasx, lasy = event.x, event.y

# def draw_smth(event):
#     global lasx, lasy
#     canvas.create_line((lasx, lasy, event.x, event.y), fill='red', width=2)
#     lasx, lasy = event.x, event.y

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

for w in waste:
    canvas.create_oval((w.getLatCord()-2, w.getLongCord()-2, w.getLatCord().get+3, w.getLongCord()+3), fill='green') # waste is green
for localSort in localSorters:
    canvas.create_oval((localSort.getLatCord()-2, localSort.getLongCord()-2, localSort.getLatCord().get+3, localSort.getLongCord()+3), fill='yellow') # local sorter is yellow
for regSort in regionalSorters:
    canvas.create_oval((regSort.getLatCord()-2, regSort.getLongCord()-2, regSort.getLatCord().get+3, regSort.getLongCord()+3), fill='orange') # regional sorter is orange
for r in recyclers:
    canvas.create_oval((r.getLatCord()-2, r.getLongCord()-2, r.getLatCord().get+3, r.getLongCord()+3), fill='red') # recycler is red

# direct path
for 
# canvas.bind("<Button-1>", get_x_and_y)
# canvas.bind("<B1-Motion>", draw_smth)



# path=r'C:\Users\Zotac\Desktop\OEC 2022\oec-2022\picture.jpg'
# image = Image.open(path)
# image = image.resize((400,400), Image.ANTIALIAS)
# image = ImageTk.PhotoImage(image)
# canvas.create_image(0,0, image=image, anchor='nw')


app.mainloop()






