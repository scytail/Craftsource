#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  MainWindow.py
#  Class that displays and runs functions in the main window of the program
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

#import other classes
from Tutorials import *
from gameInformation import *
from helpInformation import *

itemChoice = ""
oldItemChoice = ""
itemNameNumberCounter = -1
oldItemNameNumberCounter = -1
itemNoExist = 0

potionChoice = ""
oldPotionChoice = ""
potionNameNumberCounter = -1
oldPotionNameNumberCounter = -1
potionNoExist = 0

class MainWindow:
    #---BACKGROUND---#
    def __init__(self,master,gameInfo,helpInfo,tutorials):
        #---MENUBAR START---#
        self.menubar = Menu(master)#creates a menubar

        self.filemenu = Menu(self.menubar, tearoff=0)#creates the file menu button
        self.filemenu.add_command(label="Quit  <ctrl+q>", command=master.quit)#creates the Quit button in the file dropdown
        self.menubar.add_cascade(label="File", menu=self.filemenu)#creates the dropdown

        self.tutorialmenu = Menu(self.menubar, tearoff=0)#creates the tutorial menu button
        self.tutorialmenu.add_command (label="Adventuring",command=tutorials.adventuringDisp)#creates adventuring tutorial button
        self.tutorialmenu.add_command (label="Safe Homes",command=tutorials.safeHomeDisp)#creates safe homes tutorial button
        self.tutorialmenu.add_command (label="Shelter Designs",command=tutorials.shelterDisp)#creates shelter designs tutorial button
        self.tutorialmenu.add_separator()
        self.tutorialmenu.add_command (label="Nether Survival",command=tutorials.netherSurvivalDisp)#creates nether survival tutorial button
        self.tutorialmenu.add_command (label="Nomadic Experience",command=tutorials.nomadDisp)#creates nomadic experience tutorial button
        self.tutorialmenu.add_command (label="Superflat Survival",command=tutorials.superflatDisp)#creates superflat survival tutorial button
        self.menubar.add_cascade(label="Tutorials",menu=self.tutorialmenu)#creates tutorials dropdown

        self.gameInfoMenu = Menu(self.menubar,tearoff=0)
        self.biomemenu = Menu(self.gameInfoMenu,tearoff=0)
        self.biomemenu.add_command(label="Desert Biome",command=gameInfo.desertDisp)
        self.biomemenu.add_command(label="Extreme Hills Biome",command=gameInfo.extremehillsDisp)
        self.biomemenu.add_command(label="Forest Biome",command=gameInfo.forestDisp)
        self.biomemenu.add_command(label="Jungle Biome",command=gameInfo.jungleDisp)
        self.biomemenu.add_command(label="Mushroom Island Biome",command=gameInfo.mushroomislandDisp)
        self.biomemenu.add_command(label="Ocean Biome",command=gameInfo.oceanDisp)
        self.biomemenu.add_command(label="Plains Biome",command=gameInfo.plainsDisp)
        self.biomemenu.add_command(label="Sky Biome",command=gameInfo.skyDisp)
        self.biomemenu.add_command(label="Swampland Biome",command=gameInfo.swampDisp)
        self.biomemenu.add_command(label="Taiga Biome",command=gameInfo.taigaDisp)
        self.biomemenu.add_command(label="Tundra Biome",command=gameInfo.tundraDisp)
        self.gameInfoMenu.add_cascade(label="Biomes",menu=self.biomemenu)
        self.commandmenu = Menu(self.gameInfoMenu,tearoff=0)
        self.gameInfoMenu.add_command(label="In-Game Commands",command=gameInfo.commandDisp)
        self.gameInfoMenu.add_command(label="Gamemodes",command=gameInfo.gamemodeDisp)
        self.menubar.add_cascade(label="Game Info",menu=self.gameInfoMenu)

        self.helpmenu = Menu(self.menubar,tearoff=0)#creates the help menu button on the menubar
        self.helpmenu.add_command(label="Help",command=helpInfo.helpDisp)#creates the help button in the help dropdown
        self.helpmenu.add_command(label="Check for Updates",command=helpInfo.updateCheck)#creates the about button in the help dropdown
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="About",command=helpInfo.aboutDisp)#creates the updateChecker button in the help dropdown
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)#creates the helpmenu dropdown

        master.configure(menu=self.menubar)#displays the menubar
        #---MENUBAR END---#
        
        #TAB SUPPORT#
        self.notebook = Notebook(master)
        self.notebook.grid(row=0,column=0)
        
        #---ITEM SEARCH---#
        self.craftingFrame = Frame(self.notebook)
        self.craftingFrame.pack()
        
        self.searchBar = Entry(self.craftingFrame)#creates a searchbar with the window as its parent
        self.searchBar.config(width="30")
        self.searchBar.focus_set()#places the focus at the searchbar so that the user doesn't have to click the textbox to type
        self.searchBar.grid(row=0, column=0)#packs it to display

        self.searchButton = Button(self.craftingFrame,text="Find Next",command=self.searchItemXML)#creates the search button
        self.searchButton.grid(row=0,column=1)#displays the searchbutton in the correct area
        
        self.craftingBox = Canvas(self.craftingFrame,width=300,height=380)
        self.craftingBox.grid(row=1,column=0,columnspan=2,sticky="w")

        self.craftingBox.create_text(5,15,text="Name:", anchor="nw")

        self.craftingBox.create_text(5,30,text="ID:",anchor="nw")

        self.craftingBox.create_text(5,60,text=" | |",anchor="nw",font="TkFixedFont")
        self.craftingBox.create_text(5,75,text=" | |",anchor="nw",font="TkFixedFont")
        self.craftingBox.create_text(5,90,text=" | |",anchor="nw",font="TkFixedFont")

        self.craftingBox.create_text(5,120,text="key:",anchor="nw",width=300)

        self.craftingBox.create_text(5,180,text="Smelt:",anchor="nw",width=300)
        self.craftingBox.create_text(5,195,text="Tool:",anchor="nw",width=300)
        self.craftingBox.create_text(5,210,text="Durability:",anchor="nw",width=300)
        self.craftingBox.create_text(5,225,text="Obtainability:",anchor="nw",width=300)
        self.craftingBox.create_text(5,240,text="Location:",anchor="nw",width=300)
        self.craftingBox.create_text(5,255,text="Stack:",anchor="nw",width=300)
        self.craftingBox.create_text(5,270,text="Physics:",anchor="nw",width=300)
        self.craftingBox.create_text(5,285,text="Other Info:",anchor="nw",width=300)
        
        self.notebook.add(self.craftingFrame, text='Crafting & Smelting')
        
        #---POTION SEARCH---#
        self.potionFrame = Frame(self.notebook)
        self.potionFrame.pack()
        
        self.potionSearchBar = Entry(self.potionFrame)#creates a searchbar with the window as its parent
        self.potionSearchBar.config(width="30")
        self.potionSearchBar.focus_set()#places the focus at the searchbar so that the user doesn't have to click the textbox to type
        self.potionSearchBar.grid(row=0, column=0)#packs it to display

        self.potionSearchButton = Button(self.potionFrame,text="Find Next",command=self.searchPotionXML)#creates the search button
        self.potionSearchButton.grid(row=0,column=1)#displays the searchbutton in the correct area
        
        self.potionBox = Canvas(self.potionFrame,width=300,height=380)
        self.potionBox.grid(row=1,column=0,columnspan=2,sticky="w")

        self.potionBox.create_text(5,15,text="Name:", anchor="nw")

        self.potionBox.create_text(5,30,text="ID:",anchor="nw")

        self.potionBox.create_text(5,60,text=" ",anchor="nw",font="TkFixedFont")
        self.potionBox.create_text(5,75,text="     +",anchor="nw",font="TkFixedFont")
        self.potionBox.create_text(5,90,text=" ",anchor="nw",font="TkFixedFont")

        self.potionBox.create_text(5,120,text="key:",anchor="nw",width=300)

        self.potionBox.create_text(5,180,text="Duration:",anchor="nw",width=300)
        self.potionBox.create_text(5,195,text="Add Redstone:",anchor="nw",width=300)
        self.potionBox.create_text(5,210,text="Add Glowstone:",anchor="nw",width=300)
        self.potionBox.create_text(5,225,text="Add Fermented Spider Eye:",anchor="nw",width=300)
        self.potionBox.create_text(5,240,text="Obtainability:",anchor="nw",width=300)
        self.potionBox.create_text(5,255,text="Other Info:",anchor="nw",width=300)
        
        self.potionBox.create_text(5,315,text=">Adding Redstone increases duration\n>Adding Glowstone Dust increases potency\n>Adding Fermented Spider Eye corrupts effect\n>Adding Gunpowder makes a splash potion",anchor="nw",width=300)
        
        self.notebook.add(self.potionFrame, text='Brewing')
    
    #---SEARCH ITEMS---#
    def searchItemXML(self):
        global itemChoice
        global oldItemChoice
        global itemNameNumberCounter
        global oldItemNameNumberCounter
        global itemNoExist
        
        oldItemChoice = itemChoice
        
        itemChoice = self.searchBar.get().lower() #gets the text in the searchbar and converts to lowercase
        
        found = 0 #reset found var
        itemNameNumberCounter = -1 #reset counter

        #-----------------------code to check for matching objects-----------------------#
        nameList = dataList.findall("item/name") #find all objects in <name> brackets
        idList = dataList.findall("item/id") #find all objects in <id> brackets
        altList = dataList.findall("item/alt") #find all objects in <alt> brackets

        #--searches namelist and idlist--#
        for i in nameList:
            itemNameNumberCounter += 1#move to next item
            nameText = i.text #convert object to text for comparison
            idText = idList[itemNameNumberCounter].text #convert object to text for comparison

            if itemChoice == nameText or itemChoice == idText:
                found = 1#object was found; stop searching
                itemNoExist = 0#object exists (used in search looping)

                self.getItemInfo(dataList,itemNameNumberCounter)

                break #end the loop

        #code for if item wasn't found in namelist or idList
        if found == 0:
            if itemChoice == oldItemChoice:
                itemNameNumberCounter = oldItemNameNumberCounter
            else:
                itemNameNumberCounter = -1#reset counter
                oldItemNameNumberCounter = -1
                itemNoExist = 0

            #--searches altlist--#
            for i in range((oldItemNameNumberCounter + 1),len(altList)):
                itemNameNumberCounter += 1
                altText = altList[i]
                altText = altText.text #convert object to text for comparison

                if itemChoice in altText or itemChoice == "":
                    found = 1
                    itemNoExist = 0
                    
                    oldItemNameNumberCounter = itemNameNumberCounter
                    self.getItemInfo(dataList,itemNameNumberCounter)

                    break #end the loop
        #check the installed mods for matches
        if found == 0:
            #run through installed mod xmls
            for mod in modlist:
                nameList = mod.findall("item/name") #find all objects in <name> brackets
                idList = mod.findall("item/id") #find all objects in <id> brackets
                altList = mod.findall("item/alt") #find all objects in <alt> brackets
                itemNameNumberCounter = -1
                #--searches namelist and idlist--#
                for i in nameList:
                    itemNameNumberCounter += 1#move to next item
                    nameText = i.text #convert object to text for comparison
                    idText = idList[itemNameNumberCounter].text #convert object to text for comparison
                    if itemChoice == nameText or itemChoice == idText:
                        found = 1
                        itemNoExist = 0
                        
                        self.getItemInfo(mod,itemNameNumberCounter)

                        break #end the loop

                #code for if item wasn't found in namelist or idList
                if found == 0:
                    if itemChoice == oldItemChoice:
                        itemNameNumberCounter = oldItemNameNumberCounter
                    else:
                        itemNameNumberCounter = -1#reset counter
                        oldItemNameNumberCounter = -1
                        itemNoExist = 0

                    #--searches altlist--#
                    for i in range((oldItemNameNumberCounter + 1),len(altList)):
                        itemNameNumberCounter += 1
                        altText = altList[i]
                        altText = altText.text #convert object to text for comparison

                        if itemChoice in altText or itemChoice == "mod":
                            found = 1
                            itemNoExist = 0
                            
                            oldItemNameNumberCounter = itemNameNumberCounter
                            self.getItemInfo(mod,itemNameNumberCounter)

                            break #end the loop
                            
        #code to give if the program reached the end of the data list
        if found == 0:
            name = ""
            idnum = "\n\n'" + itemChoice + "' was not found. Search again to\ncontinue looking from the beginning."
            craftTop = ""
            craftMid = ""
            craftLow = ""
            craftKey = ""
            itemSmelt = ""
            itemTool = ""
            itemDurability = ""
            itemObtainability = ""
            itemLocation = ""
            itemStack = ""
            itemPhysics = ""
            itemOtherInfo = ""
            oldItemNameNumberCounter = -1
            itemNoExist += 1
            
            self.updateItemWindow(name,idnum,craftTop,craftMid,craftLow,craftKey,itemSmelt,itemTool,itemDurability,itemObtainability,itemLocation,itemStack,itemPhysics,itemOtherInfo)
            
        #code to give if the object wasn't found in namelist, idlist, or altlist
        if itemNoExist > 1:
            name = ""
            idnum = "\n\n'" + itemChoice + "' was not found. Please enter\na new query and try again."
            craftTop = ""
            craftMid = ""
            craftLow = ""
            craftKey = ""
            itemSmelt = ""
            itemTool = ""
            itemDurability = ""
            itemObtainability = ""
            itemLocation = ""
            itemStack = ""
            itemPhysics = ""
            itemOtherInfo = ""
        
            self.updateItemWindow(name,idnum,craftTop,craftMid,craftLow,craftKey,itemSmelt,itemTool,itemDurability,itemObtainability,itemLocation,itemStack,itemPhysics,itemOtherInfo)#runs the update function to update the window with the given information
            
    def getItemInfo(self,xmlSource,listLocation):

        #find the name of specified object
        name = xmlSource.findall("item/name") #gets a list of all the names (one for each name)
        name = name[listLocation] #points to the specific object in the list we want (same location as name in list because one each)
        name = name.text #converts xml to text for reading

        #find the ID of specified object
        idnum = xmlSource.findall("item/id") #gets a list of all the IDs (one for each name)
        idnum = idnum[listLocation] #points to the specific object in the list we want (same location as name in list because one each)
        idnum = idnum.text #converts xml to text for reading

        #find the top row crafting of specified object
        craftTop = xmlSource.findall("item/craftT") #gets a list of all the top rows (one for each name)
        craftTop = craftTop[listLocation] #points to the specific object in the list we want (same location as name in list because one each)
        craftTop = craftTop.text #converts xml to text for reading

        #find the middle row crafting of specified object
        craftMid = xmlSource.findall("item/craftM") #gets a list of all the mid rows (one for each name)
        craftMid = craftMid[listLocation] #points to the specific object in the list we want (same location as name in list because one each)
        craftMid = craftMid.text #converts xml to text for reading

        #find the bottom row crafting of specified object
        craftLow = xmlSource.findall("item/craftB") #gets a list of all the low rows (one for each name)
        craftLow = craftLow[listLocation] #points to the specific object in the list we want (same location as name in list because one each)
        craftLow = craftLow.text #converts xml to text for reading

        #find the key of specified object
        craftKey = xmlSource.findall("item/key") #gets a list of all the keys (one for each name)
        craftKey = craftKey[listLocation] #points to the specific object in the list we want (same location as name in list because one each)
        craftKey = craftKey.text #converts xml to text for reading

        #find the smelting of specified object
        itemSmelt = xmlSource.findall("item/smelt")
        itemSmelt = itemSmelt[listLocation]
        itemSmelt = itemSmelt.text

        #find the tool of specified object
        itemTool = xmlSource.findall("item/tool")
        itemTool = itemTool[listLocation]
        itemTool = itemTool.text

        #find the durability of specified object
        itemDurability = xmlSource.findall("item/durability")
        itemDurability = itemDurability[listLocation]
        itemDurability = itemDurability.text

        #find the durability of specified object
        itemObtainability = xmlSource.findall("item/obtainability")
        itemObtainability = itemObtainability[listLocation]
        itemObtainability = itemObtainability.text

        #find the in-game location of specified object
        itemLocation = xmlSource.findall("item/location")
        itemLocation = itemLocation[listLocation]
        itemLocation = itemLocation.text

        #find the stack amount of specified object
        itemStack = xmlSource.findall("item/stack")
        itemStack = itemStack[listLocation]
        itemStack = itemStack.text

        #find the physics of specified object
        itemPhysics = xmlSource.findall("item/physics")
        itemPhysics = itemPhysics[listLocation]
        itemPhysics = itemPhysics.text

        #find other info on specified object
        itemOtherInfo = xmlSource.findall("item/other")
        itemOtherInfo = itemOtherInfo[listLocation]
        itemOtherInfo = itemOtherInfo.text

        self.updateItemWindow(name,idnum,craftTop,craftMid,craftLow,craftKey,itemSmelt,itemTool,itemDurability,itemObtainability,itemLocation,itemStack,itemPhysics,itemOtherInfo)#runs the update function to update the window with the given information

    def updateItemWindow(self,name,idnum,craftTop,craftMid,craftLow,craftKey,itemSmelt,itemTool,itemDurability,itemObtainability,itemLocation,itemStack,itemPhysics,itemOtherInfo):
        self.craftingBox = Canvas(self.craftingFrame,width=300,height=380)
        self.craftingBox.grid(row=1, column=0, columnspan=2,sticky="w")

        self.craftingBox.create_text(5,15,text="Name: " + name,anchor="nw")

        self.craftingBox.create_text(5,30,text="ID: " + idnum,anchor="nw")

        self.craftingBox.create_text(5,60,text=craftTop,anchor="nw",font="TkFixedFont")
        self.craftingBox.create_text(5,75,text=craftMid,anchor="nw",font="TkFixedFont")
        self.craftingBox.create_text(5,90,text=craftLow,anchor="nw",font="TkFixedFont")

        self.craftingBox.create_text(5,120,text="key: " + craftKey,anchor="nw",width=300)

        self.craftingBox.create_text(5,180,text="Smelt: " + itemSmelt,anchor="nw",width=300)
        self.craftingBox.create_text(5,195,text="Tool: " + itemTool,anchor="nw",width=300)
        self.craftingBox.create_text(5,210,text="Durability: " + itemDurability,anchor="nw",width=300)
        self.craftingBox.create_text(5,225,text="Obtainability: " + itemObtainability,anchor="nw",width=300)
        self.craftingBox.create_text(5,240,text="Location: " + itemLocation,anchor="nw",width=300)
        self.craftingBox.create_text(5,255,text="Stack: " + itemStack,anchor="nw",width=300)
        self.craftingBox.create_text(5,270,text="Physics: " + itemPhysics,anchor="nw",width=300)
        self.craftingBox.create_text(5,285,text="Other: " + itemOtherInfo,anchor="nw",width=300)
    
    #---SEARCH POTIONS---#
    def searchPotionXML(self):
        global potionChoice
        global oldPotionChoice
        global potionNameNumberCounter
        global oldPotionNameNumberCounter
        global potionNoExist
        
        oldPotionChoice = potionChoice
        
        potionChoice = self.potionSearchBar.get().lower() #gets the text in the searchbar and converts to lowercase

        found = 0 #reset found var
        potionNameNumberCounter = -1 #reset counter

        #-----------------------code to check for matching objects-----------------------#
        nameList = dataList.findall("potion/name") #find all objects in <name> brackets
        idList = dataList.findall("potion/id") #find all objects in <id> brackets
        altList = dataList.findall("potion/alt") #find all objects in <alt> brackets

        #--searches namelist and idlist--#
        for i in nameList:
            potionNameNumberCounter += 1#move to next item
            nameText = i.text #convert object to text for comparison
            idText = idList[potionNameNumberCounter].text #convert object to text for comparison
            if potionChoice == nameText or potionChoice == idText:
                found = 1
                potionNoExist = 0
                
                self.getPotionInfo(dataList,potionNameNumberCounter)

                break #end the loop

        #code for if item wasn't found in namelist or idList
        if found == 0:
            if potionChoice == oldPotionChoice:
                potionNameNumberCounter = oldPotionNameNumberCounter
            else:
                potionNameNumberCounter = -1#reset counter
                oldPotionNameNumberCounter = -1
                potionNoExist = 0

            #--searches altlist--#
            for i in range((oldPotionNameNumberCounter + 1),len(altList)):
                potionNameNumberCounter += 1
                altText = altList[i]
                altText = altText.text #convert object to text for comparison

                if potionChoice in altText or potionChoice == "":
                    found = 1
                    potionNoExist = 0
                    
                    oldPotionNameNumberCounter = potionNameNumberCounter
                    self.getPotionInfo(dataList,potionNameNumberCounter)

                    break #end the loop

        #check the installed mods for matches
        if found == 0:
            #run through installed mod xmls
            for mod in modlist:
                nameList = mod.findall("potion/name") #find all objects in <name> brackets
                idList = mod.findall("potion/id") #find all objects in <id> brackets
                altList = mod.findall("potion/alt") #find all objects in <alt> brackets
                potionNameNumberCounter = -1
                #--searches namelist and idlist--#
                for i in nameList:
                    potionNameNumberCounter += 1#move to next item
                    nameText = i.text #convert object to text for comparison
                    idText = idList[potionNameNumberCounter].text #convert object to text for comparison
                    if potionChoice == nameText or potionChoice == idText:
                        found = 1
                        potionNoExist = 0
                        
                        self.getPotionInfo(mod,potionNameNumberCounter)

                        break #end the loop

                #code for if item wasn't found in namelist or idList
                if found == 0:
                    if potionChoice == oldPotionChoice:
                        potionNameNumberCounter = oldPotionNameNumberCounter
                    else:
                        potionNameNumberCounter = -1#reset counter
                        oldPotionNameNumberCounter = -1
                        potionNoExist = 0

                    #--searches altlist--#
                    for i in range((oldPotionNameNumberCounter + 1),len(altList)):
                        potionNameNumberCounter += 1
                        altText = altList[i]
                        altText = altText.text #convert object to text for comparison

                        if potionChoice in altText or potionChoice == "mod":
                            found = 1
                            potionNoExist = 0
                            
                            oldPotionNameNumberCounter = potionNameNumberCounter
                            self.getPotionInfo(mod,potionNameNumberCounter)

                            break #end the loop

        #code to give if the program reached the end of the data list
        if found == 0:
            name = ""
            idnum = "\n\n'" + potionChoice + "' was not found. Search again to\ncontinue looking from the beginning."
            craftTop = ""
            craftMid = ""
            craftLow = ""
            craftKey = ""
            potionDuration = ""
            potionRedstone = ""
            potionGlowstone = ""
            potionFermEye = ""
            potionObtainability = ""
            potionOtherInfo = ""
            oldPotionNameNumberCounter = -1
            potionNoExist += 1
            
            self.updatePotionWindow(name,idnum,craftTop,craftMid,craftLow,craftKey,potionDuration,potionRedstone,potionGlowstone,potionFermEye,potionObtainability,potionOtherInfo)
    
        #code to give if the object wasn't found in namelist, idlist, or altlist
        if potionNoExist > 1:
            name = ""
            idnum = "\n\n'" + potionChoice + "' was not found. Please enter\na new query and try again."
            craftTop = ""
            craftMid = ""
            craftLow = ""
            craftKey = ""
            potionDuration = ""
            potionRedstone = ""
            potionGlowstone = ""
            potionFermEye = ""
            potionObtainability = ""
            potionOtherInfo = ""

            self.updatePotionWindow(name,idnum,craftTop,craftMid,craftLow,craftKey,potionDuration,potionRedstone,potionGlowstone,potionFermEye,potionObtainability,potionOtherInfo)
    
    def getPotionInfo(self,xmlSource,listLocation):
        #find the name of specified object
        name = xmlSource.findall("potion/name") #gets a list of all the names (one for each name)
        name = name[listLocation] #points to the specific object in the list we want (same location as name in list because one each)
        name = name.text #converts xml to text for reading

        #find the ID of specified object
        idnum = xmlSource.findall("potion/id") #gets a list of all the IDs (one for each name)
        idnum = idnum[listLocation] #points to the specific object in the list we want (same location as name in list because one each)
        idnum = idnum.text #converts xml to text for reading

        #find the top row crafting of specified object
        craftTop = xmlSource.findall("potion/craftT") #gets a list of all the top rows (one for each name)
        craftTop = craftTop[listLocation] #points to the specific object in the list we want (same location as name in list because one each)
        craftTop = craftTop.text #converts xml to text for reading

        #find the middle row crafting of specified object
        craftMid = xmlSource.findall("potion/craftM") #gets a list of all the mid rows (one for each name)
        craftMid = craftMid[listLocation] #points to the specific object in the list we want (same location as name in list because one each)
        craftMid = craftMid.text #converts xml to text for reading

        #find the bottom row crafting of specified object
        craftLow = xmlSource.findall("potion/craftB") #gets a list of all the low rows (one for each name)
        craftLow = craftLow[listLocation] #points to the specific object in the list we want (same location as name in list because one each)
        craftLow = craftLow.text #converts xml to text for reading

        #find the key of specified object
        craftKey = xmlSource.findall("potion/key") #gets a list of all the keys (one for each name)
        craftKey = craftKey[listLocation] #points to the specific object in the list we want (same location as name in list because one each)
        craftKey = craftKey.text #converts xml to text for reading

        #find the durability of specified object
        potionDuration = xmlSource.findall("potion/duration")
        potionDuration = potionDuration[listLocation]
        potionDuration = potionDuration.text

        #find the durability of specified object
        potionRedstone = xmlSource.findall("potion/redstone")
        potionRedstone = potionRedstone[listLocation]
        potionRedstone = potionRedstone.text

        #find the in-game location of specified object
        potionGlowstone = xmlSource.findall("potion/glowstone")
        potionGlowstone = potionGlowstone[listLocation]
        potionGlowstone = potionGlowstone.text

        #find the stack amount of specified object
        potionFermEye = xmlSource.findall("potion/fermspider")
        potionFermEye = potionFermEye[listLocation]
        potionFermEye = potionFermEye.text

        #find the physics of specified object
        potionObtainability = xmlSource.findall("potion/obtainability")
        potionObtainability = potionObtainability[listLocation]
        potionObtainability = potionObtainability.text

        #find other info on specified object
        potionOtherInfo = xmlSource.findall("potion/other")
        potionOtherInfo = potionOtherInfo[listLocation]
        potionOtherInfo = potionOtherInfo.text

        self.updatePotionWindow(name,idnum,craftTop,craftMid,craftLow,craftKey,potionDuration,potionRedstone,potionGlowstone,potionFermEye,potionObtainability,potionOtherInfo)
    
    def updatePotionWindow(self,name,idnum,craftTop,craftMid,craftLow,craftKey,potionDuration,potionRedstone,potionGlowstone,potionFermEye,potionObtainability,potionOtherInfo):
        self.potionBox = Canvas(self.potionFrame,width=300,height=380)
        self.potionBox.grid(row=1, column=0, columnspan=2,sticky="w")

        self.potionBox.create_text(5,15,text="Name: " + name,anchor="nw")

        self.potionBox.create_text(5,30,text="ID: " + idnum,anchor="nw")

        self.potionBox.create_text(5,60,text=craftTop,anchor="nw",font="TkFixedFont")
        self.potionBox.create_text(5,75,text=craftMid,anchor="nw",font="TkFixedFont")
        self.potionBox.create_text(5,90,text=craftLow,anchor="nw",font="TkFixedFont")

        self.potionBox.create_text(5,120,text="key: " + craftKey,anchor="nw",width=300)

        self.potionBox.create_text(5,180,text="Duration: " + potionDuration,anchor="nw",width=300)
        self.potionBox.create_text(5,195,text="Add Redstone: " + potionRedstone,anchor="nw",width=300)
        self.potionBox.create_text(5,210,text="Add Glowstone: " + potionGlowstone,anchor="nw",width=300)
        self.potionBox.create_text(5,225,text="Add Fermented Spider Eye: " + potionFermEye,anchor="nw",width=300)
        self.potionBox.create_text(5,240,text="Obtainability: " + potionObtainability,anchor="nw",width=300)
        self.potionBox.create_text(5,255,text="Other Info: " + potionOtherInfo,anchor="nw",width=300)
        
        self.potionBox.create_text(5,315,text=">Adding Redstone increases duration\n>Adding Glowstone Dust increases potency\n>Adding Fermented Spider Eye corrupts effect\n>Adding Gunpowder makes a splash potion",anchor="nw",width=300)
