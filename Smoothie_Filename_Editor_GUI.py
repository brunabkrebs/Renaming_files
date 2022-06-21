"""
File name: Smoothie_Filename_Editor_GUI.py
Author: Bruna Krebs Kutche
Date created: 08/16/2020
Python version: 3.7
"""

import tkinter
from tkinter import *
from tkinter import filedialog
import os

#Set up GUI coordinates

gui = tkinter.Tk()
gui.title('Smoothie: Filename Editor')
gui.geometry("550x375")
gui.grid_columnconfigure(0,minsize=30)
gui.grid_columnconfigure(2,minsize=10)

for rows in range(0,11):
    gui.grid_rowconfigure(rows,minsize=20)

taglabel = Label(gui,text='by Bruna Krebs Kutche, 2020', font='Arial 12', fg='#AAB7B8',justify='left', anchor='w').grid(row=18, column=1,sticky=tkinter.W, pady=5)
emptylabel = Label(gui, text='', width=20, font='Arial 16').grid(row=14,column=1, sticky=tkinter.W, padx=15, pady=15)

#Select directory

def findfolder():
    folder = filedialog.askdirectory(initialdir="/", title="Select Folder")
    os.chdir(folder)
    selectedlocation = Label(gui, text=folder, font='Arial 12', height='1', width='40', justify='left', anchor='w', borderwidth = 2, relief="ridge").grid(row=2,column=1,sticky=tkinter.W)

folderlabel = Label(gui, text='Where are the files located?', font="Arial 16", height='1',justify='left', anchor='w').grid(row=1,column=1, sticky=tkinter.W)
browsebutton = tkinter.Button(gui, text="Browse", width=7, font='Arial 10', command=findfolder).grid(row=1,column=2, sticky=tkinter.W, padx=5)

#Set word to substitute and new word

oldwordlabel = Label(gui, text='What word do you want to substitute?', font="Arial 16", height='1',justify='left', anchor='w').grid(row=4,column=1, sticky=tkinter.W)
newwordlabel = Label(gui, text='What word do you want to replace it with?', font="Arial 16", height='1',justify='left', anchor='w').grid(row=7,column=1, sticky=tkinter.W)

oldwordvar = tkinter.StringVar()
oldwordentry = Entry(gui, textvariable=oldwordvar, width=6, font="Arial 12")
oldwordentry.grid(row=4, column=2, sticky=tkinter.W, padx=5)

newwordvar = tkinter.StringVar()
newwordentry = Entry(gui, textvariable=newwordvar, width=6, font="Arial 12")
newwordentry.grid(row=7, column=2, sticky=tkinter.W, padx=5)

#Rename the files

def renamefiles():
        currentfolder = os.getcwd()
        oldword = oldwordentry.get()
        newword = newwordentry.get()

        for file in os.listdir(currentfolder):
            if oldword in file:
                oldname = file
                newname = file.replace(oldword,newword)
                oldpathandname = os.path.join(currentfolder, oldname)
                newpathandname = os.path.join(currentfolder, newname)
                os.rename(oldpathandname, newpathandname)
        
renamebutton = tkinter.Button(gui, text="Rename Files", width=20, font='Arial 16', command=renamefiles).grid(row=10,column=1, sticky=tkinter.W, padx=65)

gui.mainloop()
