from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)


#label


my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="top")


my_label["text"] = "New Text"
my_label.config(text="altro text")


#button


def button_clicked():
    testo = input.get()
    my_label.config(text=testo)


button = Button(text="Click Me", command=button_clicked)
button.pack()



#entry

input = Entry(width=30)
# add some text to begin with
input.insert(END, string="Some text to begin with.")
input.pack()



#text
text = Text(height=5, width=30)
# puts cursor in textbox
text.focus()
# adds some text to begin with
text.insert(END, "Example of multi-line text entry.")
# get's current value in textbox at line 1, character 0
print(text.get("1.0",END))
text.pack()


#spinbox

def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#scale
# called with current scale value
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#checkbutton

def checkbutton_used():
    # prints 1 if on button checked, otherwise 0
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


#radiobutton

def radio_used():
    print(radio_state.get())
# variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()



#listbox

def listbox_used(event):
    # gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()






window.mainloop()