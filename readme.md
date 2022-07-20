## Creating A GUI with integrated SoX library
### Using Tkinter for the GUI
First thing to do is to import Python GUI Tkinter module:
`from tkinter import as *`
>Note: (*) refers to all variables, methods, etc.
>
Next, to create a window, along with title and size:
```
main = Tk()  
main.title("Musical GUI")  
main.minsize(800, 980)
```
Add a loop at the end:
`main.mainloop()`
>To run application forever, as long as the window is not closed.
>>Note: The loop should always be placed at the **last** line!
### Setting up variables and list (of lists)
box and mainbox shall be used for **columns** and **rows** respectively:
```
box = [i for i in range(8)]
for i in range(8):  
    box[i] = 0  
mainbox = [j for j in range(15)]  
for j in range(15):  
    mainbox[j] = [box[i] for i in range(8)]
```
Output for each line of code above if printed:
```
Output:
[0,1,2,3,4,5,6,7]
-
[0,0,0,0,0,0,0,0]
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
-
[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
...]
```
>The mainbox contains 15 of box : "[0,0,0,0,0,0,0,0]" in its list.

### Make a grid of buttons (15x8)
Create 8 columns and 15 rows of buttons:
```
for x in range(15):  
    for y in range(8):  
        button = Button(main, text="{},{}".format(x, y),
        width=5, height=3, fg='black')  
        button.grid(row=x, column=y)  
        button.config(bg='white', highlightbackground=
        'white',command=lambda send_var=(x, y, button):
        func(send_var)
```
>Command to **toggle** buttons whenever clicked.
>>Also, a **grid** layout is mainly used in this GUI.

It should look like this:
![Tkinter 15x8 grid image](https://ibb.co/0ZrPSzN)

Function to **toggle** buttons between 1 and 0 (with colour change):
```
def func(get_var):  
    button = get_var[2]  
    if mainbox[get_var[0]][get_var[1]] == 0:  
        mainbox[get_var[0]][get_var[1]] = 1  
  button.config(highlightbackground='green', 
  highlightthickness='0', fg='red', bg='green')  
    else:  
        mainbox[get_var[0]][get_var[1]] = 0  
  button.config(highlightbackground='white',
  fg='black', bg='white')
```
### Dropdown & slider for notes, type and BPM selection

```
profiles = ['pluck', 'sine', 'square', 'triangle', 'sawtooth', 'trapezium']  
profilesInsert = StringVar()  
profilesInsert.set("sine")  
profileDropdown = OptionMenu(main, profilesInsert, *profiles)  
profileDropdown.grid(rowspan=3, row=2, column=9)  
profileDropdown.config(width=9, height=2)  
key = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']  
keyInsert = StringVar()  
keyInsert.set("C4")  
keyDropdown = OptionMenu(main, keyInsert, *key)  
keyDropdown.grid(rowspan=3, row=3, column=9)  
keyDropdown.config(width=9, height=2)  
BPM = IntVar()  
BPM.set(60)  
BPMScale = Scale(main, variable=BPM, from_=60, to=180, orient=HORIZONTAL)  
BPMScale.grid(rowspan=3, row=4, column=9)  
BPMLabel = Label(main, text='BPM(60-180)')  
BPMLabel.grid(rowspan=2, row=5, column=9)
```
>The profiles, keys and BPM are to be stored in **variables** for implementation of sound library.
>>Both key and profile are **strings** type while BPM is suppose to be an **integer** type. Hence, the StringVar() and IntVar(). 
### Ready to import sound library and install SoX
Import sound library module:
`from pix2music.py install * `
>Note: Ensure file is in same folder directory as GUI.

Installation of SoX:
`sudo apt install sox`
### Play, clear and reset buttons
A play button is needed to eventually send out **selected** buttons. To improve the GUI, clear and reset buttons were added.
This is how to do it:
```
playbutton = Button(main, text="Play Sound", 
padx=20, pady=20, command=print_toggle).grid(rowspan=4, 
row=0, column=9)  
clearbutton = Button(main, text="Clear", padx=30, 
pady=10, command=clearbtn).grid(rowspan=3, row=6, 
column=9)  
resetbutton = Button(main, text="Reset", padx=30, 
pady=10, command=resetbtn).grid(rowspan=3, row=7, 
column=9)
```
Each button comes with their **separate** functions:
```
def print_toggle():  
    print(keyInsert.get(), profilesInsert.get(), BPM.get())  
    print("TOGGLE(CURRENT):\n{}".format(mainbox))  
    pix2music(profilesInsert.get(), BPM.get(), keyInsert.get(), mainbox)  
    
def clearbtn():  
    for i in main.winfo_children():  
        i.config(highlightbackground='white', fg='black', bg='white')  
    for j in range(15):  
        mainbox[j] = [box[i] for i in range(8)]  
    print("TOGGLE(CURRENT): \n{}".format(mainbox))  
  
def resetbtn():  
    profilesInsert.set("sine")  
    keyInsert.set("C4")  
    BPM.set(60)  
    clearbtn()
```
#### Explanation of functions above:
- print_toggle() sends selected profile, key, BPM and buttons to pix2music ; to play sound.
- clearbtn() clears selected buttons, turning them back to its original state (white background, 0).
- resetbtn() resets selected profile, key, BPM and buttons to its original state.

### Final GUI look
![Final GUI look.](https://ibb.co/wgNwy5z)