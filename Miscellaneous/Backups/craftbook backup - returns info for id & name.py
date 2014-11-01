#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import xml functions
import xml.etree.ElementTree as ET

#Define vars
loop = 1 #repeats program
choice = "" #user input var
found = 0 #fix used to not display "not found" error on quit
nameNumberCounter = -1 #count off which name in the list we are in
idNumberCounter = -1 #count off which id in the list we are in

dataList = ET.parse('data.xml') #parse the file for reading

while loop == 1:
	found = 0 #reset found var
	nameNumberCounter = -1 #reset var
	idNumberCounter = -1 #reset var
	
	choice = raw_input("Recipe: ").lower() #user input (and converts to lowercase)
	
#-----------------------code to check names-----------------------
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
			print("\n" + craftKey) #displays
			
			print("----------------------------------------")

			break #end the loop
			
		#other choices
		elif choice == "stop" or choice == "quit" or choice == "close":
			loop = 0 #stops the program
		"""
		elif choice == "list":
			print("TODO: List all of the elements here (try getting all names, converting to text and dip in a for loop)")
		"""

#-----------------------code to check alternate names-----------------------
	altList = dataList.findall("item/alt") #find all objects in <alt> brackets
	
	for i in altList:
		altText = i.text #convert object to text for comparison
		if altText == choice:
			found = 1
			
			print "you found it!"
			#TODO: add code here to gather the info on the specified object
			
			break #end the loop

#-----------------------code to check ids of objects-----------------------
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
			print("\n" + craftKey) #displays
			
			print("----------------------------------------")
			
			break #end the loop
	
	#code to give if the object wasn't found
	if loop != 0 and found == 0:
		print "Object not found. Plese enter a new query and try again."
