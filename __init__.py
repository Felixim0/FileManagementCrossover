from tkinter import filedialog
from tkinter import *
import sys
from pathlib import Path

googleDriveDirectory  = ''

def getUserWindow():
    global googleDriveDirectory
    googleDriveDirectory = filedialog.askdirectory()


def getAllPaths():
    global googleDriveDirectory
    print('Beginnging')
    if googleDriveDirectory == '':
        print('No src Directory provided')
        return ''
    paths = []
    for path in Path(googleDriveDirectory).rglob('*'):
        paths.append(path)

    for p in paths:
        print(p)
    return paths

class mainWindow(object):
    def __init__(self,master):
        global googleDriveDirectory
        self.master=master
        self.b=Button(master,text="Select Start Directory",
            command=getUserWindow)
        self.b.pack()
        self.b2=Button(master,text="Print to Check Working Directory",
            command=lambda: print(googleDriveDirectory))
        self.b2.pack()

        self.b3=Button(master,text="Find all files and directories",
            command= getAllPaths)
        self.b3.pack()

if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)
    root.mainloop()