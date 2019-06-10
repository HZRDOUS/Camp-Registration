from tkinter import *
from tkinter import messagebox
# from PIL import ImageTk, Image
root = Tk()

def clear():
    for var in vars:
        if var == genderVar:
            var.set("Male")
        elif var == programVar:
            var.set(programs[0])
        elif var == monthVar or var == dayVar:
            var.set(1)
        elif var == yearVar:
            var.set(2000)
        else:
            var.set("")

# def showMsg():
#     img = Image.open("shake.jpg").resize((200,200))
#     shakePhoto = ImageTk.PhotoImage(img)
#     popup = Toplevel(root)
#     popup.wm_title("HZRDOUS")
#     popup.tkraise(root) # This just tells the message to be on top of the root window.
#     mainLabel = Label(popup, text="If you like what you see, visit me at").grid(row=1, column = 2)
#     mainLabel2 = Label(popup, text="github.com/HZRDOUS to see more!").grid(row=2, column=2)
#     imgLabel = Label(popup, image=shakePhoto).grid(row=1, column = 1, rowspan=2)
#     imgLabel.image = shakePhoto

#def darkMode():
#    root.configure(background="black")
#    for wid in widgets:
#        if wid == mainframe:
#            wid.config(bg="black")
#        else:
#            wid.config(bg="black", fg="white")

#def lightMode():
#    root.configure(background=dbg)
#    for wid in widgets:
#        wid.config(bg=dbg, fg="black")

root.title("Camp Kidney Registration 2019")
root.iconbitmap()
dbg = root.cget("background")
mainframe = Frame(root)
infoFrame = Frame(mainframe)
regframe = Frame(mainframe)

# Define menu widgets
menu = Menu(root)
canvas = Canvas(mainframe, width = 200, height = 500)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Edit", menu=filemenu)
filemenu.add_command(label="Clear", command = clear)
#filemenu.add_command(label="Dark Mode", command = darkMode)
#filemenu.add_command(label="Light Mode", command = lightMode)

# creditButton = Button(mainframe, command = showMsg, width=1, height=1)

infoLabel = Label(regframe, text="Kid Info", font = ("Courier New", 20))
campLabel = Label(infoFrame, text="Camp Kidney", font = ("Courier New", 20))
campLabel2 = Label(infoFrame, text="Registration Program", font = ("Courier New", 18))
nameLabel = Label(infoFrame, text="Full name:", font = ("Courier New", 10))
dateOfBirthLabel = Label(infoFrame, text="Date of Birth:", font = ("Courier New", 10))
genderLabel = Label(infoFrame, text="Gender:", font = ("Courier New", 10))

months = list(range(1, 13))
days = list(range(1, 32))
daysOdd = list(range(1, 30))
daysFeb = list(range(1, 28))
years = list(range(2000, 2019))
#Main Labelframe Declaration
kidInfo = LabelFrame(infoFrame, text = "Child Info", font = ("Courier New", 10))
homeInfo = LabelFrame(infoFrame, text = "Household Info", font = ("Courier New", 10))

#Kidinfo
#Name
nameFrame = LabelFrame(kidInfo, text="Full Name:", font = ("Courier New", 10))
firstNameVar = StringVar()
firstNameChildLabel = Label(nameFrame, text="First Name:", font = ("Courier New", 8))
firstNameEntry = Entry(nameFrame)
lastNameVar = StringVar()
lastNameChildLabel = Label(nameFrame, text="Last Name:", font = ("Courier New", 8))
lastNameEntry = Entry(nameFrame)
#Date of Birth
dateFrame = LabelFrame(kidInfo, text = "Date of Birth:", font = ("Courier New", 10))
monthVar = IntVar()
monthEntry = Spinbox(dateFrame, textvariable = monthVar, values=months, width = 6)
dayVar = IntVar()
dayEntry = Spinbox(dateFrame, textvariable = dayVar, values = days, width = 6)
yearVar = IntVar()
yearEntry = Spinbox(dateFrame, textvariable = yearVar, values = years, width = 6)
dayLabel = Label(dateFrame, text="Day", font = ("Courier New", 10))
monthLabel = Label(dateFrame, text="Month", font = ("Courier New", 10))
yearLabel = Label(dateFrame, text="Year", font = ("Courier New", 10))
#Gender
genderFrame = LabelFrame(kidInfo, text="Gender:", font = ("Courier New", 10))
genderVar = StringVar()
genderVar.set("Male")
maleRadio = Radiobutton(genderFrame, text="Male", variable = genderVar, value="Male")
femaleRadio = Radiobutton(genderFrame, text="Female", variable = genderVar, value="Female")
# otherRadio = Radiobutton(genderFrame, text="Other", variable = genderVar, value="Other")
#Program
programFrame = LabelFrame(kidInfo, text="Program:", font = ("Courier New", 10))
programVar = StringVar()
programVar.set("--- Select Program ---")
programs = ["--- Select Program ---", "Session 1", "Session 2", "Session 3", "Fishing with Garrison Stokes", 
            "Pokemon Camp", "The Birds and Bees Talk", "Programming with Mr. Dani Shaft", 
            "Rap Talk with Hopsin", "Just Video Games", "Anime", "Advanced Functions MHF4U", 
            "Beyond Scared Straight (Camp Edition)"]
programMenu = OptionMenu(programFrame, programVar, *programs)
programMenu.configure(font = ("Courier New", 10))

def limitSizeCode(*args):
    value = postalVar.get()
    if len(value) > 6: postalVar.set(value[:6])

def limitSizePhone(*args):
    value = phoneVar.get()
    if len(value) > 10: phoneVar.set(value[:10])

#HomeInfo
primaryInfoFrame = LabelFrame(homeInfo, text="Primary Home Info", font = ("Courier New", 10))
addressVar = StringVar()
addressLabel = Label(primaryInfoFrame, text="Address:", font = ("Courier New", 10))
addressEntry = Entry(primaryInfoFrame, width = 60, textvariable = addressVar)
cityVar = StringVar()
cityLabel = Label(primaryInfoFrame, text="City/Town:", font = ("Courier New", 10))
cityEntry = Entry(primaryInfoFrame, textvariable = cityVar)
provinceVar = StringVar()
provinceLabel = Label(primaryInfoFrame, text="Province/State:", font = ("Courier New", 10))
provinceEntry = Entry(primaryInfoFrame, textvariable = provinceVar)
countryVar = StringVar()
countryLabel = Label(primaryInfoFrame, text="Country:", font = ("Courier New", 10))
countryEntry = Entry(primaryInfoFrame, textvariable = countryVar)
postalVar = StringVar()
postalVar.trace('w', limitSizeCode)
postalLabel = Label(primaryInfoFrame, text="Postal/Zip Code:", font = ("Courier New", 10))
postalEntry = Entry(primaryInfoFrame, textvariable = postalVar)
phoneVar = StringVar()
phoneVar.trace('w', limitSizePhone)
phoneLabel = Label(primaryInfoFrame, text="Phone Number:", font = ("Courier New", 10))
phoneEntry = Entry(primaryInfoFrame, width = 60, textvariable = phoneVar)

#Parent Info

def enableOther(): #Enable "Other" radio button and "Other" entry space
    value = enable.get()
    if value == True:
        otherEntry.config(state=NORMAL)
        childLivesWithVar.set(otherVar)
    else:
        otherEntry.config(state=DISABLED)

def checkOther(): #Check to see if the "Other" radio button is enabled so it doesn't interfere with both variables
    enabled = enable.get()
    if enabled == True:
        enable.set(False)
        otherEntry.configure(state = DISABLED)
    elif enabled == None:
        pass

parentInfoFrame = LabelFrame(homeInfo, text="Parent Info", font = ("Courier New", 10))
childLivesWithFrame = LabelFrame(parentInfoFrame, text="Child Lives With:", font = ("Courier New", 10), width = 300)
childLivesWithVar = StringVar()
childLivesWithVar.set("Both Parents")
bothCheck = Radiobutton(childLivesWithFrame, text="Both Parents", variable = childLivesWithVar, value="Both Parents", command = checkOther)
fatherCheck = Radiobutton(childLivesWithFrame, text="Father", variable = childLivesWithVar, value="Father", command = checkOther)
motherCheck = Radiobutton(childLivesWithFrame, text="Mother", variable = childLivesWithVar, value="Mother", command = checkOther)
grandparentCheck = Radiobutton(childLivesWithFrame, text="Grandparents", variable = childLivesWithVar, value="Grandparents", command = checkOther)
guardianCheck = Radiobutton(childLivesWithFrame, text="Guardian(s)", variable = childLivesWithVar, value="Guardian(s)", command = checkOther)
otherVar = StringVar()
otherEntry = Entry(childLivesWithFrame, textvariable = otherVar, state=DISABLED)
enable = BooleanVar()
otherCheck = Radiobutton(childLivesWithFrame, text="Other", variable=enable, value=True, command = enableOther)



parent1Frame = LabelFrame(parentInfoFrame, text="Parent 1:", font = ("Courier New", 10))
parent2Frame = LabelFrame(parentInfoFrame, text="Parent 2:", font = ("Courier New", 10))
genderOption1 = LabelFrame(parent1Frame, text="Parent/Guardian #1:", font = ("Courier New", 10))
parentVar1 = StringVar()
parentVar1.set("Mr.")
mrCheck1 = Radiobutton(parent1Frame, text="Mr.", variable=parentVar1, value="Mr.")
mrsCheck1 = Radiobutton(parent1Frame, text="Mrs.", variable=parentVar1, value="Mrs.")
msCheck1 = Radiobutton(parent1Frame, text="Ms.", variable=parentVar1, value="Ms.")
missCheck1 = Radiobutton(parent1Frame, text="Miss.", variable=parentVar1, value="Miss.")
drCheck1 = Radiobutton(parent1Frame, text="Dr.", variable=parentVar1, value="Dr.")
fullName1Var = StringVar()
fullName1Entry = Entry(parent1Frame, textvariable=fullName1Var)
relationship1Var = StringVar()
relationship1 = Entry(parent1Frame, textvariable=relationship1Var)
numberType1Var = StringVar()
phone1Label = Label(parent1Frame, text="")
workCheck1 = Radiobutton(parent1Frame, value="Work", variable=numberType1Var)
cellCheck1 = Radiobutton(parent1Frame, value="Cell", variable=numberType1Var)
number1Var = StringVar()
number1Entry = Entry(parent1Frame, textvariable=number1Var)
email1Var = StringVar()
email1Label = Label(parent1Frame, text="Email:")
email1Entry = Entry(parent1Frame, textvariable=email1Var)


genderOption2 = LabelFrame(parent2Frame, text="Parent/Guardian #1:", font = ("Courier New", 10))
parentVar2 = StringVar()
parentVar2.set("Mr.")
mrCheck2 = Radiobutton(parent2Frame, text="Mr.", variable=parentVar2, value="Mr.")
mrsCheck2 = Radiobutton(parent2Frame, text="Mrs.", variable=parentVar2, value="Mrs.")
msCheck2 = Radiobutton(parent2Frame, text="Ms.", variable=parentVar2, value="Ms.")
missCheck2 = Radiobutton(parent2Frame, text="Miss.", variable=parentVar2, value="Miss.")
drCheck2 = Radiobutton(parent2Frame, text="Dr.", variable=parentVar2, value="Dr.")

#Regframe declarations
scrollbar = Scrollbar(regframe)
listbox = Listbox(regframe, width = 75)
listbox.grid(row=2, column=1)

kids = []

# for i in range(100):
#     for i in kids[i]:
#         listbox.insert(END)

# bind listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

vars = [firstNameVar, lastNameVar, monthVar, dayVar, yearVar, genderVar, programVar, addressVar,
        cityVar, provinceVar, countryVar, postalVar, phoneVar]

widgets = [mainframe, infoLabel, menu, filemenu, campLabel, nameLabel, firstNameEntry, 
           lastNameEntry, dateOfBirthLabel]
#Grid
root.minsize(width=1100, height=700)
root.maxsize(width=1100, height=900)
#Frame Gridding
mainframe.grid(row=1, column = 1, padx = 10, pady = 10)
infoFrame.grid(row = 1, column = 1)
regframe.grid(row=1, column=2)
#Main Labelframe Gridding
kidInfo.grid(row=3, column = 1)
homeInfo.grid(row=4, column=1)
#Heading Gridding
campLabel.grid(row=1, column=1, padx = 0, pady = 0)
campLabel2.grid(row=2, column=1, padx = 10)

#infoFrame gridding
infoLabel.grid(row=1, column=1, sticky = "W")
#Kidinfo Gridding
nameFrame.grid(row=1, column=1, rowspan = 4, padx = 10, pady = 10)
firstNameChildLabel.grid(row=1, column=1)
firstNameEntry.grid(row=2, column=1)
lastNameChildLabel.grid(row=3, column=1)
lastNameEntry.grid(row=4, column=1)
dateFrame.grid(row=1, column=2)
monthLabel.grid(row=1, column=1)
monthEntry.grid(row=2, column = 1)
dayLabel.grid(row=1, column=2)
dayEntry.grid(row=2, column=2)
yearLabel.grid(row=1, column=3)
yearEntry.grid(row=2, column = 3)
genderFrame.grid(row=1, column=3, padx = 10, pady = 10)
#Gender gridding
maleRadio.grid(row = 1, column = 1, sticky="W")
femaleRadio.grid(row = 1, column = 2, sticky="W")
# otherRadio.grid(row = 1, column = 3, sticky="W")
programFrame.grid(row=4, column=2, columnspan = 3, padx = 10, pady = 10)
programMenu.grid(row=1, column=1)

#homeInfo gridding
#Home Info
primaryInfoFrame.grid(row=1, column=1, sticky = "W")
addressLabel.grid(row=1, column=1)
addressEntry.grid(row=1, column=2, columnspan = 3)
cityLabel.grid(row = 2, column=1)
cityEntry.grid(row = 2, column=2)
provinceLabel.grid(row = 2, column = 3)
provinceEntry.grid(row = 2, column = 4)
countryLabel.grid(row = 3, column = 1)
countryEntry.grid(row = 3, column = 2)
postalLabel.grid(row = 3, column = 3)
postalEntry.grid(row = 3, column = 4)
phoneLabel.grid(row = 4, column = 1)
phoneEntry.grid(row = 4, column = 2, columnspan = 3)
#Parent Info
parentInfoFrame.grid(row = 2, column = 1)

#Child Lives With?
childLivesWithFrame.grid(row = 1, column = 1, columnspan = 8)
bothCheck.grid(row = 1, column = 1)
fatherCheck.grid(row = 1, column = 2)
motherCheck.grid(row = 1, column = 3)
grandparentCheck.grid(row = 1, column = 4)
guardianCheck.grid(row = 1, column = 5)
otherCheck.grid(row = 1, column = 6)
otherEntry.grid(row = 1, column = 7)

#Parents 1 and 2
parent1Frame.grid(row = 2, column = 1)
parent2Frame.grid(row = 2, column = 2)
genderOption1.grid(row = 2, column = 1)
mrCheck1.grid(row = 2, column = 1)
mrsCheck1.grid(row = 2, column = 2)
msCheck1.grid(row = 2, column = 3)
missCheck1.grid(row = 2, column = 4)
drCheck1.grid(row = 2, column = 5)
genderOption2.grid(row = 2, column = 1)
mrCheck2.grid(row = 2, column = 1)
mrsCheck2.grid(row = 2, column = 2)
msCheck2.grid(row = 2, column = 3)
missCheck2.grid(row = 2, column = 4)
drCheck2.grid(row = 2, column = 5)


# creditButton.grid(row=1, column=1)
root.mainloop()