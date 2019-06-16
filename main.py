from tkinter import *
from tkinter import messagebox
root = Tk()

firstName = []
lastName = []
monthDob = []
dayDob = []
yearDob = []
gender = []
program = []
pricePaid = []
address = []
city = []
province = []
country = []
postal = []
phone = []
livesWith = []

root.title("Camp Kidney Registration 2019")
root.iconbitmap("lazlo.ico")
mainframe = Frame(root)
infoFrame = Frame(mainframe)
regframe = Frame(mainframe)

# Define menu widgets
menu = Menu(root)
canvas = Canvas(mainframe, width = 200, height = 500)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Edit", menu=filemenu)
#filemenu.add_command(label="Clear", command = clear)

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
firstNameEntry = Entry(nameFrame,  textvariable = firstNameVar,)
lastNameVar = StringVar()
lastNameChildLabel = Label(nameFrame, text="Last Name:", font = ("Courier New", 8))
lastNameEntry = Entry(nameFrame,  textvariable = lastNameVar,)
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

#Programs
programFrame = LabelFrame(kidInfo, text="Program:", font = ("Courier New", 10))
session1Var = StringVar()
session1Check = Checkbutton(programFrame, text="Session 1", variable=session1Var, onvalue="Session 1", offvalue="")
session2Var = StringVar()
session2Check = Checkbutton(programFrame, text="Session 2", variable=session2Var, onvalue="Session 2", offvalue="")
session3Var = StringVar()
session3Check = Checkbutton(programFrame, text="Session 3", variable=session3Var, onvalue="Session 3", offvalue="")
session4Var = StringVar()
session4Check = Checkbutton(programFrame, text="Session 4", variable=session4Var, onvalue="Session 4", offvalue="")

programVar = StringVar()
programs = ["Session 1", "Session 2", "Session 3", "Session 4"]

programPriceVar = DoubleVar()
programPriceVar.set(0.00)
programPrice = [0.00, 100.00, 100.00, 100.00, 500.00, 350.00, 50.00, 700.00, 1000.00, 10.00, 1.00, 0.00, 2000.00]

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
    otherEntry.config(state=NORMAL)
    childLivesWithVar.set(otherVar)


def disableOther(): #Check to see if the "Other" radio button is enabled so it doesn't interfere with both variables
    enable.set(False)
    otherEntry.configure(state = DISABLED)


childLivesWithFrame = LabelFrame(homeInfo, text="Child Lives With:", font = ("Courier New", 10), width = 300)
childLivesWithVar = StringVar()
childLivesWithVar.set("Both Parents")
bothCheck = Radiobutton(childLivesWithFrame, text="Both Parents", variable = childLivesWithVar, value="Both Parents", command = disableOther)
fatherCheck = Radiobutton(childLivesWithFrame, text="Father", variable = childLivesWithVar, value="Father", command = disableOther)
motherCheck = Radiobutton(childLivesWithFrame, text="Mother", variable = childLivesWithVar, value="Mother", command = disableOther)
grandparentCheck = Radiobutton(childLivesWithFrame, text="Grandparents", variable = childLivesWithVar, value="Grandparents", command = disableOther)
guardianCheck = Radiobutton(childLivesWithFrame, text="Guardian(s)", variable = childLivesWithVar, value="Guardian(s)", command = disableOther)
otherVar = StringVar()
otherEntry = Entry(childLivesWithFrame, textvariable = otherVar, state=DISABLED)
enable = BooleanVar()
otherCheck = Radiobutton(childLivesWithFrame, text="Other", variable=otherVar, value=True, command = enableOther)

d = 0
def checkPrice():
    global d
    global price
    print(d)
    price = 0
    vars = [session1Var.get(), session2Var.get(), session3Var.get(), session4Var.get()]
    string = ""
    program.append([])
    #print(d) #Debugging to make sure y is a good value
    #print(program[d]) #Debugging to check the index values
    if len(program[d]) != 0:
        program[d].clear()
        #print(program[d]) #Debugging to make sure list is being cleared properly
    for session in vars:
        if session not in string:
            price += 20
            program[d].append(session)
        else:
            continue
    #print(program[d]) #Debugging to make sure 2D list is being configured properly
    programPriceVar.set("{:.2f}".format(price))


priceFrame = Frame(kidInfo)
dollarLabel = Label(priceFrame, text="$", font = ("Courier New", 12))
priceLabel = Label(priceFrame, textvariable=programPriceVar, font = ("Courier New", 12))
priceButton = Button(priceFrame, text="Get Price", command = checkPrice)

#Regframe declarations
scrollbar = Scrollbar(regframe)
listBox = Listbox(regframe, width = 75, height=10)
listBox.grid(row=2, column=1, columnspan=2)
# bind listbox to scrollbar
listBox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listBox.yview)

scrollbar = Scrollbar(regframe)
listBox2 = Listbox(regframe, width = 75, height=10)

listBox2.grid(row=4, column=1, columnspan=2)
# bind listbox to scrollbar
listBox2.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listBox2.yview)

programSearchVar = StringVar()
programSearchMenu = OptionMenu(regframe, programSearchVar, *programs)
programSearchMenu.grid(row=3, column=1)

lineNum = 0
z = 0
def enterInfo():
    global d
    global z
    global lineNum
    requiredVarsGet = [firstNameVar.get(), lastNameVar.get(), addressVar.get(), cityVar.get(), provinceVar.get(), countryVar.get(), postalVar.get(), phoneVar.get()]
    requiredVars = [firstNameVar, lastNameVar, addressVar, cityVar, provinceVar, countryVar, postalVar, phoneVar]
    for x in requiredVarsGet:
        if len(x) == 0:
           messagebox.showerror("Error", "Error: A required field has been left blank. Please go back and check to see if your info has been entered correctly!")
           return
        else:    
           continue
    if programPriceVar.get() == 0:
        messagebox.showerror("Error", "Error: You have not gotten the price paid for the child. Please get the price and try again!")
        return

    firstName.append(firstNameVar.get() + " " + lastNameVar.get())
    monthDob.append(monthVar.get())
    dayDob.append(dayVar.get())
    yearDob.append(yearVar.get())
    gender.append(genderVar.get())
    pricePaid.append(programPriceVar.get())
    address.append(addressVar.get())
    city.append(cityVar.get())
    province.append(provinceVar.get())
    country.append(countryVar.get())
    postal.append(postalVar.get())
    phone.append(phoneVar.get())
    livesWith.append(childLivesWithVar.get())    
    listBox.insert(lineNum, f"{firstName[z]}")

    for x in requiredVars:
        x.set("")
    lineNum += 1
    d += 1
    z += 1

def programSearch():
    if listBox2.size() != 0:
        listBox2.delete(0, END)
    selectedProgram = programSearchVar.get()
    global p
    p = 0
    o = 0 
    for child in firstName:
        for subitem in range(len(program[p])):
            print(subitem)
            if selectedProgram in program[p][subitem]:
                listBox2.insert(p, child)
                #print(program[p][subitem])
            elif selectedProgram not in program[p][subitem]:
                continue
        p += 1

#programMenuVar = StringVar()
#programMenu = OptionMenu(programFrame, programVar, *programs)
#programMenu.configure(font = ("Courier New", 10))
searchButton = Button(regframe, text="Search", command = programSearch).grid(row=3, column=2)


def getInfo():
    global counteri
    global i
    global y
    i = 0
    selection = listBox.curselection()
    print(selection)
    for child in firstName:
        if child in listBox.get(selection, END):
            i = int(selection[0])
        else:
            continue
    print(i)
    print(program[i])
    s = ""
    for t in range(len(program[i])):
        print(t)
        s += str(program[i][t])
        if program[i][t] == program[i][(len(program[i]) - 1)]:
            s += "."
        else:
            s += ", "
    print(s)
    
    lines = [f"Info on {firstName[i]}",
                f"Born {monthDob[i]}/{(dayDob[i])}/{(yearDob[i])}",
                f"Charged ${pricePaid[i]:.2f} for {s}",
                f"Lives on {address[i]}, {city[i]}, {province[i]}, {postal[i]}, {country[i]}",
                f"Lives with {livesWith[i]}",
                f"Can be contacted at {phone[i]}"]

    messagebox.showinfo("Child Info", "\n".join(lines))

enterButton = Button(infoFrame, text="Enter info", command=enterInfo)
showInfoButton = Button(regframe, text="Show Child Info", command = getInfo).grid(row=1, column=2)
# bind listbox to scrollbar
listBox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listBox.yview)

#Grid
root.minsize(width=1100, height=700)
root.maxsize(width=1200, height=900)
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
nameFrame.grid(row=1, column=1, rowspan = 5, padx = 10, pady = 10)
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
programFrame.grid(row=3, column=2, columnspan=3)
session1Check.grid(row=1, column=1)
session2Check.grid(row=1, column=2)
session3Check.grid(row=1, column=3)
session4Check.grid(row=1, column=4)

#homeInfo gridding
#Home Info
primaryInfoFrame.grid(row=1, column=1, sticky = "S")
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

#Child Lives With?
childLivesWithFrame.grid(row = 2, column = 1, columnspan = 8)
bothCheck.grid(row = 1, column = 1)
fatherCheck.grid(row = 1, column = 2)
motherCheck.grid(row = 1, column = 3)
grandparentCheck.grid(row = 1, column = 4)
guardianCheck.grid(row = 1, column = 5)
otherCheck.grid(row = 1, column = 6)
otherEntry.grid(row = 1, column = 7)

#price
priceFrame.grid(row=5, column=1, columnspan=3, sticky='s')
dollarLabel.grid(row=1, column=1, sticky="s")
priceLabel.grid(row=1, column=2, sticky='s')
priceButton.grid(row=2, column=1, sticky='s', columnspan=2)

enterButton.grid(row=6, column=1)


# creditButton.grid(row=1, column=1)
root.mainloop()