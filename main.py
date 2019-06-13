from tkinter import *
from tkinter import messagebox
# from PIL import ImageTk, Image
root = Tk()

firstName = []
lastName = []
monthDob = []
dayDob = []
yearDob = []
gender = []
program = []
price = []
discount = []
address = []
city = []
province = []
country = []
postal = []
phone = []
livesWith = []
title1 = []
parentName1 = []
relationship1 = []
phoneType1 = []
phone1 = []
email1 = []
title2 = []
parentName2 = []
relationship2 = []
phoneType2 = []
phone2 = []
email2 = []
pricePaid = []
payment = []
discount = []
creditNumber = []
cvv = []
expiryDate = []

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

programPriceVar = DoubleVar()
programPriceVar.set(0.00)
programPrice = [0.00, 100.00, 100.00, 100.00, 500.00, 350.00, 50.00, 700.00, 1000.00, 10.00, 1.00, 0.00, 2000.00]

def limitSizeCode(*args):
    value = postalVar.get()
    if len(value) > 6: postalVar.set(value[:6])

def limitSizePhone(*args):
    value = phoneVar.get()
    if len(value) > 10: phoneVar.set(value[:10])

def limitSizeParentPhone1(*args):
    value = number1Var.get()
    if len(value) > 10: number1Var.set(value[:10])

def limitSizeParentPhone2(*args):
    value = number2Var.get()
    if len(value) > 10: number2Var.set(value[:10])

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
fullName1Label = Label(parent1Frame, text="Full Name: ")
fullName1Entry = Entry(parent1Frame, textvariable=fullName1Var, width=40)
relationship1Var = StringVar()
relationship1Label = Label(parent1Frame, text="Relationship: ")
relationship1Entry = Entry(parent1Frame, textvariable=relationship1Var, width=40)
numberType1Var = StringVar()
numberType1Var.set("Work")
phone1Label = Label(parent1Frame, text="Phone:")
workCheck1 = Radiobutton(parent1Frame, text="Work", value="Work", variable=numberType1Var)
cellCheck1 = Radiobutton(parent1Frame, text="Cell", value="Cell", variable=numberType1Var)
number1Var = StringVar()
number1Var.trace('w', limitSizeParentPhone1)
number1Entry = Entry(parent1Frame, textvariable=number1Var)
email1Var = StringVar()
email1Label = Label(parent1Frame, text="Email:")
email1Entry = Entry(parent1Frame, textvariable=email1Var, width=40)


genderOption2 = LabelFrame(parent2Frame, text="Parent/Guardian #1:", font = ("Courier New", 10))
parentVar2 = StringVar()
parentVar2.set("Mr.")
mrCheck2 = Radiobutton(parent2Frame, text="Mr.", variable=parentVar2, value="Mr.")
mrsCheck2 = Radiobutton(parent2Frame, text="Mrs.", variable=parentVar2, value="Mrs.")
msCheck2 = Radiobutton(parent2Frame, text="Ms.", variable=parentVar2, value="Ms.")
missCheck2 = Radiobutton(parent2Frame, text="Miss.", variable=parentVar2, value="Miss.")
drCheck2 = Radiobutton(parent2Frame, text="Dr.", variable=parentVar2, value="Dr.")
fullName2Var = StringVar()
fullName2Label = Label(parent2Frame, text="Full Name: ")
fullName2Entry = Entry(parent2Frame, textvariable=fullName2Var, width=40)
relationship2Var = StringVar()
relationship2Label = Label(parent2Frame, text="Relationship: ")
relationship2Entry = Entry(parent2Frame, textvariable=relationship2Var, width=40)
numberType2Var = StringVar()
numberType2Var.set("Work")
phone2Label = Label(parent2Frame, text="Phone:")
workCheck2 = Radiobutton(parent2Frame, text="Work", value="Work", variable=numberType2Var)
cellCheck2 = Radiobutton(parent2Frame, text="Cell", value="Cell", variable=numberType2Var)
number2Var = StringVar()
number2Var.trace('w', limitSizeParentPhone2)
number2Entry = Entry(parent2Frame, textvariable=number2Var)
email2Var = StringVar()
email2Label = Label(parent2Frame, text="Email:")
email2Entry = Entry(parent2Frame, textvariable=email2Var,width=40)


#Payment info

def limitSizeCreditNumber(*args):
    value = creditNumberVar.get()
    if len(value) > 16: creditNumberVar.set(value[:16])

def limitSizeCvv(*args):
    value = cvvVar.get()
    if len(value) > 3: cvvVar.set(value[:3])

yearExpiry = list(range(19, 27))

paymentFrame = LabelFrame(infoFrame, text="Payment Info", font = ("Courier New", 10))
paymentTypeVar = StringVar()
paymentTypeVar.set("Visa")
paymentTypeFrame = LabelFrame(paymentFrame, text="Payment Type", font = ("Courier New", 10))
visaCheck = Radiobutton(paymentTypeFrame, text="Visa", value="Visa", variable=paymentTypeVar)
mcCheck = Radiobutton(paymentTypeFrame, text="Mastercard", value="Mastercard", variable=paymentTypeVar)
amexCheck = Radiobutton(paymentTypeFrame, text="American Express", value="American Express", variable=paymentTypeVar)
paymentDetailsFrame = LabelFrame(paymentFrame, text="Payment Details", font = ("Courier New", 10))
creditNumberVar = StringVar()
creditNumberVar.trace('w', limitSizeCreditNumber)
creditNumberLabel = Label(paymentDetailsFrame, text="16 Digit Number:", font = ("Courier New", 10))
creditNumberEntry = Entry(paymentDetailsFrame, textvariable=creditNumberVar)
cvvVar = StringVar()
cvvVar.trace('w', limitSizeCvv)
cvvLabel = Label(paymentDetailsFrame, text="3 digits on back:", font = ("Courier New", 10))
cvvEntry = Entry(paymentDetailsFrame, textvariable=cvvVar, width=10)
expiryDateMonthVar = IntVar()
expiryDateYearVar = IntVar()
expiryLabel = Label(paymentDetailsFrame, text="Expiry Date: ", font = ("Courier New", 10))
expiryMonthMenu = Spinbox(paymentDetailsFrame, textvariable = expiryDateMonthVar, values=months, width=5)
slashLabel = Label(paymentDetailsFrame, text="/")
expiryYearMenu = Spinbox(paymentDetailsFrame, textvariable = expiryDateYearVar, values=yearExpiry, width=5)

#Price
def checkProgram():
    i = 0
    for item in programs:
        if programs[i] == programVar.get():
            programPriceVar.set(programPrice[i])
            if discountVar.get() != 0:
                programPriceVar.set(programPrice[i] * discountVar.get())
            else:
                pass
        else:
            i += 1
            continue


priceFrame = Frame(paymentFrame)
dollarLabel = Label(priceFrame, text="$", font = ("Courier New", 12))
priceLabel = Label(priceFrame, textvariable=programPriceVar, font = ("Courier New", 12))
priceButton = Button(priceFrame, text="Get Price", command = checkProgram)

discountFrame = LabelFrame(paymentFrame, text="Discount?")
discountVar = DoubleVar()
discountVar.set
discountCheck = Checkbutton(discountFrame, text="Dani Shaft Deal (5% off)", onvalue=0.950, offvalue=0, variable=discountVar, font = ("Courier New", 10))

#Regframe declarations
scrollbar = Scrollbar(regframe)
listBox = Listbox(regframe, width = 75)
listBox.grid(row=2, column=1)
# bind listbox to scrollbar
listBox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listBox.yview)

i = 0
counteri = 0
studentCount = 1

def enterInfo():
    global counteri
    global i
    global studentCount
    firstName.append(firstNameVar.get())
    lastName.append(lastNameVar.get())
    listBox.insert(counteri, str(i + 1) + ". " + firstName[i] + " " + lastName[i])

    counteri += 1

    monthDob.append(monthVar.get())
    dayDob.append(dayVar.get())
    yearDob.append(yearVar.get())
    listBox.insert(counteri, "- " + str(dayDob[i]) + "-" + str(monthDob[i]) + "-" + str(yearDob[i]))

    counteri += 1

    gender.append(genderVar.get())
    listBox.insert(counteri, "- " + gender[i])

    counteri+=1

    program.append(programVar.get())
    price.append(programPriceVar.get())
    listBox.insert(counteri, "- Signed up for " + program[i] + " and being charged $" + str(price[i]))

    counteri+=1

    if discountVar.get() != 0: #Check if child applied with discount
        discount.append(discountVar.get())
        listBox.insert(counteri, "- Applied with a discount of " + str(discount[i]) + "%")
        counteri+=1
    else:
        pass

    address.append(addressVar.get())
    city.append(cityVar.get())
    province.append(provinceVar.get())
    country.append(countryVar.get())
    postal.append(postalVar.get())
    listBox.insert(counteri, "- " + address[i] + " " + city[i] + ", " + province[i] + ", " + postal[i] + ", " + country[i])

    counteri += 1

    livesWith.append(childLivesWithVar.get())
    listBox.insert(counteri, "- Lives with " + livesWith[i])

    counteri += 1

    title1.append(parentVar1.get())
    parentName1.append(fullName1Var.get())
    relationship1.append(relationship1Var.get())
    phoneType1.append(numberType1Var.get())
    email1.append(email1Var.get())
    listBox.insert(counteri, "- Parent 1: " + title1[i] + parentName1[i] + ", child's " + relationship[i])

    i += 1
    counteri += 1

enterButton = Button(infoFrame, text="Enter info", command=enterInfo)

# for i in range(100):
#     for i in kids[i]:
#         listbox.insert(END)

# bind listbox to scrollbar
listBox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listBox.yview)

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
fullName1Label.grid(row=3, column=1)
fullName1Entry.grid(row=3, column=2, columnspan = 5)
relationship1Label.grid(row=4, column=1)
relationship1Entry.grid(row=4, column=2, columnspan = 5)
phone1Label.grid(row=5, column=1)
workCheck1.grid(row=5, column=2)
cellCheck1.grid(row=5,column=3)
number1Entry.grid(row=5, column=4)
email1Label.grid(row=6, column=1)
email1Entry.grid(row=6, column=2, columnspan = 5)


genderOption2.grid(row = 2, column = 1)
mrCheck2.grid(row = 2, column = 1)
mrsCheck2.grid(row = 2, column = 2)
msCheck2.grid(row = 2, column = 3)
missCheck2.grid(row = 2, column = 4)
drCheck2.grid(row = 2, column = 5)
fullName2Label.grid(row=3, column=1)
fullName2Entry.grid(row=3, column=2, columnspan = 5)
relationship2Label.grid(row=4, column=1)
relationship2Entry.grid(row=4, column=2, columnspan = 5)
phone2Label.grid(row=5, column=1)
workCheck2.grid(row=5, column=2)
cellCheck2.grid(row=5,column=3)
number2Entry.grid(row=5, column=4)
email2Label.grid(row=6, column=1)
email2Entry.grid(row=6, column=2, columnspan = 5)

#price
priceFrame.grid(row=1, column=3, sticky='w')
dollarLabel.grid(row=1, column=1, sticky="s")
priceLabel.grid(row=1, column=2, sticky='s')
priceButton.grid(row=2, column=1, sticky='s', columnspan=2)

discountFrame.grid(row=1, column=2, sticky='w')
discountCheck.grid(row=1, column=1)

paymentFrame.grid(row=5, column = 1)
paymentTypeFrame.grid(row=1, column=1)
visaCheck.grid(row=1, column=1)
mcCheck.grid(row=1, column=2)
amexCheck.grid(row=1, column=3)
paymentDetailsFrame.grid(row=2, column=1, columnspan=3)
creditNumberLabel.grid(row=1, column=1)
creditNumberEntry.grid(row=1, column=2)
cvvLabel.grid(row=1, column=3)
cvvEntry.grid(row=1, column=4)
expiryLabel.grid(row=1, column=5)
expiryMonthMenu.grid(row=1, column=6)
slashLabel.grid(row=1, column=7)
expiryYearMenu.grid(row=1, column=8)

enterButton.grid(row=6, column=1)



# creditButton.grid(row=1, column=1)
root.mainloop()