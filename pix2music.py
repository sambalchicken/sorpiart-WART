#version 1.1 
#changes sound type, bpm and key 
#this library uses the SoX (Sound Exchange) library
#huats club 2022

import numpy as np
import subprocess

def pix2music(soundtype, bpm, noteorigin, picture):

    musickey = (['C','D','E','F','G','A','B','C','D','E','F','G','A','B','C','D','E','F','G','A','B','C'])


    #Checking if soundtype is a valid input
    if (soundtype == 'pluck' or soundtype == 'sine' or soundtype == 'square' or soundtype == 'triangle' or soundtype == 'sawtooth' or soundtype == 'trapezium') :
        #print('Sound type detected is ', soundtype, '\n')
        pass
    else : 
        soundtype = 'pluck' 
        #print('Sound type detected is invalid. Sound type set to pluck.\n')
 
    #Checking if bpm is from 60 - 180
    if (bpm >= 60 or bpm <= 180 ):
        #print('BPM detected is ', bpm, '\n')
        pass
    else : 
        bpm = 60
        #print('BPM detected is invalid. BPM set to 60.\n')

    duration = round(60/bpm,2)


    #Checking if starting note is from C1 to C6
    startnote=noteorigin[0]
    key=int(noteorigin[1])

    
    if (startnote in musickey and (key <= 6 and key >= 1 )) :
            #print(startnote)
            #print(key)
            pass
    else : 
        startnote = 'C'
        key = 4

    
    #code to check picture is list of lists

    data=np.array(picture)
    data_size=data.shape

    keynumbers = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])

    final_notes=[]
    if ( len(data_size) != 2):
        print('Pixel data provided does not have same number of elements per row')
    else :
        
        for row in range(data_size[0]):
            #print(data[row])
            data_out = np.multiply(data[row],keynumbers[0:data_size[1]])
            data_out_nozeroes = data_out[data_out != 0]
            #print(data_out_nozeroes)
            #print([musickey[i-1]+str(key+int(i/8)) for i in data_out_nozeroes])
            
            data_notes = [musickey[i-1]+str(key+int((i-1)/7)) for i in data_out_nozeroes]
            final_notes.append(data_notes)                
                
        #print('This are the final translated notes')
        #print(final_notes)

        
        
        for row in range(data_size[0]):
            if final_notes[row]:
                #print(final_notes[row])
                currnote=''
                for eachnote in final_notes[row]:
                    currnote = currnote+' '+soundtype+' ' + eachnote+' ' 
                #print(currnote)
                cmd = 'play -n synth ' + str(duration) + ' ' + currnote  + 'channels 1'
                #print(cmd)
                subprocess.run(cmd,shell=True)
            else:
                sleepcmd = 'sleep ' + str(duration)
                subprocess.run(sleepcmd,shell=True)

    


