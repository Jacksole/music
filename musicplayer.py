'''
Music Play App Created based off of a Youtube Playlist
Author: Le Aundre Jackson
Created 7/19/2018
Updated: 8/6/2018
'''
# Importing needed modules
import os
from random import shuffle
from tkinter.filedialog import askdirectory

import pygame
from mutagen.id3 import ID3
from tkinter import *

root = Tk()
root.minsize(300, 300)


listofsongs = []
realnames = []



        
v = StringVar()
songlabel = Label(root, textvariable=v, width=35)

index = 0


def directorychooser():
        '''Ask what folder the music files are stored'''
        directory = askdirectory()
        os.chdir(directory)

        for files in os.listdir(directory):
                if files.endswith(".mp3"):

                        realdir = os.path.realpath(files)
                        audio = ID3(realdir)
                        realnames.append(audio['TIT2'].text[0])

                        listofsongs.append(files)

        pygame.mixer.init()
        pygame.mixer.music.load(listofsongs[0])
        # pygame.mixer.music.play()


directorychooser()


def updatelabel():
        '''Updates Song label at the bottom of the app'''
        global index
        global songname
        v.set(realnames[index])
        # return songname


def nextsong(event):
        '''Plays next song'''
        global index
        index += 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        updatelabel()


def prevsong(event):
        '''Skips to previous song'''
        global index
        index -= 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        updatelabel()


def stopsong(event):
        '''Stops the song currently playing'''
        pygame.mixer.music.stop()
        v.set("")
        # return songname


##def shufflesong(event):
##        '''Randomizes the play list'''
##        global index
##        shuffle(listofsongs[index])
##        pygame.mixer.music.load(listofsongs[index])
##        pygame.mixer.music.play()
##        v.set("")
##        updatelabel()


def rewindsong(event):
        '''Restarts the song currently playing'''
        pygame.mixer.music.rewind()
        v.set("")


label = Label(root, text='Music Player')
label.pack()

scrollbar = Scrollbar(root, orient=VERTICAL)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack()

# listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0, items)

realnames.reverse()
# listofsongs.reverse()


rewindbutton = Button(root, text='Rewind Song')
rewindbutton.pack()

nextbutton = Button(root, text='Next Song')
nextbutton.pack()

previousbutton = Button(root, text='Previous Song')
previousbutton.pack()

stopbutton = Button(root, text='Stop Music')
stopbutton.pack()

# shufflebutton = Button(root, text='Shuffle')
# shufflebutton.pack()

nextbutton.bind("<Button-1>", nextsong)
previousbutton.bind("<Button-1>", prevsong)
stopbutton.bind("<Button-1>", stopsong)
# shufflebutton.bind("<Button-1>", shufflesong)
rewindbutton.bind("<Button-1>", rewindsong)


songlabel.pack()


root.mainloop()
