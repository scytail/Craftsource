#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  helpInformation.py
#  Class of windows that displays information about the program
#
#  Copyright 2012 Suturesoft, all rights reserved.
#

#import GUI base (Tkinter) and styling (ttk)
try:
    from Tkinter import *
except:
    from tkinter import *

try:
    from ttk import *
except:
    from tkinter.ttk import *

try:    
    import tkMessageBox
except:
    from tkinter import messagebox as tkMessageBox

#import url reading library
from urllib import *

class HelpInformation:
    def aboutDisp(self):
        window = Toplevel()
        window.title(string="About")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Craftsource v. 1.4.6", font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        subTitleLabel = Label(window,text=" Built for Minecraft 1.4.6\n")
        subTitleLabel.grid(row=1,column=0,sticky="n")

        devTeam = Label(window,text="Development Team:\n    Suturesoft Craftsource Team")
        devTeam.grid(row=2,column=0,sticky="w")

        email = Label(window,text="Contact Information:\n    support@suturesoft.com\n")
        email.grid(row=3,column=0,sticky="w")

        sources = Label(window,text="Sources:\n    http://www.minecraftwiki.net\n    http://www.minecraftforums.net\n")
        sources.grid(row=4,column=0,sticky="w")

        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0,sticky="e")

    def helpDisp(self):
        window = Toplevel()
        window.title(string="Help")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')
        

        titleLabel = Label(window,text="Craftsource Help",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        bodyLabel = Label(window,text="Basic Usage:\nTo use Craftsource, simply type in the name or ID of an object found in Minecraft and click <Find Next>. It will then give you the name and ID of the object along with how to craft it in a crafting table and other useful data. Typing in a potion name under the 'Brewing' tab will give you information about that potion and how to brew it. Pressing <Find Next> without changing your input will find and display the next match for your search query. You can rotate thorugh all objects by clearing the search bar and clicking <Find Next>.\n\nMobs:\nTo find a mob's information, type 'mob: [mob/mob_id]' into the input area under the 'Crafting and Smelting' tab and click <Find Next>. You can also rotate thorugh all mobs by typing in 'mob:' and pressing <Find Next>.\n\nMods:\nBy default, any mod pack installed in the program will be searched as well. To rotate through the list of all items in your mod packs, type 'mod' and press <Find Next>.\n\nOther Information:\nTo quit Craftsource, close the window or go to File>Quit. Select 'about' in the help menu for program information. You can check for updates for the program by going to help>Check for Updates. Tutorials can be found in the Tutorials menu, and general information about Minecraft can be found under the Game Info menu. ",justify="left",wraplength=350)
        bodyLabel.grid(row=1,column=0)

        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=2,column=0,sticky="e")

    def updateCheck(self):
        update = False
        outputText = ""
        #Gets downloaded version
        versionSource = open('version.txt', 'r')
        versionContents = versionSource.read()

        try:
            #gets newest version
            updateSource = urlopen("http://www.suturesoft.com/Updates/craftsource.txt")
            updateContents = updateSource.read()
            failed = False
        except:
            failed = True

        #checks for url redirects
        for i in range(0,11):
            if updateContents[i] != versionContents[i]:
                failed = True

        #notifies on failiure
        if failed:
            outputText = "The server could not be accessed at this time.\nPlease check your internet connection and try again."
            outputTitle = "Error"
            
            #display info box with result
            tkMessageBox.showerror(outputTitle,outputText)

        #checks for updates
        elif not failed:
            for i in range(0,20):
                if updateContents[i] != versionContents[i]:
                    outputText = "There are data updates availible.\n"
                    outputTitle = "Updates Availible"
                    update = True
                    break
            for i in range(22,43):
                if updateContents[i] != versionContents[i]:
                    outputText = outputText + "There are version updates availible."
                    outputTitle = "Updates Availible"
                    update = True
                    break
            if not update:
                outputText = "You are running the most up to date version."
                outputTitle = "No Updates Availible"
            
            #display info box with result
            tkMessageBox.showinfo(outputTitle,outputText)

            #close server file
            updateSource.close()

        #closes version file
        versionSource.close()
