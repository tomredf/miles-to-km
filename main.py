from tkinter import *

window = Tk()
window.title("Miles Kilometers Converter")
window.config(padx=25, pady=25)

label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)

entry = Entry(width=5)
# Add some text to begin with
entry.insert(END, string="0")
entry.grid(column=1, row=0)

label_2 = Label(text="Miles")
label_2.grid(column=2, row=0)

label_3 = Label(text="0")
label_3.grid(column=1, row=1)

label_4 = Label(text="Km")
label_4.grid(column=2, row=1)


def action():
    m = float(entry.get())
    k = m * 1.609
    label_3["text"] = k


button = Button(text="Convert", command=action)
button.grid(column=1, row=2)












window.mainloop()