import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)


#label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 30, "bold"))
my_label.pack(side="top")











window.mainloop()