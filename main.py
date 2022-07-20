from tkinter import *
from pix2music import *
from tkinter import messagebox
import tkinter.font as font
import pyautogui
from PIL import Image, ImageTk
import time
import yagmail
import json
def savepreset():
    presets.append(presetname.get())
    presetdict[presetname.get()] = mainbox
    with open('preset.json','w') as fp:
        json.dump(presetdict, fp)
    presetDD = OptionMenu(main, preset, *presets)
    presetDD.place(x=1050, y=105)
    presetDD.config(width=8, height=2,bg='white',activebackground='white')
def create_preset(createbtn):
    global savebtn,presetname
    clearbtn()
    createbtn.place_forget()
    presetname = Entry(main)
    presetname.insert(0, "New Preset")
    presetname.configure(width=15)
    presetname.place(x=1040, y=10)
    presetname.bind("<FocusIn>", lambda args:presetname.delete('0','end'))
    presetname.bind("<FocusOut>", lambda args:presetname.insert('0','New Preset'))
    savebtn = Button(main, text="Save",command=save_selected, bg='white',activebackground='white',relief='ridge', font=myFont)
    savebtn.place(x=1070, y=35)
def save_selected():
    global presetdict,presetDD, presets
    x = 0
    if presetname.get() == "":
        messagebox.showinfo(title='Error',message='Please enter a preset name.')
    else:
        if len(presets) > 3:
            del presets[-1]
            savepreset()
        else:
            savepreset()
    preset.set("")
    createbtn.place(x=1045, y=30)
    savebtn.place_forget()
    presetname.place_forget()
    clearbtn()

def bsend():
    if recEntry.get() == "":
        messagebox.showinfo(title='Error',message='No input found')
    else:
        cfm = messagebox.askquestion("Confirm Email","Are you sure?")
        if cfm == "yes":
            if recEntry.get() == "":
                messagebox.showinfo(title="Error", message="No input found!")
            else:
                yag = yagmail.SMTP("holyshuts@gmail.com","dwqeyosexupmdqkc")
                yag.send(to = recEntry.get(), contents = ["Here's your final output image", "screenshot.png","test.wav"])
                bclear()
                time.sleep(0.5)
                messagebox.showinfo(title="Update",message="Successfully sent image!")
        elif cfm == "no":
            pass
        else:
            messagebox.showerror("Error","Something went wrong!")
def bclear():
    recEntry.delete(0,"end")
def close_top():
    top.destroy()
    for w in main.winfo_children():
        w.configure(state="normal")

def takeScreenshot():
    global top, recEntry
    for w in main.winfo_children():
        w.configure(state="disabled")
    x, y = main.winfo_rootx(), main.winfo_rooty()
    w, h = main.winfo_width(), main.winfo_height()
    im1 = pyautogui.screenshot(region=(x, y, w-175, h-25))
    im1.save("screenshot.png")
    im1 = ImageTk.PhotoImage(im1)
    top = Toplevel(main)
    top.title("Screenshot(OUTPUT)")
    top.minsize(1180, 1000)
    top.maxsize(1180, 1000)
    top.geometry("+%d+%d" %(x-10,y-30))
    top.wm_transient(main)
    image1 = Label(top, image=im1)
    image1.image = im1
    image1.place(x=0, y=0)
    top.protocol("WM_DELETE_WINDOW", close_top)
    Label(top, text="Enter Email: ").place(x=1050, y=450)
    recEntry = Entry(top, textvariable = temp_rec, width=15)
    recEntry.place(x=1030, y=470)
    Button(top, text="Send",command=bsend, activebackground='lightgreen',bg='lightgreen', relief=RIDGE).place(x=1105, y=500)
    Button(top, text="Clear", command=bclear, activebackground='pink', bg='pink', relief=RIDGE).place(x=1035, y=500)
def btngreen():
    for i in range(15):
            for j in range(14):
                if mainbox[i][j] == 1:
                    button[i][j].config(activebackground='green',bg='green')
                else:
                    button[i][j].config(activebackground='white',bg='white')
def getpreset(*args):
    global mainbox
    if preset.get() == 'Happy Bdy':
        mainbox = [[0, 0, 0, 0, 1, 0, 0, 0,0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0,0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0,0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0,0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        btngreen()
    elif preset.get() == 'Jingle Bells':
        mainbox = [[0, 0, 0, 0, 0, 0, 0, 0,0, 1, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0,0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0,0, 1, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        btngreen()
    elif preset.get() == 'I Love U':
        mainbox = [[0, 0, 0, 0, 1, 0, 0, 0,0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0,0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        btngreen()
    elif preset.get() in presets:
        with open('preset.json') as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
        mainbox = jsonObject[preset.get()]
        btngreen()
def clearbtn():
    for i in range(15):
        mainbox[i] = [box[j] for j in range(14)]
    btngreen()
    
def resetbtn():
    clearbtn()
    preset.set("")
    BPM.set(60)
    profilesInsert.set("sine")
    keyInsert.set("C4")
    
def func(get_var):
    global button, mainbox, presetmainbox
    if mainbox[get_var[0]][get_var[1]] == 0:
        mainbox[get_var[0]][get_var[1]] = 1
        
        button[get_var[0]][get_var[1]].config(activebackground="green",bg='green')
    else:
        mainbox[get_var[0]][get_var[1]] = 0
        button[get_var[0]][get_var[1]].config(activebackground="white",bg='white')
        
def print_toggle():
    if mainbox == [[0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0]]:
        empty()
        resetbtn()
    else:
        pix2music(profilesInsert.get(),BPM.get(),keyInsert.get(),mainbox)
        
def empty():
    messagebox.showinfo(title='Error', message='No notes selected!')
def testbtn():
    mainbox = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    pix2music(profilesInsert.get(),BPM.get(),keyInsert.get(),mainbox)
    
main=Tk()
main.title("Musical GUI")
main.minsize(1200, 1000)
main.maxsize(1200, 1000)
notes = ["C","D","E","F","G","A","B","C","D","E","F","G","A","B"]
myFont = font.Font(family='MS Serif', size='10', weight='bold')
phone_number = StringVar()
box = [0 for j in range(14)]
mainbox = [i for i in range(15)]
for i in range(15):
    mainbox[i] = [box[j]for j in range(14)]
presetmainbox = mainbox
button = [0 for i in range(15)]
for i in range(15):
    button[i] = [0 for j in range(14)]
for i in range(15):
    for j in range(14):
        button[i][j] = Button(main, text='{}'.format(notes[j]),width=5, height=3,font=myFont)
        button[i][j].grid(row=i, column=j)
        button[i][j].config(activebackground='white', bg='white',command=lambda send_var=(i,j):func(send_var))

playbutton = Button(main,bg='white',activebackground='white', text="Play Sound", font=myFont,padx=10, pady=20, command=print_toggle, relief='ridge').place(x=1050, y=600)
clearbutton = Button(main,bg='white',activebackground='white', text="Clear", padx=30, pady=10, command=clearbtn, relief='ridge',font=myFont).place(x=1050, y=480)
resetbutton = Button(main,bg='white',activebackground='white', text="Reset", padx=30, pady=10, command=resetbtn, relief='ridge',font=myFont).place(x=1050, y=540)
quicktestbtn = Button(main,bg='white',activebackground='white', text="Quick Test", padx=10, pady=10, command=testbtn, relief='ridge',font=myFont).place(x=1050, y=700)
profiles = ['pluck', 'sine', 'square', 'triangle', 'sawtooth', 'trapezium']
profilesInsert = StringVar()
profilesInsert.set("sine")
profileDropdown = OptionMenu(main, profilesInsert, *profiles)
profileDropdown.place(x= 1050, y=200)
profileLabel = Label(main, text='Select Profile:',font=myFont)
profileLabel.place(x=1055, y=175)
profileDropdown.config(width=8, height=2,bg='white',activebackground='white')
key = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']
keyInsert = StringVar()
keyInsert.set("C4")
keyDropdown = OptionMenu(main, keyInsert, *key)
keyDropdown.place(x=1050, y=300)
keyLabel = Label(main, text='Select Key:',font=myFont)
keyLabel.place(x=1058, y=275)
keyDropdown.config(width=8, height=2,bg='white',activebackground='white')
BPM = IntVar()
BPM.set(60)
BPMScale = Scale(main, variable=BPM, from_=60, to=180, orient=HORIZONTAL)
BPMScale.config(activebackground='white',bg='white')
BPMScale.place(x=1055,y=400)
BPMLabel = Label(main, text='BPM(60-180)',font=myFont)
BPMLabel.place(x=1055, y=375)
BPMLabel.config(activebackground='white')
presets = ['Happy Bdy','I Love U','Jingle Bells']
preset = StringVar()
preset.set('')
presetDD = OptionMenu(main, preset, *presets)
presetDD.place(x=1050, y=105)
presetDD.config(width=8, height=2,bg='white',activebackground='white')
presetLabel = Label(main, text='Select Preset:', font=myFont)
presetLabel.place(x=1055, y = 80)
preset.get()
preset.trace('w',getpreset)
photo = PhotoImage(file="emailpic.png")
photobtn = Button(main, image=photo, command=takeScreenshot)
photobtn.config(width=60, height=50, bg='white',activebackground='white',relief='ridge')
photobtn.place(x=1065, y=795)
photolabel = Label(main, text='Share', font=myFont)
photolabel.place(x=1075, y=770)
temp_rec = StringVar()
presetdict = {}
createbtn = Button(main, text="Create Preset",command=lambda:create_preset(createbtn), bg='white',activebackground='white',relief='ridge', font=myFont)
createbtn.place(x=1045, y=30)
main.mainloop()
