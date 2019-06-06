from tkinter import *

def clear():
    pass


def darkMode():
    root.configure(background="black")
    for wid in widgets:
        if wid == mainframe:
            wid.config(bg="black")
        else:
            wid.config(bg="black", fg="white")

def lightMode():
    root.configure(background=dbg)
    for wid in widgets:
        wid.config(bg=dbg, fg="black")

root = Tk()
dbg = root.cget("background")
mainframe = Frame(root)

# Define menu widgets
menu = Menu(root)
canvas = Canvas(mainframe, width = 200, height = 500)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Edit", menu=filemenu)
filemenu.add_command(label="Clear", command = clear)
filemenu.add_command(label="Dark Mode", command = darkMode)
filemenu.add_command(label="Light Mode", command = lightMode)

campLabel = Label(mainframe, text="Camp Kidney", font = ("Courier New", 20))
infoLabel = Label(mainframe, text="Kid Info", font = ("Courier New", 20))
nameLabel = Label(mainframe, text="Full name:", font = ("Courier New", 14))
dateOfBirthLabel = Label(mainframe, text="Date of Birth", font = ("Courier New", 14))
monthLabel = Label(mainframe, text="Month:", font = ("Courier New", 14))
dayLabel = Label(mainframe, text="Day:", font = ("Courier New", 14))
yearLabel = Label(mainframe, text="Year:", font = ("Courier New", 14))

months = list(range(1, 12))
days = list(range(1, 31))
daysOdd = list(range(1, 30))
daysFeb = list(range(1, 28))
years = list(range(2000, 2019))

nameVar = StringVar()
nameEntry = Entry(mainframe)

monthVar = IntVar()
monthEntry = Spinbox(mainframe, textvariable = monthVar, values=months)
dayVar = IntVar()
dayEntry = Spinbox(mainframe, textvariable = dayVar, values = days)
yearVar = IntVar()
yearEntry = Spinbox(mainframe, textvariable = yearVar, values = years)

scrollbar = Scrollbar(mainframe, command=canvas.yview)
canvas.configure(yscrollcommand = scrollbar.set)

widgets = [mainframe, infoLabel, menu, filemenu, campLabel, nameLabel, nameEntry, dateOfBirthLabel]

#Grid
root.minsize(width=900, height=600)
root.maxsize(width=1000, height=700)
mainframe.grid(padx = 10, pady = 10)
campLabel.grid(row=1, column=1, padx = 30, pady = 30)
infoLabel.grid(row=1, column=2, padx = 30, pady = 30)
nameLabel.grid(row=2, column=1, sticky = "W")
nameEntry.grid(row=3, column=1)
dateOfBirthLabel.grid(row=4, column=1, sticky = "W")
dayLabel.grid(row=5, column=1)
dayEntry.grid(row=6, column = 1)
monthLabel.grid(row=7, column=1)
monthEntry.grid(row=8, column=1)
yearLabel.grid(row=9, column=1)
yearEntry.grid(row=10, column = 1)

root.mainloop()