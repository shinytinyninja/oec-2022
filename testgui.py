import tkinter as tk

def main():
    print("starting carnival Routing")
    # main GUI window
    window = tk.Tk()
    # GUI Window initial size
    window.geometry("1800x1000")

    # create necessary frames for buttons and matrix output
    topFrame = tk.Frame(window)
    topFrame.pack(side = 'top')

    botFrame = tk.Frame(window)
    botFrame.pack(side = "bottom")

    # top label
    header = tk.Label(topFrame, text = "OEC Plastic Tracker", font=(112))
    header.pack(side ="top")

    info = tk.Label(topFrame, text = "The first stop added is the start point. The last stop added is the end point.")
    info.pack(side ="top")
    info2 = tk.Label(topFrame, text = "All stops inbetween are what is calculated.")
    info2.pack(side ="top")

    currHeight = 0
    currLength = 0

    for currHeight in range(0, 400):
            newFrame = tk.Frame(botFrame)
            newFrame.pack(side = "top")
            for currWidth in range(0, 400):
                attractionObject = tk.Label(newFrame, bg = "red", relief="groove", height=1, width=1)
                attractionObject.pack(side ="left")

    window.mainloop()

if __name__ == "__main__":
    main()
