import tkinter as tk
button=tk.Button(text="click")
def buttonp():
    open("but.html")
button.config(command=buttonp)
root=tk.Tk()
button.pack()
root.mainloop()