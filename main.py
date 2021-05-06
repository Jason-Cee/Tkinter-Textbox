from tkinter import *

root = Tk()
root.geometry("500x300")

root.config(bg='#a52b34')

root.title("Adding two numbers")

# Labels
label1 = Label(root, text="Enter First Number: ")
label2 = Label(root, text="Enter Second Number:")
label3 = Label(root, text="Answer: ")
label4 = Label(root)

First_Number = Entry(root)
Second_Number = Entry(root)
total = Entry(root)


# Defining Functions
def button_clear():
    total.delete(0, END)
    First_Number.delete(0, END)
    Second_Number.delete(0, END)


def button_add():
    dig_a = First_Number.get()
    dig_b = Second_Number.get()
    first_add = int(dig_a)
    second_add = int(dig_b)
    sum = first_add + second_add
    total.insert(0, sum)


def button_exit():
    import sys
    sys.exit()


# Button Functions
button_add = Button(root, borderwidth=4, font="Serif", text="Add", bg="#d3c797", fg="black", width=8,
                    command=button_add)
button_clear = Button(root, borderwidth=4, font="Serif", text="Clear", bg="#d3c797", fg="black", width=8,
                      command=button_clear)
button_exit = Button(root, borderwidth=4, font="Serif", text="Exit", bg="#d3c797", fg="black", width=8,
                     command=button_exit)

# Display
label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)
label3.grid(row=2, column=0, padx=10, pady=10)
First_Number.grid(row=0, column=1, padx=10, pady=10)
Second_Number.grid(row=1, column=1, padx=10, pady=10)
total.grid(row=2, column=1, padx=10, pady=10)

# Button Location
button_add.place(x=20, y=150)
button_clear.place(x=200, y=150)
button_exit.place(x=380, y=150)
root.mainloop()
