from tkinter import *

app = Tk("OEC-2022")
app.geometry("800x850")


# def get_x_and_y(event):
#     global lasx, lasy
#     lasx, lasy = event.x, event.y

# def draw_smth(event):
#     global lasx, lasy
#     canvas.create_line((lasx, lasy, event.x, event.y), fill='red', width=2)
#     lasx, lasy = event.x, event.y
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

canvas = Canvas(app, bg="#86bdd6", height=800, width=800)
canvas.pack(side="bottom")

canvas.create_oval((200-2, 200-2, 200+3, 200+3), fill='green') # waste is green
canvas.create_oval((100, 200, 105,205), fill="yellow") # local sorter is yellow
canvas.create_oval((600, 200, 600, 200), fill="orange") #regional sorter is orange
canvas.create_oval((300, 500, 300,500), fill="red") #reycler is red

# canvas.bind("<Button-1>", get_x_and_y)
# canvas.bind("<B1-Motion>", draw_smth)



# path=r'C:\Users\Zotac\Desktop\OEC 2022\oec-2022\picture.jpg'
# image = Image.open(path)
# image = image.resize((400,400), Image.ANTIALIAS)
# image = ImageTk.PhotoImage(image)
# canvas.create_image(0,0, image=image, anchor='nw')


app.mainloop()






