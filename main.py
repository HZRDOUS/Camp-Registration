from tkinter import *

def doNothing():
    print("Owo")


def darkMode():
    root.configure(background="black")
    for wid in widgets:
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
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Edit", menu=filemenu)
filemenu.add_command(label="Clear", command = doNothing)
filemenu.add_command(label="Dark Mode", command = darkMode)
filemenu.add_command(label="Light Mode", command = lightMode)

infoLabel = Label(mainframe, text="Camp Kidney", font = ("Courier New", 20))



widgets = [infoLabel, menu, filemenu]

#Grid
root.minsize(width=700, height=600)
root.maxsize(width=800, height=700)
mainframe.grid(padx = 25, pady = 25)
infoLabel.grid(row=1, column=1)

root.mainloop()
