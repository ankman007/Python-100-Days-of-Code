import math
from tkinter import *

# Labels, Button, Entry(Input Field), Text(Text Box),
# Spinbox(Counter), Scale, Radiobutton, Checkbutton, Listbox

def calculate():
    miles = int(user_input.get())
    km = miles * 1.60934
    result.config(text=round(km, 2))
    # user_input.delete(0, END)


window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=400, height=200)
window.config(padx=60, pady=60)

miles_label = Label(text='Miles')
miles_label.grid(column=3, row=1)

user_input = Entry()
user_input.grid(column=2, row=1)

equal_label = Label(text='is equal to')
equal_label.grid(column=1, row=2)

result = Label(text='0')
result.grid(column=2, row=2)

km_label = Label(text='Km')
km_label.grid(column=3, row=2)

btn = Button(text='Calculate', command=calculate, border=1)
btn.grid(column=2, row=3)

window.mainloop()
