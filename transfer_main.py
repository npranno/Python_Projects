from tkinter import *
import tkinter as tk

import transfer_gui
import transfer_func

#use frame method as a parent class that the child class will inheret from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #master frame configuration
        self.master = master
        self.master.minsize(220,155)
        self.master.maxsize(220,155)
        
        #center_window centers the program on user's screen
        transfer_func.center_window(self,500,300)
        self.master.title("Transfer Files")
        self.master.configure(bg="darkgrey")
        
        #catches if user clicks the X at the top right. built in tkinter function
        #uses ask_quit function within transfer_func file
        self.master.protocol("WM_DELETE_WINDOW", lambda: transfer_func.ask_quit(self))

        #load separate gui file into main file
        transfer_gui.load_gui(self)

        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
