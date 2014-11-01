#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  Main executable file to call and run other windows
#
#  Copyright 2012 Suturesoft, all rights reserved.
#

#import xml parser
try:
    from xml.etree.cElementTree import parse
except:
    from xml.etree.ElementTree import parse

#import GUI base (Tkinter) and styling (ttk)
try:
    from Tkinter import *
except:
    from tkinter import *

try:
    from ttk import *
except:
    from tkinter.ttk import *

#import os for file path joining
import os

#import other python files
from MainWindow import *
from Tutorials import *
from gameInformation import *
from helpInformation import *

class Keybindings:
    def launchSearch(self,event):
        #find current tab
        currentTab = window.notebook.index("current")
        
        if currentTab == 0:
            window.searchItemXML()
        if currentTab == 1:
            window.searchPotionXML()
        
    def exitProgram(self,event): #keybinding quit program
        root.quit()

    def launchHelp(self,event): #keybinding helpDisp
        window.helpDisp()

#finds and parses all availible mod packs
path = 'mods/'
modfiles = os.listdir(path)
modlist = [] #list of all mods after parsing
for modxml in modfiles:
    modlist.append(parse(os.path.join(path,modxml)))

#parse standard XML
dataList = parse("data.xml")

root = Tk()#creates the window
root.title(string="Craftsource")#titles the window
root.iconbitmap('icon.ico')
root.resizable(False, False)

#initialize window classes
tutorials = Tutorials()
gameInfo = GameInformation()
helpInfo = HelpInformation()
window = MainWindow(root,gameInfo,helpInfo,tutorials)#calls the info on the window
key = Keybindings()

#---KEYBINDINGS---#
root.bind("<Return>", key.launchSearch)
root.bind("<Control-q>", key.exitProgram)
root.bind("<Alt-F4>", key.exitProgram)
root.bind("<Control-h>", key.launchHelp)
root.bind("<F12>", key.launchHelp)

root.mainloop()#displays the window
