#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import xml functions
import xml.etree.ElementTree as ET

#Define vars
loop = 1 #repeats program
choice = "" #user input var
found = 0 #fix used to not display "not found" error on quit

dataList = ET.parse('data.xml') #parse the file for reading

while loop == 1:
	found = 0 #reset found var
	choice = raw_input("Recipe: ").lower() #user input (and converts to lowercase)
	
#-----------------------code to check names-----------------------
	nameList = dataList.findall("item/name") #find all objects in <name> brackets
	
	for i in nameList:
		nameText = i.text #convert object to text for comparison
		if nameText == choice:
			print "you found it!"
			#TODO: add code here to gather the info on the specified object
			found = 1
			break #end the loop
		elif choice == "stop" or choice == "quit" or choice == "close":
			loop = 0 #stops the program

#-----------------------code to check alternate names-----------------------
	altList = dataList.findall("item/alt") #find all objects in <alt> brackets
	
	for i in altList:
		altText = i.text #convert object to text for comparison
		if altText == choice:
			print "you found it!"
			#TODO: add code here to gather the info on the specified object
			found = 1
			break #end the loop

#-----------------------code to check ids of objects-----------------------
	idList = dataList.findall("item/id") #find all objects in <id> brackets
	
	for i in idList:
		idText = i.text #convert object to text for comparison
		if idText == choice:
			print "you found it!"
			#TODO: add code here to gather the info on the specified object
			found = 1
			break #end the loop
	
	#code to give if the object wasn't found
	if loop != 0 and found == 0:
		print "Object not found. Plese enter a new query and try again."
