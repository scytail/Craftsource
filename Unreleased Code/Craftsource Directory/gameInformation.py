#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gameInformation.py
#  Class of windows that displays gameInformation
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

#parse standard XML
dataList = parse("data.xml")

#create biome lists
biomeAboutList = dataList.findall("biome/about")
biomeItemList = dataList.findall("biome/items")
biomeMobList = dataList.findall("biome/mobs")

#finds and parses all availible mod packs
path = 'mods/'
modfiles = os.listdir(path)
modlist = [] #list of all mods after parsing
for modxml in modfiles:
    modlist.append(parse(os.path.join(path,modxml)))

class GameInformation:
    def desertDisp(self):
        XMLLOCATION = 0
        window = Toplevel()
        window.title(string="Desert Biome")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Desert Biome",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---ABOUT---#
        subTitleLabel = Label(window,text="\nAbout",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,biomeAboutList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=2,column=0)

        #---MOBS/ITEMS---#
        subTitleLabel = Label(window,text="\nMobs and Items",font="TkSubHeadingFont")
        subTitleLabel.grid(row=3,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Items:\n")
        textbox1.insert(END,biomeItemList[XMLLOCATION].text)
        textbox1.insert(END,"\n\nMobs:\n")
        textbox1.insert(END,biomeMobList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=4,column=0)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0)

    def extremehillsDisp(self):
        XMLLOCATION = 1
        window = Toplevel()
        window.title(string="Extreme Hills Biome")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Extreme Hills Biome",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---ABOUT---#
        subTitleLabel = Label(window,text="\nAbout",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,biomeAboutList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=2,column=0)

        #---MOBS/ITEMS---#
        subTitleLabel = Label(window,text="\nMobs and Items",font="TkSubHeadingFont")
        subTitleLabel.grid(row=3,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Items:\n")
        textbox1.insert(END,biomeItemList[XMLLOCATION].text)
        textbox1.insert(END,"\n\nMobs:\n")
        textbox1.insert(END,biomeMobList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=4,column=0)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0)

    def forestDisp(self):
        XMLLOCATION = 2
        window = Toplevel()
        window.title(string="Forest Biome")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Forest Biome",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---ABOUT---#
        subTitleLabel = Label(window,text="\nAbout",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,biomeAboutList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=2,column=0)

        #---MOBS/ITEMS---#
        subTitleLabel = Label(window,text="\nMobs and Items",font="TkSubHeadingFont")
        subTitleLabel.grid(row=3,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Items:\n")
        textbox1.insert(END,biomeItemList[XMLLOCATION].text)
        textbox1.insert(END,"\n\nMobs:\n")
        textbox1.insert(END,biomeMobList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=4,column=0)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0)

    def jungleDisp(self):
        XMLLOCATION = 3
        window = Toplevel()
        window.title(string="Jungle Biome")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Jungle Biome",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---ABOUT---#
        subTitleLabel = Label(window,text="\nAbout",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,biomeAboutList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=2,column=0)

        #---MOBS/ITEMS---#
        subTitleLabel = Label(window,text="\nMobs and Items",font="TkSubHeadingFont")
        subTitleLabel.grid(row=3,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Items:\n")
        textbox1.insert(END,biomeItemList[XMLLOCATION].text)
        textbox1.insert(END,"\n\nMobs:\n")
        textbox1.insert(END,biomeMobList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=4,column=0)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0)

    def mushroomislandDisp(self):
        XMLLOCATION = 4
        window = Toplevel()
        window.title(string="Mushroom Island Biome")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Mushroom Island Biome",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---ABOUT---#
        subTitleLabel = Label(window,text="\nAbout",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,biomeAboutList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=2,column=0)

        #---MOBS/ITEMS---#
        subTitleLabel = Label(window,text="\nMobs and Items",font="TkSubHeadingFont")
        subTitleLabel.grid(row=3,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Items:\n")
        textbox1.insert(END,biomeItemList[XMLLOCATION].text)
        textbox1.insert(END,"\n\nMobs:\n")
        textbox1.insert(END,biomeMobList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=4,column=0)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0)

    def netherDisp(self): #aka Hell
        XMLLOCATION = 5
        window = Toplevel()
        window.title(string="Nether Biome")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Nether Biome",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---ABOUT---#
        subTitleLabel = Label(window,text="\nAbout",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,biomeAboutList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=2,column=0)

        #---MOBS/ITEMS---#
        subTitleLabel = Label(window,text="\nMobs and Items",font="TkSubHeadingFont")
        subTitleLabel.grid(row=3,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Items:\n")
        textbox1.insert(END,biomeItemList[XMLLOCATION].text)
        textbox1.insert(END,"\n\nMobs:\n")
        textbox1.insert(END,biomeMobList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=4,column=0)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0)

    def oceanDisp(self):
        XMLLOCATION = 6
        window = Toplevel()
        window.title(string="Ocean Biome")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Ocean Biome",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---ABOUT---#
        subTitleLabel = Label(window,text="\nAbout",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,biomeAboutList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=2,column=0)

        #---MOBS/ITEMS---#
        subTitleLabel = Label(window,text="\nMobs and Items",font="TkSubHeadingFont")
        subTitleLabel.grid(row=3,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Items:\n")
        textbox1.insert(END,biomeItemList[XMLLOCATION].text)
        textbox1.insert(END,"\n\nMobs:\n")
        textbox1.insert(END,biomeMobList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=4,column=0)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0)

    def plainsDisp(self):
        XMLLOCATION = 7
        window = Toplevel()
        window.title(string="Plains Biome")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Plains Biome",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---ABOUT---#
        subTitleLabel = Label(window,text="\nAbout",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,biomeAboutList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=2,column=0)

        #---MOBS/ITEMS---#
        subTitleLabel = Label(window,text="\nMobs and Items",font="TkSubHeadingFont")
        subTitleLabel.grid(row=3,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Items:\n")
        textbox1.insert(END,biomeItemList[XMLLOCATION].text)
        textbox1.insert(END,"\n\nMobs:\n")
        textbox1.insert(END,biomeMobList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=4,column=0)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0)

    def skyDisp(self): #aka The End
        XMLLOCATION = 8
        window = Toplevel()
        window.title(string="Sky Biome")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Sky Biome",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---ABOUT---#
        subTitleLabel = Label(window,text="\nAbout",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,biomeAboutList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=2,column=0)

        #---MOBS/ITEMS---#
        subTitleLabel = Label(window,text="\nMobs and Items",font="TkSubHeadingFont")
        subTitleLabel.grid(row=3,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Items:\n")
        textbox1.insert(END,biomeItemList[XMLLOCATION].text)
        textbox1.insert(END,"\n\nMobs:\n")
        textbox1.insert(END,biomeMobList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=4,column=0)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0)

    def swampDisp(self):
        XMLLOCATION = 9
        window = Toplevel()
        window.title(string="Swampland Biome")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Swampland Biome",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---ABOUT---#
        subTitleLabel = Label(window,text="\nAbout",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,biomeAboutList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=2,column=0)

        #---MOBS/ITEMS---#
        subTitleLabel = Label(window,text="\nMobs and Items",font="TkSubHeadingFont")
        subTitleLabel.grid(row=3,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Items:\n")
        textbox1.insert(END,biomeItemList[XMLLOCATION].text)
        textbox1.insert(END,"\n\nMobs:\n")
        textbox1.insert(END,biomeMobList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=4,column=0)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0)

    def taigaDisp(self):
        XMLLOCATION = 10
        window = Toplevel()
        window.title(string="Taiga Biome")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Taiga Biome",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---ABOUT---#
        subTitleLabel = Label(window,text="\nAbout",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,biomeAboutList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=2,column=0)

        #---MOBS/ITEMS---#
        subTitleLabel = Label(window,text="\nMobs and Items",font="TkSubHeadingFont")
        subTitleLabel.grid(row=3,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Items:\n")
        textbox1.insert(END,biomeItemList[XMLLOCATION].text)
        textbox1.insert(END,"\n\nMobs:\n")
        textbox1.insert(END,biomeMobList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=4,column=0)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0)

    def tundraDisp(self): #aka Ice Plains
        XMLLOCATION = 11
        window = Toplevel()
        window.title(string="Ice Plains Biome")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Ice Plains Biome",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---ABOUT---#
        subTitleLabel = Label(window,text="\nAbout",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,biomeAboutList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=2,column=0)

        #---MOBS/ITEMS---#
        subTitleLabel = Label(window,text="\nMobs and Items",font="TkSubHeadingFont")
        subTitleLabel.grid(row=3,column=0)

        frame1 = Frame(window)

        textbox1 = Text(frame1,bd=1,width=50,height=10,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Items:\n")
        textbox1.insert(END,biomeItemList[XMLLOCATION].text)
        textbox1.insert(END,"\n\nMobs:\n")
        textbox1.insert(END,biomeMobList[XMLLOCATION].text)
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=4,column=0)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0)

    def commandDisp(self):
        window = Toplevel()
        window.title(string="In-game Commands")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="In-game Commands",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0,columnspan=10)

        #---COMMANDS---#
        commandNameList = dataList.findall("command/name")
        commandDescriptionList = dataList.findall("command/description")
        row = -1
        column = 0
        numberCommands = len(commandNameList)
        for listLocation in range(0,numberCommands):
            row += 2
            if row > 13:
                row = 1
                column += 1

            commandLabel = Label(window,text="\n" + commandNameList[listLocation].text,font="TkFixedFont",wrap=300)
            commandLabel.grid(row=row,column=column)
            descriptionLabel = Label(window,text=commandDescriptionList[listLocation].text,wrap=300)
            descriptionLabel.grid(row=row + 1,column=column)

        #---MOD COMMANDS---#
        for mod in modlist:
            commandNameList = mod.findall("command/name")
            commandDescriptionList = mod.findall("command/description")
            numberCommands = len(commandNameList)
            for listLocation in range(0,numberCommands):
                row += 2
                if row > 13:
                    row = 1
                    column += 1

                commandLabel = Label(window,text="\n" + commandNameList[listLocation].text,font="TkFixedFont",wrap=300)
                commandLabel.grid(row=row,column=column)
                descriptionLabel = Label(window,text=commandDescriptionList[listLocation].text,wrap=300)
                descriptionLabel.grid(row=row + 1,column=column)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=21,column=0,columnspan=10)

    def gamemodeDisp(self):
        window = Toplevel()
        window.title(string="Minecraft Gamemodes")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')

        titleLabel = Label(window,text="Minecraft Gamemodes",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0,columnspan=10)

        #---COMMANDS---#
        nameList = dataList.findall("gamemode/name")
        descriptionList = dataList.findall("gamemode/description")
        row = -1
        column = 0

        for listLocation in range(0,4):
            row += 2
            if row > 13:
                row = 1
                column += 1

            nameLabel = Label(window,text="\n" + nameList[listLocation].text,font="TkFixedFont")
            nameLabel.grid(row=row,column=column)
            descriptionLabel = Label(window,text=descriptionList[listLocation].text,wrap=600)
            descriptionLabel.grid(row=row + 1,column=column)

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=21,column=0,columnspan=10)
    
    def horseDisp(self):
        window = Toplevel()
        window.title(string="Minecraft Gamemodes")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')
        Label(window,text="Horses",font="TkHeadingFont",relief="solid").grid(row=0,column=0,columnspan=1)
