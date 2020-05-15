import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter.filedialog import askdirectory
import os.path
import time
import shutil



import guiDrill



def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def create_DB(self):
    conn = sqlite3.connect ('guiDrill.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_file( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            file_name TEXT \
            mTime DATETIME \
            )")
        conn.commit()
    conn.close()

   




def choose_file(self):
    try:
        self.name = askdirectory(title = 'path')
        self.txt_filepath.insert(INSERT,self.name)
    except:
        print('No File Exist')


def choose_file1(self):
    try:
        self.name1 = askdirectory(title = 'path')
        self.txt_filepath_2.insert(INSERT,self.name1)
    except:
        print('No File Exist')

def check_files(self):
    
    
    dir_list = os.listdir(self.name)
    print (dir_list)


    for file in dir_list:
        src = self.txt_filepath
        dest = self.txt_filepath_2
    

        if (file.endswith('.txt')):
            abPath = os.path.join(self.name, file)
            mTime = os.path.getmtime(abPath)
            print (file, mTime)
            shutil.move(file, dest)
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_file(file_name, mTime) VALUES (?,?)", \
                    (file))
                conn.commit()
    conn.close()
            
         

        







        
if __name__ == "__main__":
    pass
