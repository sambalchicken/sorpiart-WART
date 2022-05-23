# sorpiart
Raspberry Pi project on "Painting with Sound"

## To run Tkinter GUI on boot
In order to run your tkinter gui script (**e.g. main.py**) everytime the **Raspberry Pi** boots up, we can utilise on **autostart**. 

### Configuration (autostart)
1. open terminal
2. change directory to **.config**
2.1 `cd .config/`
3. Create an **autostart** folder
3.1 `mkdir autostart`
4. copy **tkinterautostart.desktop** into the folder
4.1 `cp ~/sorpiart/tkinterautostart.desktop ~/.config/autostart/`
5. edit **tkinterautostart.desktop** 
5.1 `nano tkinterautostart.desktop`

## To install sox library (pix2music)
In order for **pix2music.py** to work, the **Raspberry Pi** will require the **Sound Exchange (sox)** library to be installed.

To install **sox**
1. open terminal
2. `sudo apt install sox`