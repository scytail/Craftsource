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

#Define vars
loop = 1 #repeats program
choice = "" #user input var
found = 0 #fix used to not display "not found" error on quit
nameNumberCounter = -1 #count off which name in the list we are in
idNumberCounter = -1 #count off which id in the list we are in
altNumberCounter = -1 #count off which alternate name in the list we are in

dataList = ET.parse('data.xml') #parse the file for reading

print("")
print("Craftbook Version 1.3.0\nBuilt for Minecraft 1.3.0.")
print("----------------------------------------\n")

while loop == 1:
	found = 0 #reset found var
	nameNumberCounter = -1
	idNumberCounter = -1
	altNumberCounter = -1

	choice = raw_input("Recipe: ").lower() #user input (and converts to lowercase)

#-----------------------code to check names-----------------------
	nameNumberCounter = -1 #reset var
	nameList = dataList.findall("item/name") #find all objects in <name> brackets

	for i in nameList:
		nameNumberCounter = nameNumberCounter + 1
		nameText = i.text #convert object to text for comparison
		if nameText == choice:
			found = 1

			print("----------------------------------------")
			print("Name:" + choice)

			#find the ID of specified object
			idnum = dataList.findall("item/id") #gets a list of all the IDs (one for each name)
			idnum = idnum[nameNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
			idnum = idnum.text #converts xml to text for reading
			print("ID:" + idnum) #displays
			print("")

			#find the top row crafting of specified object
			craftTop = dataList.findall("item/craftT") #gets a list of all the top rows (one for each name)
			craftTop = craftTop[nameNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
			craftTop = craftTop.text #converts xml to text for reading
			print("\t" + craftTop) #displays

			#find the middle row crafting of specified object
			craftMid = dataList.findall("item/craftM") #gets a list of all the mid rows (one for each name)
			craftMid = craftMid[nameNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
			craftMid = craftMid.text #converts xml to text for reading
			print("\t" + craftMid) #displays

			#find the bottom row crafting of specified object
			craftLow = dataList.findall("item/craftB") #gets a list of all the low rows (one for each name)
			craftLow = craftLow[nameNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
			craftLow = craftLow.text #converts xml to text for reading
			print("\t" + craftLow) #displays

			#find the key of specified object
			craftKey = dataList.findall("item/key") #gets a list of all the low rows (one for each name)
			craftKey = craftKey[nameNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
			craftKey = craftKey.text #converts xml to text for reading
			print("\nkey: " + craftKey) #displays

			print("----------------------------------------")

			break #end the loop

	#other choices
	if choice == "help" or choice == "?":
		found = 1
		print("----------------------------------------")
		print("Craftbook Help")
		print("")
		print("How to use Craftbook:")
		print("\tTo use Craftbook, simply type in \n\tthe name or ID of an object \n\tfound in Minecraft and press \n\t<enter>. It will then give you \n\tthe name and ID of the object\n\tand how to craft it in a\n\tcrafting table. \n\n\tTo find a mob's information,\n\ttype 'mob: '(including the\n\tspace at the end) into the input\n\t area and the name of the mob\n\tand press <enter>.\n\n\tTo quit Craftbook, type 'stop' \n\tor 'quit' into the input area \n\tand press <enter>. Type 'about' \n\tinto the input area and press \n\t<enter> for program information.")
		print("----------------------------------------")
	elif choice == "about":
		found = 1
		print("----------------------------------------")
		print("Craftbook - v. 1.3.0\n  Built for Minecraft 1.3.0")
		print("")
		print("Dev Team:\n  Ben Schwabe")
		print("")
		print("e-mail:\n  bspymaster@gmail.com")
		print("----------------------------------------")
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
	elif choice == "stop" or choice == "quit" or choice == "close" or choice == "exit":
		loop = 0 #stops the program	

#-----------------------code to check alternate names-----------------------
	altNumberCounter = -1 #reset var
	altList = dataList.findall("item/alt") #find all objects in <alt> brackets

	for i in altList:
		altNumberCounter = altNumberCounter + 1
		altText = i.text #convert object to text for comparison

		if altText == choice:
			found = 1
			print("----------------------------------------")

			#find the name of specified object
			name = dataList.findall("item/name") #gets a list of all the IDs (one for each name)
			name = name[altNumberCounter] #points to the specific object in the list we want (1/2 location as name in list because two each)
			name = name.text #converts xml to text for reading
			print("Name:" + name) #displays

			#find the ID of specified object
			idnum = dataList.findall("item/id") #gets a list of all the IDs (one for each name)
			idnum = idnum[altNumberCounter] #points to the specific object in the list we want (1/2 location as name in list because two each)
			idnum = idnum.text #converts xml to text for reading
			print("ID:" + idnum) #displays
			print("")

			#find the top row crafting of specified object
			craftTop = dataList.findall("item/craftT") #gets a list of all the top rows (one for each name)
			craftTop = craftTop[altNumberCounter] #points to the specific object in the list we want (1/2 location as name in list because two each)
			craftTop = craftTop.text #converts xml to text for reading
			print("\t" + craftTop) #displays

			#find the middle row crafting of specified object
			craftMid = dataList.findall("item/craftM") #gets a list of all the mid rows (one for each name)
			craftMid = craftMid[altNumberCounter] #points to the specific object in the list we want (1/2 location as name in list because two each)
			craftMid = craftMid.text #converts xml to text for reading
			print("\t" + craftMid) #displays

			#find the bottom row crafting of specified object
			craftLow = dataList.findall("item/craftB") #gets a list of all the low rows (one for each name)
			craftLow = craftLow[altNumberCounter] #points to the specific object in the list we want (1/2 location as name in list because two each)
			craftLow = craftLow.text #converts xml to text for reading
			print("\t" + craftLow) #displays

			#find the key of specified object
			craftKey = dataList.findall("item/key") #gets a list of all the low rows (one for each name)
			craftKey = craftKey[altNumberCounter] #points to the specific object in the list we want (1/2 location as name in list because two each)
			craftKey = craftKey.text #converts xml to text for reading
			print("\nkey: " + craftKey) #displays

			print("----------------------------------------")

			break #end the loop

#-----------------------code to check ids of objects-----------------------
	idNumberCounter = -1 #reset var
	idList = dataList.findall("item/id") #find all objects in <id> brackets

	for i in idList:
		idNumberCounter = idNumberCounter + 1
		idText = i.text #convert object to text for comparison
		if idText == choice:
			found = 1

			print("----------------------------------------")

			#find the name of specified object
			name = dataList.findall("item/name") #gets a list of all the IDs (one for each name)
			name = name[idNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
			name = name.text #converts xml to text for reading
			print("Name:" + name) #displays

			print("ID:" + choice) #displays
			print("")

			#find the top row crafting of specified object
			craftTop = dataList.findall("item/craftT") #gets a list of all the top rows (one for each name)
			craftTop = craftTop[idNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
			craftTop = craftTop.text #converts xml to text for reading
			print("\t" + craftTop) #displays

			#find the middle row crafting of specified object
			craftMid = dataList.findall("item/craftM") #gets a list of all the mid rows (one for each name)
			craftMid = craftMid[idNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
			craftMid = craftMid.text #converts xml to text for reading
			print("\t" + craftMid) #displays

			#find the bottom row crafting of specified object
			craftLow = dataList.findall("item/craftB") #gets a list of all the low rows (one for each name)
			craftLow = craftLow[idNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
			craftLow = craftLow.text #converts xml to text for reading
			print("\t" + craftLow) #displays

			#find the key of specified object
			craftKey = dataList.findall("item/key") #gets a list of all the low rows (one for each name)
			craftKey = craftKey[idNumberCounter] #points to the specific object in the list we want (same location as name in list because one each)
			craftKey = craftKey.text #converts xml to text for reading
			print("\nkey: " + craftKey) #displays

			print("----------------------------------------")

			break #end the loop

	#code to give if the object wasn't found
	if loop != 0 and found == 0:
		print "Object not found. Plese enter a new query and try again."
