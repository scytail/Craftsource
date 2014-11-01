#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2012 Ben Schwabe <bspymaster@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#

#import xml functions
import xml.etree.ElementTree as ET

#import tk
import Tkinter

#import image classes
#from PIL import Image

dataList = ET.parse('data.xml') #parse the XML document

#define vars
name = ""
idnum = ""
craftTop = " | | "
craftMid = " | | "
craftLow = " | | "
craftKey = ""
itemSmelt = ""
itemTool = ""
itemLocation = ""
itemStack = ""
itemPhysics = ""
itemOtherInfo = ""


class GUI:
	def __init__(self,master,name,idnum,craftTop,craftMid,craftLow,craftKey,itemSmelt,itemTool,itemLocation,itemStack,itemPhysics,itemOtherInfo):
		
		self.menubar = Tkinter.Menu(root)#creates a menubar

		self.filemenu = Tkinter.Menu(self.menubar, tearoff=0)#creates the file menu button
		self.filemenu.add_command(label="Quit", command=root.quit)#creates the Quit button in the file dropdown
		self.menubar.add_cascade(label="File", menu=self.filemenu)#creates the dropdown
		
		self.helpmenu = Tkinter.Menu(self.menubar,tearoff=0)#creates the help menu button on the menubar
		self.helpmenu.add_command(label="Help",command=self.helpDisp)#creates the about button in the help dropdown
		self.helpmenu.add_separator()
		self.helpmenu.add_command(label="About",command=self.aboutDisp)#creates the about button in the help dropdown
		self.menubar.add_cascade(label="Help", menu=self.helpmenu)#creates the dropdown
		
		root.configure(menu=self.menubar)#displays the menubar

		self.searchBar = Tkinter.Entry(root)#creates a searchbar with the window as its parent
		self.searchBar.grid(row=0, column=0)#packs it to display
		
		self.searchButton = Tkinter.Button(root,text="Search",command=self.searchXML)
		self.searchButton.grid(row=0,column=1)
		
		self.craftingBox = Tkinter.Canvas(root,width=300,height=350)
		
		self.craftingBox.create_text(5,15,text="name: " + name, anchor="nw")
		
		self.craftingBox.create_text(5,30,text="id: " + idnum,anchor="nw")
		
		self.craftingBox.create_text(5,60,text=craftTop,anchor="nw",font="TkFixedFont")
		self.craftingBox.create_text(5,75,text=craftMid,anchor="nw",font="TkFixedFont")
		self.craftingBox.create_text(5,90,text=craftLow,anchor="nw",font="TkFixedFont")
		
		self.craftingBox.create_text(5,120,text="key: " + craftKey,anchor="nw",width=300)
		
		self.craftingBox.create_text(5,180,text="Smelt: " + itemSmelt,anchor="nw",width=300)
		self.craftingBox.create_text(5,195,text="Tool: " + itemTool,anchor="nw",width=300)
		self.craftingBox.create_text(5,210,text="Location: " + itemLocation,anchor="nw",width=300)
		self.craftingBox.create_text(5,225,text="Stack: " + itemStack,anchor="nw",width=300)
		self.craftingBox.create_text(5,240,text="Physics: " + itemPhysics,anchor="nw",width=300)
		self.craftingBox.create_text(5,255,text="Other Info: " + itemOtherInfo,anchor="nw",width=300)
		
		self.craftingBox.grid(row=1,column=0,columnspan=2,sticky="w")
		
		
	def searchXML(self):
		choice = self.searchBar.get() #gets the text in the searchbar
		found = 0 #reset found var
		nameNumberCounter = -1
		idNumberCounter = -1
		altNumberCounter = -1
		"""
		#must display image of data values (doesn't work)
		if choice == "data values" or choice == "data value":
			
			found = 1
			
			dataValuesWindow = Tkinter.Tk()
			dataValuesWindow.title(string="Data Values")
			
			pictureDisp = Tkinter.Canvas(dataValuesWindow, height=400, width=300)
			
			photo = Tkinter.PhotoImage('DataValues1.3.0.gif')
			pictureDisp.create_image(100,100,image=photo)
			
			canvas.grid(row=0,column=0)
			
			dataValuesCloseButton = Tkinter.Button(aboutWindow,text="Close",command=dataValuesWindow.destroy)
			dataValuesCloseButton.grid(row=1,column=0,sticky="e")
			
			name = ""
			idnum = ""
			craftTop = " | | "
			craftMid = " | | "
			craftLow = " | | "
			craftKey = ""
			itemSmelt = ""
			itemTool = ""
			itemLocation = ""
			itemStack = ""
			itemPhysics = ""
			itemOtherInfo = ""
			
		elif choice == "251" or choice == "dye":
			#list dye choices here
			
		elif choice == "list" or choice == "all":
			found = 1
			print("----------------------------------------")
			print("All objects:\n")
			nameList = dataList.findall("item/name")
			idList = dataList.findall("item/id")
			for i in nameList:
				idNumberCounter = idNumberCounter + 1
				name = i.text
				idNum = idList[idNumberCounter]
				idNum = idNum.text
				print(idNum + ": " + name)
			print("----------------------------------------")
			name = ""
			idnum = ""
			craftTop = " | | "
			craftMid = " | | "
			craftLow = " | | "
			craftKey = ""
		"""
		
		#-----------------------code to check names-----------------------
		nameNumberCounter = -1 #reset var
		nameList = dataList.findall("item/name") #find all objects in <name> brackets
		
		for i in nameList:
			nameNumberCounter = nameNumberCounter + 1
			nameText = i.text #convert object to text for comparison
			if nameText == choice:
				found = 1
				
				#find the name of specified object
				name = dataList.findall("item/name") #gets a list of all the IDs (one for each name)
				name = name[nameNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
				name = name.text #converts xml to text for reading
	
				#find the ID of specified object
				idnum = dataList.findall("item/id") #gets a list of all the IDs (one for each name)
				idnum = idnum[nameNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
				idnum = idnum.text #converts xml to text for reading
	
				#find the top row crafting of specified object
				craftTop = dataList.findall("item/craftT") #gets a list of all the top rows (one for each name)
				craftTop = craftTop[nameNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
				craftTop = craftTop.text #converts xml to text for reading
	
				#find the middle row crafting of specified object
				craftMid = dataList.findall("item/craftM") #gets a list of all the mid rows (one for each name)
				craftMid = craftMid[nameNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
				craftMid = craftMid.text #converts xml to text for reading
	
				#find the bottom row crafting of specified object
				craftLow = dataList.findall("item/craftB") #gets a list of all the low rows (one for each name)
				craftLow = craftLow[nameNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
				craftLow = craftLow.text #converts xml to text for reading
	
				#find the key of specified object
				craftKey = dataList.findall("item/key") #gets a list of all the keys (one for each name)
				craftKey = craftKey[nameNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
				craftKey = craftKey.text #converts xml to text for reading
				
				#find the smelting of specified object
				itemSmelt = dataList.findall("item/smelt")
				itemSmelt = itemSmelt[nameNumberCounter]
				itemSmelt = itemSmelt.text
				
				#find the tool of specified object
				itemTool = dataList.findall("item/tool")
				itemTool = itemTool[nameNumberCounter]
				itemTool = itemTool.text
				
				#find the in-game location of specified object
				itemLocation = dataList.findall("item/location")
				itemLocation = itemLocation[nameNumberCounter]
				itemLocation = itemLocation.text
				
				#find the stack amount of specified object
				itemStack = dataList.findall("item/stack")
				itemStack = itemStack[nameNumberCounter]
				itemStack = itemStack.text
				
				#find the physics of specified object
				itemPhysics = dataList.findall("item/physics")
				itemPhysics = itemPhysics[nameNumberCounter]
				itemPhysics = itemPhysics.text
				
				#find other info on specified object
				itemOtherInfo = dataList.findall("item/other")
				itemOtherInfo = itemOtherInfo[nameNumberCounter]
				itemOtherInfo = itemOtherInfo.text
	
				break #end the loop
	
		#-----------------------code to check alternate names-----------------------
		altNumberCounter = -1 #reset var
		altList = dataList.findall("item/alt") #find all objects in <alt> brackets
		
		for i in altList:
			altNumberCounter = altNumberCounter + 1
			altText = i.text #convert object to text for comparison
	
			if altText == choice:
				found = 1
	
				#find the name of specified object
				name = dataList.findall("item/name") #gets a list of all the IDs (one for each name)
				name = name[altNumberCounter] #points to the specific object in the list we want (1/2 location as name in list because two each)
				name = name.text #converts xml to text for reading
	
				#find the ID of specified object
				idnum = dataList.findall("item/id") #gets a list of all the IDs (one for each name)
				idnum = idnum[altNumberCounter] #points to the specific object in the list we want (1/2 location as name in list because two each)
				idnum = idnum.text #converts xml to text for reading
	
				#find the top row crafting of specified object
				craftTop = dataList.findall("item/craftT") #gets a list of all the top rows (one for each name)
				craftTop = craftTop[altNumberCounter] #points to the specific object in the list we want (1/2 location as name in list because two each)
				craftTop = craftTop.text #converts xml to text for reading
	
				#find the middle row crafting of specified object
				craftMid = dataList.findall("item/craftM") #gets a list of all the mid rows (one for each name)
				craftMid = craftMid[altNumberCounter] #points to the specific object in the list we want (1/2 location as name in list because two each)
				craftMid = craftMid.text #converts xml to text for reading
	
				#find the bottom row crafting of specified object
				craftLow = dataList.findall("item/craftB") #gets a list of all the low rows (one for each name)
				craftLow = craftLow[altNumberCounter] #points to the specific object in the list we want (1/2 location as name in list because two each)
				craftLow = craftLow.text #converts xml to text for reading
	
				#find the key of specified object
				craftKey = dataList.findall("item/key") #gets a list of all the keys (one for each name)
				craftKey = craftKey[altNumberCounter] #points to the specific object in the list we want (1/2 location as name in list because two each)
				craftKey = craftKey.text #converts xml to text for reading
				
				#find the smelting of specified object
				itemSmelt = dataList.findall("item/smelt")
				itemSmelt = itemSmelt[altNumberCounter]
				itemSmelt = itemSmelt.text
				
				#find the tool of specified object
				itemTool = dataList.findall("item/tool")
				itemTool = itemTool[altNumberCounter]
				itemTool = itemTool.text
				
				#find the in-game location of specified object
				itemLocation = dataList.findall("item/location")
				itemLocation = itemLocation[altNumberCounter]
				itemLocation = itemLocation.text
				
				#find the stack amount of specified object
				itemStack = dataList.findall("item/stack")
				itemStack = itemStack[altNumberCounter]
				itemStack = itemStack.text
				
				#find the physics of specified object
				itemPhysics = dataList.findall("item/physics")
				itemPhysics = itemPhysics[altNumberCounter]
				itemPhysics = itemPhysics.text
				
				#find other info on specified object
				itemOtherInfo = dataList.findall("item/other")
				itemOtherInfo = itemOtherInfo[altNumberCounter]
				itemOtherInfo = itemOtherInfo.text

				break #end the loop
	
		#-----------------------code to check ids of objects-----------------------
		idNumberCounter = -1 #reset var
		idList = dataList.findall("item/id") #find all objects in <id> brackets
		
		for i in idList:
			idNumberCounter = idNumberCounter + 1
			idText = i.text #convert object to text for comparison
			if idText == choice:
				found = 1
		
				#find the name of specified object
				name = dataList.findall("item/name") #gets a list of all the IDs (one for each name)
				name = name[idNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
				name = name.text #converts xml to text for reading
	
				#find the ID of specified object
				idnum = dataList.findall("item/id") #gets a list of all the IDs (one for each name)
				idnum = idnum[idNumberCounter] #points to the specific object in the list we want (1/2 location as name in list because two each)
				idnum = idnum.text #converts xml to text for reading
	
				#find the top row crafting of specified object
				craftTop = dataList.findall("item/craftT") #gets a list of all the top rows (one for each name)
				craftTop = craftTop[idNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
				craftTop = craftTop.text #converts xml to text for reading
	
				#find the middle row crafting of specified object
				craftMid = dataList.findall("item/craftM") #gets a list of all the mid rows (one for each name)
				craftMid = craftMid[idNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
				craftMid = craftMid.text #converts xml to text for reading
	
				#find the bottom row crafting of specified object
				craftLow = dataList.findall("item/craftB") #gets a list of all the low rows (one for each name)
				craftLow = craftLow[idNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
				craftLow = craftLow.text #converts xml to text for reading
	
				#find the key of specified object
				craftKey = dataList.findall("item/key") #gets a list of all the keys (one for each name)
				craftKey = craftKey[idNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
				craftKey = craftKey.text #converts xml to text for reading
				
				#find the smelting of specified object
				itemSmelt = dataList.findall("item/smelt")
				itemSmelt = itemSmelt[idNumberCounter]
				itemSmelt = itemSmelt.text
				
				#find the tool of specified object
				itemTool = dataList.findall("item/tool")
				itemTool = itemTool[idNumberCounter]
				itemTool = itemTool.text
				
				#find the in-game location of specified object
				itemLocation = dataList.findall("item/location")
				itemLocation = itemLocation[idNumberCounter]
				itemLocation = itemLocation.text
				
				#find the stack amount of specified object
				itemStack = dataList.findall("item/stack")
				itemStack = itemStack[idNumberCounter]
				itemStack = itemStack.text
				
				#find the physics of specified object
				itemPhysics = dataList.findall("item/physics")
				itemPhysics = itemPhysics[idNumberCounter]
				itemPhysics = itemPhysics.text
				
				#find other info on specified object
				itemOtherInfo = dataList.findall("item/other")
				itemOtherInfo = itemOtherInfo[idNumberCounter]
				itemOtherInfo = itemOtherInfo.text
				
				break #end the loop
	
		#code to give if the object wasn't found
		if found == 0:
			name = ""
			idnum = "\n\nObject not found. Please enter\na new query and try again."
			craftTop = ""
			craftMid = ""
			craftLow = ""
			craftKey = ""
			itemSmelt = ""
			itemTool = ""
			itemLocation = ""
			itemStack = ""
			itemPhysics = ""
			itemOtherInfo = ""
		
		GUI.updateWindow(self,name,idnum,craftTop,craftMid,craftLow,craftKey,itemSmelt,itemTool,itemLocation,itemStack,itemPhysics,itemOtherInfo)#runs the update function to update the window with the given information
		
	def updateWindow(self,name,idnum,craftTop,craftMid,craftLow,craftKey,itemSmelt,itemTool,itemLocation,itemStack,itemPhysics,itemOtherInfo):
		self.craftingBox = Tkinter.Canvas(root,width=300,height=350)
		
		self.craftingBox.create_text(5,15,text="name: " + name, anchor="nw")
		
		self.craftingBox.create_text(5,30,text="id: " + idnum,anchor="nw")
		
		self.craftingBox.create_text(5,60,text=craftTop,anchor="nw",font="TkFixedFont")
		self.craftingBox.create_text(5,75,text=craftMid,anchor="nw",font="TkFixedFont")
		self.craftingBox.create_text(5,90,text=craftLow,anchor="nw",font="TkFixedFont")
		
		self.craftingBox.create_text(5,120,text="key: " + craftKey,anchor="nw",width=300)
		
		self.craftingBox.create_text(5,180,text="Smelt: " + itemSmelt,anchor="nw",width=300)
		self.craftingBox.create_text(5,195,text="Tool: " + itemTool,anchor="nw",width=300)
		self.craftingBox.create_text(5,210,text="Location: " + itemLocation,anchor="nw",width=300)
		self.craftingBox.create_text(5,225,text="Stack: " + itemStack,anchor="nw",width=300)
		self.craftingBox.create_text(5,240,text="Physics: " + itemPhysics,anchor="nw",width=300)
		self.craftingBox.create_text(5,255,text="Other: " + itemOtherInfo,anchor="nw",width=300)
		
		self.craftingBox.grid(row=1, column=0, columnspan=2,sticky="w")
	
	def aboutDisp(self):
		aboutWindow = Tkinter.Tk()
		aboutWindow.title(string="About")
		aboutWindow.resizable(False, False)
		
		titleLabel = Tkinter.Label(aboutWindow,text="Craftbook v. 1.3.0",font="bold")
		titleLabel.grid(row=0,column=0)
		
		subTitleLabel = Tkinter.Label(aboutWindow,text=" Built for Minecraft 1.3.0\n")
		subTitleLabel.grid(row=1,column=0)
		
		devTeam = Tkinter.Label(aboutWindow,text="Development Team:\n  Ben Schwabe\n")
		devTeam.grid(row=2,column=0)
		
		email = Tkinter.Label(aboutWindow,text="Contact Information:\n  craftbook.devteam@gmail.com")
		email.grid(row=3,column=0)
		
		space = Tkinter.Label(aboutWindow,text="")
		space.grid(row=4,column=0)
		
		aboutCloseButton = Tkinter.Button(aboutWindow,text="Close",command=aboutWindow.destroy)
		aboutCloseButton.grid(row=5,column=0,sticky="e")
		
		name = ""
		idnum = ""
		craftTop = " | | "
		craftMid = " | | "
		craftLow = " | | "
		craftKey = ""
		itemSmelt = ""
		itemTool = ""
		itemLocation = ""
		itemStack = ""
		itemPhysics = ""
		itemOtherInfo = ""
	
	def helpDisp(self):
		helpWindow = Tkinter.Tk()
		helpWindow.title(string="Help")
		helpWindow.resizable(False, False)
		
		titleLabel = Tkinter.Label(helpWindow,text="Craftbook Help",font="bold")
		titleLabel.grid(row=0,column=0)
		
		subTitleLabel = Tkinter.Label(helpWindow,text="How to use Craftbook:\n")
		subTitleLabel.grid(row=1,column=0)
		
		bodyLabel = Tkinter.Label(helpWindow,text="To use Craftbook, simply type in \nthe name or ID of an object \nfound in Minecraft and click \n<Search>. It will then give you \nthe name and ID of the object\nand how to craft it in a crafting\ntable. \n\nTo find a mob's information,\ntype 'mob: '(including the\nspace at the end) into the input\narea and the name of the mob\nand click <Search>.\n\nTo quit Craftbook, close the\nwindow or go to File>Quit. Type\n'about' into the input area and\npress <enter> for program\ninformation.\n",justify="left")
		bodyLabel.grid(row=2,column=0)
		
		helpCloseButton = Tkinter.Button(helpWindow,text="Close",command=helpWindow.destroy)
		helpCloseButton.grid(row=5,column=0,sticky="e")
		
		name = ""
		idnum = ""
		craftTop = " | | "
		craftMid = " | | "
		craftLow = " | | "
		craftKey = ""
		itemSmelt = ""
		itemTool = ""
		itemLocation = ""
		itemStack = ""
		itemPhysics = ""
		itemOtherInfo = ""

root = Tkinter.Tk()#creates the window
root.title(string="Craftbook")#titles the window
root.resizable(False, False)

window = GUI(root,name,idnum,craftTop,craftMid,craftLow,craftKey,itemSmelt,itemTool,itemLocation,itemStack,itemPhysics,itemOtherInfo)#calls the info on the window

root.mainloop()#displays the window
