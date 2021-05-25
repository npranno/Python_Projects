from tkinter import *
import tkinter as tk

import transfer_main
import transfer_func


def load_gui(self):

    self.lbl_browse1 = tk.Label(self.master,text='Select all of the files you wish to transfer.')
    self.lbl_browse1.grid(row=0,column=0,columnspan=2,padx=(1,1),pady=(1,1),sticky=N+E+S+W)
    
    self.btn_browse1 = tk.Button(self.master,width=12,height=2,text='Source Folder',command=lambda: transfer_func.browseFolder1(self))
    self.btn_browse1.grid(row=1,column=0,padx=(1,1),pady=(1,1),sticky=N+E+S+W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=2,text='Destination Folder',command=lambda: transfer_func.browseFolder2(self))
    self.btn_browse2.grid(row=1,column=1,padx=(1,1),pady=(1,1),sticky=N+E+S+W)
    self.btn_fileCheck = tk.Button(self.master,width=12,height=2,text='Check Files',command=lambda: transfer_func.fileCheck(self))
    self.btn_fileCheck.grid(row=2,column=0,columnspan=2,padx=(1,1),pady=(1,1),sticky=N+E+S+W)
    self.btn_exit = tk.Button(self.master,width=12,height=2,text='Exit',command=lambda: transfer_func.ask_quit(self))
    self.btn_exit.grid(row=3,column=0,columnspan=2,padx=(1,1),pady=(1,1),sticky=N+E+S+W)

    
if __name__ == "__main__":
    pass
