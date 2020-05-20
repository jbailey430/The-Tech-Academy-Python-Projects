#
# Python Ver:   3.8.2
#
# Author:       Jacob R. Bailey
#
# Purpose:      Drill assignment, creating a script that creates a GUI
#
# Tested OS:  This code was written and tested to work with Windows 10.



import tkinter as tk
from tkinter import *
import guiDrill_func






class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame. __init__ (self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(600,175)
        self.master.maxsize(600,175)
        guiDrill_func.center_window(self,600,175)
        self.master.title('Check files')
        self.master.config(bg='lightgray')
        
       
        
            
        self.button = tk.Button(self.master, text='Broswe...', width=12,command = lambda: guiDrill_func.choose_file(self))
        self.button.grid(row=1,column=0,padx=(20,0),pady=(20,0))
        self.button1 = tk.Button(self.master, text='Broswe...', width=12,command = lambda: guiDrill_func.choose_file1(self))
        self.button1.grid(row=2, column=0,padx=(20,0) ,pady=(20,0))
        self.button2 = tk.Button(self.master, text='Check for files...',height=2, width=12, command = lambda: guiDrill_func.check_files(self))
        self.button2.grid(row=3,column=0, rowspan=2,padx=(20,0), pady=(20,0))
        self.button3 = tk.Button(self.master, text='Close Program',height=2, width=12, command=self.master.destroy)
        self.button3.grid(row=3,column=1, rowspan=2, padx=(350,0), pady=(20,0))

        self.txt_filepath = tk.Entry(self.master, width=70, text='')
        self.txt_filepath.delete(0, END)
        self.txt_filepath.insert(END,'')
        self.txt_filepath.grid(row=1,column=1,padx=(20,0) ,pady=(20,0))
        self.txt_filepath_2 = tk.Entry(self.master, width=70, text='')
        self.txt_filepath_2.delete(0, END)
        self.txt_filepath_2.insert(END,'')
        self.txt_filepath_2.grid(row=2,column=1,padx=(20,0) ,pady=(20,0))





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
