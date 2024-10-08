import tkinter


#Skapar fönstret
root = tkinter.Tk()
root.title("ToDoListan")

rubrik = tkinter.Label(root, text="Dina uppgifter:\n", font=("Arial", 14))
rubrik.pack()

entry = tkinter.Entry(root, width=50)
entry.pack(anchor="nw")
root.mainloop()
