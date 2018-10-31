from tkinter import *

from PIL import Image, ImageTk
import os
from pathfile import *


def findmaxyz():
    global x, y, z
    i = 1
    z = 0
    while i != 0:
        if os.path.isdir(pathfile + '/' + str(z + 1)):
            z += 1
        else:
            i = 0
    files = os.listdir(pathfile + '/' + str(z))
    if not files:
        print("Folder is empty. Check your local data")
    else:
        x = int(files[0])
    files = os.listdir(pathfile + '/' + str(z) + '/' + str(x))
    if not files:
        print("Folder is empty. Check your local data")
    else:
        y = int(os.path.splitext(files[0])[0])


def checkpath(x, y, z):
    if os.path.exists(pathfile + '/' + str(z) + '/' + str(x) + '/' + str(y) + '.png'):
        return True
    else:
        return False


def genpath(x, y, z):
    imagepath = pathfile + '/' + str(z) + '/' + str(x) + '/' + str(y) + '.png'
    return imagepath


root = Tk()


def drawmap(x, y, z):
    global tkimage1, tkimage2, tkimage3, tkimage4
    tkimage1 = ImageTk.PhotoImage(Image.open(genpath(x, y + 1, z)))
    tkimage2 = ImageTk.PhotoImage(Image.open(genpath(x + 1, y + 1, z)))
    tkimage3 = ImageTk.PhotoImage(Image.open(genpath(x, y, z)))
    tkimage4 = ImageTk.PhotoImage(Image.open(genpath(x + 1, y, z)))
    Label(image=tkimage1).grid(row=0, column=0)
    Label(image=tkimage2).grid(row=0, column=1)
    Label(image=tkimage3).grid(row=1, column=0)
    Label(image=tkimage4).grid(row=1, column=1)


def moveright():
    global x
    if checkpath(x + 2, y, z) and checkpath(x + 2, y + 1, z):
        x += 1
        drawmap(x, y, z)


def moveleft():
    global x
    if checkpath(x - 1, y, z) and checkpath(x - 1, y + 1, z):
        x -= 1
        drawmap(x, y, z)


def moveup():
    global y
    if checkpath(x, y + 2, z) and checkpath(x + 1, y + 2, z):
        y += 1
        drawmap(x, y, z)


def movedown():
    global y
    if checkpath(x, y - 1, z) and checkpath(x + 1, y - 1, z):
        y -= 1
        drawmap(x, y, z)


def movein():
    global x, y, z
    if checkpath((x * 2) + 1, (y * 2) + 1, z + 1) and checkpath((x * 2) + 2, (y * 2) + 2, z + 1):
        z += 1
        y = (y * 2) + 1
        x = (x * 2) + 1
        drawmap(x, y, z)


def moveout():
    global x, y, z
    if checkpath(int((x - 1) / 2), int((y - 1) / 2), z - 1) and checkpath(int(((x - 1) / 2) + 1),
                                                                          int(((y - 1) / 2) + 1), z - 1):
        z -= 1
        y = int((y - 1) / 2)
        x = int((x - 1) / 2)
        drawmap(x, y, z)


findmaxyz()
drawmap(x, y, z)

left_b = Button(text="←", command=moveleft).grid(row=5, column=3)
right_b = Button(text="→", command=moveright).grid(row=5, column=5)
up_b = Button(text="↑", command=moveup).grid(row=4, column=4)
down_b = Button(text="↓", command=movedown).grid(row=5, column=4)
out_b = Button(text="-", command=moveout).grid(row=5, column=6)
in_b = Button(text="+", command=movein).grid(row=4, column=6)

root.mainloop()
