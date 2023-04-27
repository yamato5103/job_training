import tkinter as tk

root=tk.Tk()
root.geometry("240x240")
root.title("GUI Sample")

button= tk.Button(root,text="hello")

button.pack()
root.mainloop()