from tkinter import *
from math import pi

root = Tk()
root.title("Ösen Kalkulator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_enter():
    myLabel = Label(root, text=e.get())
    myLabel.pack()
    

#Define Button

# Buttons that store the nummber that is being displayed in the entry into a Variable
myButton_d_cable = Button(root, text="D.Leitung", padx=49, command=button_enter)
myButton_d_screw = Button(root, text="D.Schraube", padx=45, command=button_enter)
myButton_l_cable = Button(root, text="L.Leitung", padx=50, command=button_enter)

# Buttons that calculate according to the Variables given

myButton_two_osen = Button(root, text="Zwei", padx=50, command=button_enter)
myButton_one_osen = Button(root, text="Eine", padx=50, command=button_enter)

 


# Put button on the screen
myButton_d_cable.grid(row=1, column=0)
myButton_d_screw.grid(row=2, column=0)
myButton_l_cable.grid(row=3, column=0)

myButton_one_osen.grid(row=1, column=1)
myButton_two_osen.grid(row=2, column=1)


root.mainloop()

