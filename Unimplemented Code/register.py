#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  craftbook.py
#
#  Copyright 2012 Suturesoft
#

#import
import Tkinter
from urllib import urlopen
import webbrowser

#number of four-digit groupings in product key
keylength = 4

class GUI:
    def __init__(self,master):
        
        #---MENUBAR START---#
        self.menubar = Tkinter.Menu(root)#creates a menubar

        self.filemenu = Tkinter.Menu(self.menubar, tearoff=0)#creates the file menu button
        self.filemenu.add_command(label="Quit", command=root.quit)#creates the Quit button in the file dropdown
        self.menubar.add_cascade(label="File", menu=self.filemenu)#creates the dropdown
        root.configure(menu=self.menubar)#displays the menubar
        
        self.title = Tkinter.Label(root,text="Thank you for purchasing Craftbook!",font="TkSubHeadingFont")
        self.title.grid(row=0,column=0,columnspan=7)
        
        self.subtitle = Tkinter.Label(root,text="Please register your product to get started.\n\n")
        self.subtitle.grid(row=1,column=0,columnspan=7)
        
        self.registertext = Tkinter.Label(root,text="Please type in the product key you recieved.")
        self.registertext.grid(row=2,column=0,columnspan=7)
        
        self.keyEntry1 = Tkinter.Entry(root,width="4",font="TkFixedFont")
        self.keyEntry1.focus_set()
        self.keyEntry1.grid(row=3, column=0,padx=2)
        
        self.dashtext = Tkinter.Label(root,text="-")
        self.dashtext.grid(row=3,column=1,padx=2)
        
        self.keyEntry2 = Tkinter.Entry(root,width="4",font="TkFixedFont")
        self.keyEntry2.grid(row=3, column=2,padx=2)
        
        self.dashtext = Tkinter.Label(root,text="-")
        self.dashtext.grid(row=3,column=3,padx=2)
        
        self.keyEntry3 = Tkinter.Entry(root,width="4",font="TkFixedFont")
        self.keyEntry3.grid(row=3, column=4,padx=2)
        
        self.dashtext = Tkinter.Label(root,text="-")
        self.dashtext.grid(row=3,column=5,padx=2)
        
        self.keyEntry4 = Tkinter.Entry(root,width="4",font="TkFixedFont")
        self.keyEntry4.grid(row=3, column=6,padx=2)
        
        self.submitButton = Tkinter.Button(root,text="Register",command=self.CheckValid)
        self.submitButton.grid(row=4,column=0,columnspan=7,pady=10)
    
    def CheckValid(self):
        #define keyinput
        keyinput = []
        for i in range(0,keylength):
            keyinput.append(0)
            
        keyinput[0] = self.keyEntry1.get().lower()
        keyinput[1] = self.keyEntry2.get().lower()
        keyinput[2] = self.keyEntry3.get().lower()
        keyinput[3] = self.keyEntry4.get().lower()
        keystring = "-".join(keyinput)
        
        if (len(keystring)) < 19 or (len(keystring)) > 19:
            print "error"
        else:
            print keystring#TEMPORARY
        
            webbrowser.open("http://www.suturesoft.com")
        """
        #validate key
        try:
            #gets newest version
            updateSource = urlopen("http://www.suturesoft.com/Updates/craftbook.txt")
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
            dataLabel = Tkinter.Label(root,text="\n\nThe server could not be accessed at this time.\nPlease check your internet connection and try again.\n\n")
            dataLabel.pack()
        
        #checks for updates
        elif not failed:
            
        #close server file
        updateSource.close()
        """
#checks file existence
try:
    keyfile = open("valid.dat")
    key = keyfile.read()

    #checks for validation
    if key == "1":
        registered = 1
    else:
        registered = 0

except:
    registered = 0
    keyfile = open("valid.dat","w")
    keyfile.write("xxxx-xxxx-xxxx-xxxx")

#Determine if registered; if yes, run program as normal. if no, disp register window
if registered == 1:
    keyfile.close()
    execfile("craftbook_stable.py")
else:
    root = Tkinter.Tk()#creates the window
    root.title(string="Register Craftbook")#titles the window
    root.iconbitmap('icon.ico')
    root.resizable(False, False)
    root.attributes("-alpha",0.97)
    
    window = GUI(root)#calls the info on the window
    
    root.mainloop()#displays the window
keyfile.close()