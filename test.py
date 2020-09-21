from tkinter import *
from math import pi
from tkinter import messagebox

root = Tk()
root.title("Ösen Kalkulator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# function that shows the end result after the program calculates the formula that is given


def first_formula():
    result = d_cable + d_screw * pi + d_screw + 1 * 2 + l_cable + d_screw
    messagebox.showinfo("Länge Leitung", str(result) + "mm")


def second_formula():
    result = d_cable + d_screw * pi + d_screw + 1 * 2 + l_cable + d_screw * 2
    messagebox.showinfo("Länge Leitung", str(result) + "mm")


# functions that show the integer that got saved into their respective global variables
def d_cable_show():
    messagebox.showinfo("D. Leitung",
                        str(d_cable))


def d_screw_show():
    messagebox.showinfo("D. Schraube",
                        str(d_screw))


def l_cable_show():
    messagebox.showinfo("D. Leitung",
                        str(l_cable))

# functions of the buttons


def button_enter_1():  # saves the diameter of the cable
    number = e.get()
    global d_cable
    d_cable = float(number)
    d_cable_show()
    e.delete(0, END)


def button_enter_2():  # save the diameter of the screw
    number = e.get()
    global d_screw
    d_screw = int(number)
    d_screw_show()
    e.delete(0, END)


def button_enter_3():  # save the desired length of the cable
    number = e.get()
    global l_cable
    l_cable = int(number)
    l_cable_show()
    e.delete(0, END)


# Define Button
# Buttons that store the nummber that is being displayed in the entry into a Variable
myButton_d_cable = Button(root, text="D.Leitung",
                          padx=49, command=button_enter_1)
myButton_d_screw = Button(root, text="D.Schraube",
                          padx=45, command=button_enter_2)
myButton_l_cable = Button(root, text="L.Leitung",
                          padx=50, command=button_enter_3)

# Buttons that calculate according to the Variables given

myButton_two_osen = Button(root, text="Zwei", padx=50, command=second_formula)
myButton_one_osen = Button(root, text="Eine", padx=50, command=first_formula)


# Put button on the screen
myButton_d_cable.grid(row=1, column=0)
myButton_d_screw.grid(row=2, column=0)
myButton_l_cable.grid(row=3, column=0)

myButton_one_osen.grid(row=1, column=1)
myButton_two_osen.grid(row=2, column=1)

root.mainloop()
