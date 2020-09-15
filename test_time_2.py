#import Tkinter as tk
from tkinter import*
import time

class App():
    def __init__(self,master):

        self.master=master
        self.label = Label(text="")
        self.label.pack()
        self.update_clock()
        

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.master.after(1000, self.update_clock)

def main():
    root = Tk()
    app=App(root)
    root.mainloop()

if __name__ == '__main__':
    main()