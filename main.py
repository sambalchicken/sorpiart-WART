#sample template to demonstrate the functionalities of pix2music.py
#huats 2022

from tkinter import *
from pix2music import *

def play():
    global picture

    pix2music("pluck", 100, "C4", picture)
    

main = Tk()

title = Label(main, text="Press the PLAY SOUND button to start hearing sounds", font="10")
title.grid(row=0, column=0, columnspan=3)

button = Button(main, text="PLAY SOUND", font="50", width=20, height=5, command=play)
button.grid(row=1,column=0, columnspan=3)

labelsound = Label(main, text="Sound Type = Pluck")
labelbpm = Label(main, text="BPM = 100")
labelkey = Label(main, text="Key = C4")

labelsound.grid(row=2, column=0)
labelbpm.grid(row=2, column=1)
labelkey.grid(row=2, column=2)

picture = [[1,0,0,],[0,1,0],[0,0,1],[1,0,0],[0,0,1],[1,0,0],[0,0,1]]

main.mainloop()