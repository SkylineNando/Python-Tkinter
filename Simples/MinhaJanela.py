from tkinter import *
class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
myapp = App()
myapp.master.title("Meu programa")
myapp.master.minsize(600, 400)
myapp.mainloop()
