import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showerror
from tkinter.font import Font

top = tkinter.Tk("Haris's tab")
font = Font(family="Helvetica", size = 12)
alertFont = Font(family="Helvetica", size = 18)
top.geometry("500x600")
top.configure(background = 'light blue')


welcomeLabel = Label(top, text = "Welcome to the COVID 19 Risk Calculator", background = 'light blue', font = font)
welcomeLabel.pack(side = TOP)

ageLabel = Label(top, text = "Age", background = 'light blue', font = font)
ageLabel.place(x=10, y = 90)

ageEntry = Entry(top, bd = 5)
ageEntry.place(x=90, y = 90)

ethnicityLabel = Label(top, text = "Ethnicity", background = 'light blue', font = font)
ethnicityLabel.place( x = 10, y =150)

ethnicityEntry = Entry(top, bd = 5)
ethnicityClick = StringVar()
ethnicityDrop = OptionMenu(top, ethnicityClick, "White", "Chinese", "Mixed", "Indian",
                  "Bangladeshi", "Pakistani", "Middle Eastern", "Black", "Other")
ethnicityDrop.place(x = 90, y = 150)

genderLabel = Label(top, text = "Gender", background = 'light blue', font = font)
genderLabel.place(x = 10, y = 210)

varGender = IntVar()

female = Radiobutton(top, text = "Female",  value = 1, variable = varGender, background = 'light blue', font = font)
female.place( x = 70, y = 210)

male = Radiobutton(top, text = "Male",  value = 2, variable = varGender, background = 'light blue', font = font)
male.place( x = 150, y = 210)

healthLabel = Label(top, text = "Underlying health conditions?", background = 'light blue', font = font)
healthLabel.place(x = 10, y = 270)

varHealth = IntVar()

healthNone= Radiobutton(top, text = "None",  value = 4, variable = varHealth, background = 'light blue', font = font)
healthNone.place( x = 220, y = 270)

healthOne = Radiobutton(top, text = "One",  value = 1, variable = varHealth, background = 'light blue', font = font)
healthOne.place( x = 290, y = 270)

healthTwo = Radiobutton(top, text = "Two",  value = 2, variable = varHealth, background = 'light blue', font = font)
healthTwo.place( x = 350, y = 270)

healthThree = Radiobutton(top, text = "Three or more",  value = 3, variable = varHealth, background = 'light blue',
                          font = font)
healthThree.place( x = 220, y = 290)

pregnancyLabel = Label(top, text = "Are you pregnant?", background = 'light blue', font = font)
pregnancyLabel.place(x = 10, y = 330)

varPregnancy = IntVar()

pregnancyUnder = Radiobutton(top, text = "Under 28 Weeks",  value = 1, variable = varPregnancy,
                             background = 'light blue', font = font)
pregnancyUnder.place( x = 140, y = 330)

pregnancyOver = Radiobutton(top, text = "Over 28 Weeks",  value = 2, variable = varPregnancy, background = 'light blue',
                            font = font)
pregnancyOver.place( x = 290, y = 330)

pregnancyNo = Radiobutton(top, text = "No",  value = 3, variable = varPregnancy, background = 'light blue', font = font)
pregnancyNo.place( x = 430, y = 330)

BMILabel = Label(top, text = "What is your BMI?", background = 'light blue', font = font)
BMILabel.place(x = 10, y = 390)

varBMI = IntVar()

BMIless23 = Radiobutton(top, text = "Less than 23",  value = 4, variable = varBMI, background = 'light blue', font = font)
BMIless23.place( x = 140, y = 390)

BMI23 = Radiobutton(top, text = "23 - 29",  value = 1, variable = varBMI, background = 'light blue', font = font)
BMI23.place( x = 260, y = 390)

BMI30 = Radiobutton(top, text = "30 - 39", value = 2, variable = varBMI, background = 'light blue', font = font)
BMI30.place( x = 340, y = 390)

BMI40 = Radiobutton(top, text = "Over 40",  value = 3, variable = varBMI, background = 'light blue', font = font)
BMI40.place( x = 420, y = 390)

vitaminLabel = Label(top, text = "Vitamin D Levels?", background = 'light blue', font = font)
vitaminLabel.place( x = 10, y = 450)


vitaminClick = StringVar()
vitaminDrop = OptionMenu(top, vitaminClick, "Less than 30", "30-50", "Over 50")
vitaminDrop.place(x = 150, y = 450)

riskLabel = Label(top, text="Risk:", background='light blue', font=alertFont)
riskLabel.place(x=150, y=510)


def calculateScore():
    score = 0
    gen = varGender.get()
    health = varHealth.get()
    ethnic= ethnicityClick.get()
    preg= varPregnancy.get()
    bmi = varBMI.get()
    vit = vitaminClick.get()
    age = ageEntry.get()
    if gen == 1:
        score = score + 1
    elif gen == 2:
        score = score + 2

    if health == 1:
        score = score + 1
    elif health == 2:
        score = score + 4
    elif health == 3:
        score = score + 7
    elif health == 4:
        score = score + 0

    if (ethnic == "Chinese") or (ethnic == "White") or (ethnic == "Mixed") or (ethnic == "Other"):
        score = score + 1
    elif ethnic == "Indian":
        score = score + 2
    elif (ethnic == "Bangladeshi") or (ethnic == "Pakistani") or (ethnic == "Middle Eastern"):
        score = score + 3
    elif ethnic == "Black":
        score = score + 4

    if preg == 1:
        score = score + 2
    elif preg == 2:
        score = score + 13
    elif preg == 3:
        score = score + 0

    if vit == 1:
        score = score + 1
    elif vit == 2:
        score = score + 2

    if bmi == 1 and (ethnic != "Chinese" or ethnic != "White" or ethnic != "Mixed"):
        score = score + 1
    elif bmi == 2 and (ethnic == "Chinese" or ethnic == "White" or ethnic == "Mixed"):
        score = score + 3
    elif bmi == 2 and (ethnic != "Chinese" or ethnic != "White" or ethnic != "Mixed"):
        score = score + 4
    elif bmi == 3:
        score = score + 7

    a = int(age)

    if a < 0:
        score = score + 0
    elif 49 > a > 40:
        score = score + 1
    elif 59 > a > 50:
        score = score + 2
    elif 69 > a > 60:
        score = score + 3
    elif a > 70:
        score = score + 13

    return score


alertLabel = Label(top, text="", background='light blue', font=alertFont)
alertLabel.place(x=250, y=510)


def buttonPress():
    age = ageEntry.get()

    try:
        age = int(age)
    except ValueError:
        showerror('Non-Int Error', 'Please enter an integer value for age')
    else:
        if 8 >= calculateScore() >= 1:
            alertLabel["text"] = "Mild Risk"
            alertLabel["background"] = 'green'
        elif 12 >= calculateScore() >= 9:
            alertLabel["text"] = "Moderate Risk"
            alertLabel["background"] = 'yellow'
        elif calculateScore() >= 12:
            alertLabel["text"] = "High Risk"
            alertLabel["background"] = 'red'
        #message = messagebox.showinfo("Risk Score", risk)





calculateBtn = Button(top, text = "Calculate", command = buttonPress, font = font)
calculateBtn.place(x = 220, y = 40)

top.mainloop()





