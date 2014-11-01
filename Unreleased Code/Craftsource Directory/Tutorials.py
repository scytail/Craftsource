#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tutorials.py
#  class of windows that display tutorials
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
    
class Tutorials:
    def adventuringDisp(self):
        window = Toplevel()
        window.title(string="Adventuring Tips")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')
        
        #TAB SUPPORT#
        notebook = Notebook(window)
        notebook.grid(row=1,column=0)
        
        titleLabel = Label(window,text="Tips for Adventuring",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---INVENTORY---#
        inventoryFrame = Frame(notebook)
        inventoryFrame.pack()
        
        subTitleLabel = Label(inventoryFrame,text="Inventory",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame1 = Frame(inventoryFrame)

        textbox1 = Text(frame1,bd=1,width=60,height=15,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END, "Your inventory, when embarking on an adventure, should be as clear as possible. An adventurer normally picks up many items in his or her travels, and more open inventory space is more space that can be used for items collected along the way. Some things that should always be carried along with you when going on a full-scale adventure are:\n1) Weapons such as a sword and/or bow (with arrows)\n2) A pickaxe (preferably iron or diamond)\n3) 64 wooden logs \n4) Plenty of food, cooked meat such as steak or cooked porkchops and/or apples or bread\n5) A bed \n6) A crafting table and a furnace\n7) 64 Torches.\nSome things are also very helpful to take along, although are not necessary, such as 64 dirt and/or cobblestone for making shelters quickly or climbing up mountains easily without having to dig; tools such as shovels and axes for faster digging times, and a nether chest. The nether chest can be placed on the ground, have items stored in it as a sort of cache or reserve and then dug so that if the player dies, those items will still be in the ender chest and it also frees up space in your immediate inventory. Ender chests can be dug by any pickaxe, so the only resource problem is creating an eye of ender and retrieving 8 obsidian blocks.")
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=1,column=0)
        
        notebook.add(inventoryFrame, text='Inventory')
        
        
        #---BREADCRUMBS---#
        breadcrumbFrame = Frame(notebook)
        breadcrumbFrame.pack()
        
        subTitleLabel = Label(breadcrumbFrame,text="Breadcrumb Trails",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame2 = Frame(breadcrumbFrame)

        textbox2 = Text(frame2,bd=1,width=60,height=15,wrap="word")
        textbox2.pack(side=LEFT,fill=Y)

        scrollbar2 = Scrollbar(frame2)
        scrollbar2.pack(side=RIGHT,fill=Y)
        scrollbar2.config(command=textbox2.yview)

        textbox2.insert(END, "When exploring anywhere, whether it be the nether, a mineshaft, or the surface world, you can easily get lost. A good way to combat this is to follow a standard method. A popular method that always works is to place torches so that if you pass a torch on your right side, you know you are exploring farther away from the exit or from your house, and if you pass a torch on your left side, you know you are heading home or heading towards the exit. When placing torches, make sure that the next torch is in sight of the previous torch, so that you don't lose track of your torch trail. If you are exploring in the nether or on the surface of the overworld, this may seem harder to do. However, you can easily recreate this by creating a post two blocks high out of a material such as dirt or cobblestone and placing a torch on the side of it. The torch, when placed, should be on your right if you are facing away from your original direction,and on your left if you are facing towards it. Simple disciplines like this can keep you from getting lost and can allow you to travel more deeply into complex cave systems without worrying about where the exit is.")
        textbox2.config(state="disabled")
        textbox2.config(yscrollcommand=scrollbar2.set)

        frame2.grid(row=1,column=0)
        
        notebook.add(breadcrumbFrame, text='Breadcrumb Trails')
        
        
        #---EFFICIENCY---#
        efficiencyFrame = Frame(notebook)
        efficiencyFrame.pack()
        
        subTitleLabel = Label(efficiencyFrame,text="Hunting and Efficiency",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame3 = Frame(efficiencyFrame)

        textbox3 = Text(frame3,bd=1,width=60,height=15,wrap="word")
        textbox3.pack(side=LEFT,fill=Y)

        scrollbar3 = Scrollbar(frame3)
        scrollbar3.pack(side=RIGHT,fill=Y)
        scrollbar3.config(command=textbox3.yview)

        textbox3.insert(END, "Often you will need to gather things quickly, or will need food but don't have the time to cook it. When mining out such things as cacti or sugar cane, dig the lowest block of the substance and the rest will fall down as well, saving you the time of digging three blocks by digging just one block. Also, when killing mobs, try to hit them while sprinting or while jumping. These hits have a possibility of dealing extra damage to the mobs and save valuable uses on your equipment. When obtaining meat as food from mobs such as pigs or cows, light them on fire. If they die while from the fire, they will drop cooked meat, which allows you to eat it and have more of your food bar filled than if it had been raw. If you are mining gravel or sand, an efficient way to clear it out instead of having to dig each block individually is to dig the bottom block and then quickly place a torch underneath. If sand or gravel falls on the torch, it will be destroyed and turn into a droppable item that you can easily collect. This method saves you from having to mine out a lot of gravel or sand individually.")
        textbox3.config(state="disabled")
        textbox3.config(yscrollcommand=scrollbar3.set)

        frame3.grid(row=1,column=0)
        
        notebook.add(efficiencyFrame, text="Hunting and Efficiency")

        #---TOOLS---#
        toolsFrame = Frame(notebook)
        toolsFrame.pack()
        
        subTitleLabel = Label(toolsFrame,text="Tools and Trees",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame4 = Frame(toolsFrame)

        textbox4 = Text(frame4,bd=1,width=60,height=15,wrap="word")
        textbox4.pack(side=LEFT,fill=Y)

        scrollbar4 = Scrollbar(frame4)
        scrollbar4.pack(side=RIGHT,fill=Y)
        scrollbar4.config(command=textbox4.yview)

        textbox4.insert(END, "A good thing to keep in mind when adventuring is to always use the correct tool for the job. By using the right tool, you'll mine things faster, and not waste the tools you have when you may need them later. While adventuring, you may not have the resources to craft another tool, if you waste yours on something they are not supposed to be used on. Also, when enchanting tools, don't put a high-cost enchantment on a low cost tool. Iron or Diamond are the best choices for large enchantments because they last the longest, and in the case of pickaxes, can dig more blocks. Small enchantments on tools can still go a long way, however, and achieving level 5 experience is not difficult. If at all possible, when mining for an extended period of time, use a silk touch enchanted pickaxe to mine ores. One block of redstone ore takes up less space than six or seven redstone dust, which can quickly fill up your inventory. You can then take the ores back to your base when you are finished exploring and use a fortune enchanted pickaxe to get the most out of the ores. If you are mining trees, don't use a silk touch pickaxe to get the leaves off trees. Shears will also allow you to harvest the leaves directly. To most efficiently dig trees, dig blocks two and three up from the base and then jump on the first block and dig up from there. This gives you a boost when reaching the tops of trees. Avoid chopping large oak trees because they form a very irregular shape and is very difficult to chop all of the wood contained in the tree. Some wood is often hidden in branches a few blocks away. Go on to a smaller tree to save time.")
        textbox4.config(state="disabled")
        textbox4.config(yscrollcommand=scrollbar4.set)

        frame4.grid(row=1,column=0)

        notebook.add(toolsFrame, text='Tools and Trees')
        
        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=2,column=0)
        
    def safeHomeDisp(self):
        window = Toplevel()
        window.title(string="Building Tips")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')
        
        #TAB SUPPORT#
        notebook = Notebook(window)
        notebook.grid(row=1,column=0)

        titleLabel = Label(window,text="Building a Safe Home",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---WATER & LAVA---#
        waterLavaFrame = Frame(notebook)
        waterLavaFrame.pack()
        
        subTitleLabel = Label(waterLavaFrame,text="Water and Lava", font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame1 = Frame(waterLavaFrame)

        textbox1 = Text(frame1,bd=1,width=60,height=15,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Items like wheat, torches, and redstone are prone to damage by moving water. If water interacts with them, they are destroyed. To prevent this, be sure that the area in which you build has no water sources, hidden or shown, that may interfere with or flood your house as you expand it. Lava, although it moves more slowly, is much more hazardous, because it destroys torches and similar items the same way water does, but then causes the items dropped by the destroyed blocks to be burned up, causing a loss of resources. It also can burn nearby flammable objects such as fences and wood, either by touching it or by the fireballs that occasionally fly out. Lava also causes the player to burn, and the decreased moving rate while in it can kill players in seconds.")
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=1,column=0)
        
        notebook.add(waterLavaFrame, text='Liquids')

        #---SAND & GRAVEL---#
        sandGravelFrame = Frame(notebook)
        sandGravelFrame.pack()
        
        subTitleLabel = Label(sandGravelFrame,text="Sand and Gravel",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame2 = Frame(sandGravelFrame)

        textbox2 = Text(frame2,bd=1,width=60,height=15,wrap="word")
        textbox2.pack(side=LEFT,fill=Y)

        scrollbar2 = Scrollbar(frame2)
        scrollbar2.pack(side=RIGHT,fill=Y)
        scrollbar2.config(command=textbox2.yview)

        textbox2.insert(END,"Be careful when building on sand or gravel, as these blocks are affected by gravity. Always ensure that your roof has a stable top like stone or cobblestone, especially if your house is built under sand. Similarly, if you build your house on top of sand, make sure that you have a strong foundation and that there are no hidden caves under your house. If you dig under your house and start mining sand, you may accidentally dig out your floor. This is possible if a foundation was not laid correctly.")
        textbox2.config(state="disabled")
        textbox2.config(yscrollcommand=scrollbar2.set)

        frame2.grid(row=1,column=0)
        
        notebook.add(sandGravelFrame, text='Gravity')

        #---GENERAL DEFENSES---#
        defenseFrame = Frame(notebook)
        defenseFrame.pack()
        
        subTitleLabel = Label(defenseFrame,text="General Mob Defenses", font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame3 = Frame(defenseFrame)

        textbox3 = Text(frame3,bd=1,width=60,height=15,wrap="word")
        textbox3.pack(side=LEFT,fill=Y)

        scrollbar3 = Scrollbar(frame3)
        scrollbar3.pack(side=RIGHT,fill=Y)
        scrollbar3.config(command=textbox3.yview)

        textbox3.insert(END,"To stop mobs from invading your house, build a fence or wall around your house. Wooden fences are designed for stopping mobs from getting in, but for a more effective approach, you may find that a cobblestone wall better withstands explosive damage. As an added bonus, skeletons can't shoot arrows over walls if build high enough. You should avoid using wooden doors on your house when playing on hard or hardcore mode, as zombies can break down doors. This allows other mobs to enter your house after them. Fences made of two rows of cacti (in a checkerboard fashion) do well to simulate a barbed wire fence. Mobs that touch it get damaged and then try to avoid the fence, keeping you safe inside. Other protections include digging ditches and placing lava, water, or cacti at the bottom, or putting netherrack with fire around your house. Always remember to keep your house and surrounding areas well- lit as hostile mobs can only spawn in level 7 light or less. Ladders are not reccomeded as a mob deterrent to access your house unless you have a trapdoor at the top, because mobs can climb ladders.")
        textbox3.config(state="disabled")
        textbox3.config(yscrollcommand=scrollbar3.set)

        frame3.grid(row=1,column=0)
        
        notebook.add(defenseFrame, text='Mobs')

        #---CREEPER---#
        creeperFrame = Frame(notebook)
        creeperFrame.pack()
        
        
        subTitleLabel = Label(creeperFrame,text="Creeper Defenses",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame4 = Frame(creeperFrame)

        textbox4 = Text(frame4,bd=1,width=60,height=15,wrap="word")
        textbox4.pack(side=LEFT,fill=Y)

        scrollbar4 = Scrollbar(frame4)
        scrollbar4.pack(side=RIGHT,fill=Y)
        scrollbar4.config(command=textbox4.yview)

        textbox4.insert(END,"Creepers are, in all probability, one of the most dangerous mobs in the game. They remain silent until just before they explode, allowing one to creep up on you quite easily without your knowledge, and blowing you and your house to bits. Building large walls is highly recommended, as creepers will not explode if they have no direct path to the player (exemplified by a player standing on a tower two blocks tall with a creeper below the tower). Blocks like wood and glass are not recommended wall materials, as they have a low blast resistance, meaning that if a creeper explodes, many blocks will need to be replaced. A more sturdy block such as stone will withstand crepper explosions much better. Obsidian is not destroyed by explosions, and is thus the recommended wall material.")
        textbox4.config(state="disabled")
        textbox4.config(yscrollcommand=scrollbar4.set)

        frame4.grid(row=1,column=0)
        
        notebook.add(creeperFrame, text='Creepers')

        #---SPIDER---#
        spiderFrame = Frame(notebook)
        spiderFrame.pack()
        
        subTitleLabel = Label(spiderFrame,text="Spider Defenses", font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame5 = Frame(spiderFrame)

        textbox5 = Text(frame5,bd=1,width=60,height=15,wrap="word")
        textbox5.pack(side=LEFT,fill=Y)

        scrollbar5 = Scrollbar(frame5)
        scrollbar5.pack(side=RIGHT,fill=Y)
        scrollbar5.config(command=textbox5.yview)

        textbox5.insert(END,"Spiders can jump 2-3 blocks, and can climb walls, rendering most walls and ditches useless against them. Cactus walls are a bit more effective as spiders get damaged as they climb them, but they can still get inside. The recommended way to keep them out is to build a wall with an overhanging edge at least 4 blocks off the ground and an entrance that is only 1 block wide (spiders need two blocks to pass through a space). Underground houses are also recommended, as  spiders then need a 2x2 space to get down into it, making your job easier (although then it is much easier for other mobs to access it). Interrupting your wall with a glass pane or iron bars also stops a spider from climbing. Another classic way to protect walls is to have lava pouring down the side of it so that the spider must avoid it to survive.")
        textbox5.config(state="disabled")
        textbox5.config(yscrollcommand=scrollbar5.set)

        frame5.grid(row=1,column=0)
        
        notebook.add(spiderFrame, text='Spiders')

        #---SKELETON---#
        skeletonFrame = Frame(notebook)
        skeletonFrame.pack()
        
        subTitleLabel = Label(skeletonFrame,text="Skeleton Defenses",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame6 = Frame(skeletonFrame)

        textbox6 = Text(frame6,bd=1,width=60,height=15,wrap="word")
        textbox6.pack(side=LEFT,fill=Y)

        scrollbar6 = Scrollbar(frame6)
        scrollbar6.pack(side=RIGHT,fill=Y)
        scrollbar6.config(command=textbox6.yview)

        textbox6.insert(END,"Skeletons are quite irritating and harmful, as they have a ranged attack and can attack you from over a fence that keeps the actual mob out. Skeletons can also attack through defensive measures you have set up, such as walls made of iron bars or lava. The best method to stopping skeletons from hurting you is to create a low wall that a skeleton cannot see over and to have glass windows, rather than empty ones which skeletons can shoot through. Skeletons will not attack if they cannot see you, so small windows also minimize visibility time when you are walking by.")
        textbox6.config(state="disabled")
        textbox6.config(yscrollcommand=scrollbar6.set)

        frame6.grid(row=1,column=0)
        
        notebook.add(skeletonFrame, text='Skeletons')

        #---ZOMBIE---#
        zombieFrame = Frame(notebook)
        zombieFrame.pack()
        
        subTitleLabel = Label(zombieFrame,text="Zombie Defenses", font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame7 = Frame(zombieFrame)

        textbox7 = Text(frame7,bd=1,width=60,height=15,wrap="word")
        textbox7.pack(side=LEFT,fill=Y)

        scrollbar7 = Scrollbar(frame7)
        scrollbar7.pack(side=RIGHT,fill=Y)
        scrollbar7.config(command=textbox7.yview)

        textbox7.insert(END,"Zombies are probably the easiest mobs to defend from. Their short range of attack and slow movement allow for almost any defense to stop it. Landmines, pits, and walls are all good examples of ways to keep zombies out of your house. The one key thing to remember is that they can break wooden doors in hard or hardcore mode. To combat this, one can create a piston door or replace the wooden door with an iron door, which zombies cannot dig.")
        textbox7.config(state="disabled")
        textbox7.config(yscrollcommand=scrollbar7.set)

        frame7.grid(row=1,column=0)
        
        notebook.add(zombieFrame, text='Zombies')

        #---GHAST---#
        ghastFrame = Frame(notebook)
        ghastFrame.pack()
        
        subTitleLabel = Label(ghastFrame,text="Ghast Defenses",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame8 = Frame(ghastFrame)

        textbox8 = Text(frame8,bd=1,width=60,height=15,wrap="word")
        textbox8.pack(side=LEFT,fill=Y)

        scrollbar8 = Scrollbar(frame8)
        scrollbar8.pack(side=RIGHT,fill=Y)
        scrollbar8.config(command=textbox8.yview)

        textbox8.insert(END,"Ghasts, are extremely dangerous even though they only spawn in the nether, as they have an incredibly ranged exploding fireball attack that can destroy homes and create holes in netherrack overhangs. These explosions can also start fires which can burn down a player's house if it is made of flammable materials such as wood. The easiest way to combat a ghast is to build a roof over your house and to lay the foundation and structure of your house in a sturdy material such as obsidian or cobblestone. One can also create a ghast-free area by placing blocks in strategic areas so that there is never a 5x5x5 open space in the area, which is the area required for a ghast to spawn. Ghasts cannot see through glass, so creating a glass wall, although much weaker than stone or cobblestone, provides the same visibility protection form ghasts and allows you to see if any mobs are lurking outside before you leave the safety of your house.")
        textbox8.config(state="disabled")
        textbox8.config(yscrollcommand=scrollbar8.set)

        frame8.grid(row=1,column=0)
        
        notebook.add(ghastFrame, text='Ghasts')

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=2,column=0)

    def shelterDisp(self):
        window = Toplevel()
        window.title(string="Shelter Tutorial")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')
        
        #TAB SUPPORT#
        notebook = Notebook(window)
        notebook.grid(row=1,column=0)

        titleLabel = Label(window,text="Types of Shelters",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0,columnspan=3)

        #---NOMADIC---#
        nomadFrame = Frame(notebook)
        nomadFrame.pack()
        
        subTitleLabel = Label(nomadFrame,text="\nNomadic",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=0)

        descriptionLabel = Label(nomadFrame,text="Nomadic houses are usually very simple and can be constructed in almost no time. They also need very few resources, as the design of them is not meant to be pretty, just functional.\n",justify="center",wraplength=400)
        descriptionLabel.grid(row=2,column=0,sticky="n")

        #---EMERGENCY HOUSE---#
        houseLabel = Label(nomadFrame,text="Emergency House",font="TkHeadingFont")
        houseLabel.grid(row=3,column=0)

        frame1 = Frame(nomadFrame)

        textbox1 = Text(frame1,bd=1,width=50,height=9,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Emergency houses are very basic, being designed so that it provides basic protection in cases of the player being stuck in the wilderness with night approaching. The most basic of these provides digging three blocks down, and then two blocks forward in one direction. You can then place a dirt block or any block on the above hole in your roof, sealing you in. Place a torch and a bed, and your house is built. An alternate includes digging four blocks deep into a cliff or mountain and sealing yourself in that as well. Both usually work fairly well.")
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=4,column=0)

        #--PILLAR SHELTER---#
        houseLabel = Label(nomadFrame,text="Pillar Shelter",font="TkHeadingFont")
        houseLabel.grid(row=5,column=0)

        frame2 = Frame(nomadFrame)

        textbox2 = Text(frame2,bd=1,width=50,height=9,wrap="word")
        textbox2.pack(side=LEFT,fill=Y)

        scrollbar2 = Scrollbar(frame2)
        scrollbar2.pack(side=RIGHT,fill=Y)
        scrollbar2.config(command=textbox2.yview)

        textbox2.insert(END,"Pillar shelters are good if when you wake, you want to be able to see the landscape where you want to go or to see if there are any dangerous mobs around before encountering them directly. To build a pillar shelter, construct a tower of any block not sand or gravel. While at the top of the tower, build a small platform around the pillar, making sure all of the sides of the pillar have some sort of a lip in them (to prevent spiders from attacking you). Make sure the platform is well lit, place your bed, and sleep. Be careful not to move to quickly when you first wake up, however, in case you accidentally fall off of the tower. This also works with trees and large mushrooms, assuming that the platform is the leaves of the tree and the tower is the trunk.")
        textbox2.config(state="disabled")
        textbox2.config(yscrollcommand=scrollbar2.set)

        frame2.grid(row=6,column=0)

        #---HUT---#
        houseLabel = Label(nomadFrame,text="Huts",font="TkHeadingFont")
        houseLabel.grid(row=7,column=0)

        frame3 = Frame(nomadFrame)

        textbox3 = Text(frame3,bd=1,width=50,height=9,wrap="word")
        textbox3.pack(side=LEFT,fill=Y)

        scrollbar3 = Scrollbar(frame3)
        scrollbar3.pack(side=RIGHT,fill=Y)
        scrollbar3.config(command=textbox3.yview)

        textbox3.insert(END,"Huts are basic above-ground houses. They can be as simple as building a box out of dirt with room enough for a bed, or finding an NPC village and sleeping in one of the buildings there. Another open-air hut can be made using walls at least three blocks high with a lip four blocks off the ground (to prevent spiders from climbing in) and placing your bed inside these walls.")
        textbox3.config(state="disabled")
        textbox3.config(yscrollcommand=scrollbar3.set)

        frame3.grid(row=8,column=0)
        
        notebook.add(nomadFrame, text='Nomadic')

        #---EFFICIENT---#
        efficientFrame = Frame(notebook)
        efficientFrame.pack()
        
        subTitleLabel = Label(efficientFrame,text="\nEfficient",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=1)

        descriptionLabel = Label(efficientFrame,text="Efficient houses are usually built once the player has a few resources and are usually more permanent than nomadic shelters. They are also more structurally sound and look better.\n",justify="center",wraplength=400)
        descriptionLabel.grid(row=2,column=1,sticky="n")

        #---TREE HOUSE---#
        houseLabel = Label(efficientFrame,text="Tree House",font="TkHeadingFont")
        houseLabel.grid(row=3,column=1)

        frame4 = Frame(efficientFrame)

        textbox4 = Text(frame4,bd=1,width=50,height=9,wrap="word")
        textbox4.pack(side=LEFT,fill=Y)

        scrollbar4 = Scrollbar(frame4)
        scrollbar4.pack(side=RIGHT,fill=Y)
        scrollbar4.config(command=textbox4.yview)

        textbox4.insert(END,"Tree houses are nice because they are already in a decently safe position, and they look nice when constructed well, even if the builder had a very limited number of resources. To build one, make a flat surface on the top of a tree and cover it with any material besides sand or gravel for the base. Then put walls and a roof over the base. To finish, place either stairs leading up to it, or for a more safe option, place ladders on the trunk and create an opening in the floor where you can enter through the ladders.")
        textbox4.config(state="disabled")
        textbox4.config(yscrollcommand=scrollbar4.set)

        frame4.grid(row=4,column=1)

        #---CAMO HOUSE---#
        houseLabel = Label(efficientFrame,text="Camouflaged House",font="TkHeadingFont")
        houseLabel.grid(row=5,column=1)

        frame5 = Frame(efficientFrame)

        textbox5 = Text(frame5,bd=1,width=50,height=9,wrap="word")
        textbox5.pack(side=LEFT,fill=Y)

        scrollbar5 = Scrollbar(frame5)
        scrollbar5.pack(side=RIGHT,fill=Y)
        scrollbar5.config(command=textbox5.yview)

        textbox5.insert(END,"Camouflaged houses often require the player to be picky with how the outside looks and where it is built, as if it is built incorrectly, or in a bad area, it isn't camouflaged at all, and is quite obvious to passers-by. This home is perfect for people who are building on a PvP or survival server, because it allows you to be well hidden from other players. A recommendation to be fully secure is to always sneak while in your house, which also means make it as compact as possible. To build this house, find a place where shapes of land are not easily defined (hills and forests can work well, but jungles are perfect). Then build a house (preferably out of dirt) that flows with the land. This may require terraforming to some extent to make it look like part of the landscape. Then, place a door in a hidden spot and live inside.")
        textbox5.config(state="disabled")
        textbox5.config(yscrollcommand=scrollbar5.set)

        frame5.grid(row=6,column=1)

        #---STILT HOUSE---#
        houseLabel = Label(efficientFrame,text="Stilt House",font="TkHeadingFont")
        houseLabel.grid(row=7,column=1)

        frame6 = Frame(efficientFrame)

        textbox6 = Text(frame6,bd=1,width=50,height=9,wrap="word")
        textbox6.pack(side=LEFT,fill=Y)

        scrollbar6 = Scrollbar(frame6)
        scrollbar6.pack(side=RIGHT,fill=Y)
        scrollbar6.config(command=textbox6.yview)

        textbox6.insert(END,"Stilt houses are good because they provide the same protection as tree houses or pillar shelters, but can be used where there are no trees. They can also be used in more hilly terrain where the ground is not flat because the stilts ensure that the foundation is above the ground. To make one, put pillars of a desired height above the ground and then connect them with blocks and fill in the spaces between them, creating the floor. Then add walls and a roof. To access, build stairs or a ladder going up one of the stilts.")
        textbox6.config(state="disabled")
        textbox6.config(yscrollcommand=scrollbar6.set)

        frame6.grid(row=8,column=1)
        
        notebook.add(efficientFrame, text='Efficient')

        #---COMPLEX---#
        complexFrame = Frame(notebook)
        complexFrame.pack()
        
        subTitleLabel = Label(complexFrame,text="\nComplex",font="TkSubHeadingFont")
        subTitleLabel.grid(row=1,column=2)

        descriptionLabel = Label(complexFrame,text="Complex houses are usually built when the player is well-off in a world and has resources to spare. These should not be attempted early on in a game when resources are limited.\n",justify="center",wraplength=400)
        descriptionLabel.grid(row=2,column=2,sticky="n")

        #---ISLAND FORT---#
        houseLabel = Label(complexFrame,text="Island Fortress",font="TkHeadingFont")
        houseLabel.grid(row=3,column=2)

        frame7 = Frame(complexFrame)

        textbox7 = Text(frame7,bd=1,width=50,height=9,wrap="word")
        textbox7.pack(side=LEFT,fill=Y)

        scrollbar7 = Scrollbar(frame7)
        scrollbar7.pack(side=RIGHT,fill=Y)
        scrollbar7.config(command=textbox7.yview)

        textbox7.insert(END,"Perfect for building in the ocean, these houses allow you to see whenever a mob or player approaches, giving ample warning. Build a house with its foundation on the surface of the water. Add walls and a ceiling. Building down to make sub-surface rooms are nice as well, but clearing out the water from underneath can be tiring and difficult. It also ensures that unless a creeper actually gets into your fort, it will not destory anything (because creeper explosions don't do block damage if they are in the water). Oceans are also always flat, so you won't need to worry about your foundation not being level.")
        textbox7.config(state="disabled")
        textbox7.config(yscrollcommand=scrollbar7.set)

        frame7.grid(row=4,column=2)

        #---DEFENSIVE COMPOUND---#
        houseLabel = Label(complexFrame,text="Defensive Compound",font="TkHeadingFont")
        houseLabel.grid(row=5,column=2)

        frame8 = Frame(complexFrame)

        textbox8 = Text(frame8,bd=1,width=50,height=9,wrap="word")
        textbox8.pack(side=LEFT,fill=Y)

        scrollbar8 = Scrollbar(frame8)
        scrollbar8.pack(side=RIGHT,fill=Y)
        scrollbar8.config(command=textbox8.yview)

        textbox8.insert(END,"Defensive compounds are nice because it allows for a small group of people to live together, and easily defend it. To build, construct one central building (to hold all of the goods like iron and gold). Then, build three buildings in such a way that they surround the central building, leaving three narrow openings between the buildings for friendly players to move in and out of the area. Cover the ground between the buildings with a strong block so that people cannot attack from below. This is good for PvP servers. It is highly recommended that you build the buildings out of a strong material such as obsidian. Walls going around the central structure of buildings is recommended as well.")
        textbox8.config(state="disabled")
        textbox8.config(yscrollcommand=scrollbar8.set)

        frame8.grid(row=6,column=2)

        #---NETHER BASE---#
        houseLabel = Label(complexFrame,text="Nether Base",font="TkHeadingFont")
        houseLabel.grid(row=7,column=2)

        frame9 = Frame(complexFrame)

        textbox9 = Text(frame9,bd=1,width=50,height=9,wrap="word")
        textbox9.pack(side=LEFT,fill=Y)

        scrollbar9 = Scrollbar(frame9)
        scrollbar9.pack(side=RIGHT,fill=Y)
        scrollbar9.config(command=textbox9.yview)

        textbox9.insert(END,"Nether Bases are bases that are specifically designed for use in the Nether. When building these, build tall walls around your base that will help to hide you from ghasts when outside of your house. All structures should be made of strong materials. Wood and dirt are not recommended. Obsidian or Cobblestone are best. Make sure you have a stable floor. Create an overhang around your door to prevent ghasts from blowing it up. When building windows, use glass, because ghasts cannot see through glass. A good design feature is to have pistons that can push cobblestone in front of the glass to protect it from Ghast explosions, should a ghast fire at your house. Also, be careful when digging down, as many times, you will unknowingly build your house on a large overhang. You may accidentally dig through it and could fall over 40 blocks to your death, possibly into lava as well.")
        textbox9.config(state="disabled")
        textbox9.config(yscrollcommand=scrollbar9.set)

        frame9.grid(row=8,column=2)
        
        notebook.add(complexFrame, text='Complex')

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=9,column=0,columnspan=3)
    
    def superflatDisp(self):
        window = Toplevel()
        window.title(string="Superflat Survival Tutorial")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')
        
        #TAB SUPPORT#
        notebook = Notebook(window)
        notebook.grid(row=1,column=0)

        titleLabel = Label(window,text="How to Survive in Superflat Mode",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---RAID A VILLAGE---#
        villageFrame = Frame(notebook)
        villageFrame.pack()
        
        subTitleLabel = Label(villageFrame,text="Step 1: Raid a village",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame1 = Frame(villageFrame)

        textbox1 = Text(frame1,bd=1,width=60,height=15,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"To successfully survive in superflat mode, you must first find an NPC village. Do not stop to fight mobs or to dig dirt. Just run until you find an NPC village. It is recommended that you have your render distance as high as possible to increase the chance of finding one. When you find one, check the blacksmith's chest for useful items such as armor, tools, food, and raw materials. Then proceed to take apart a few houses to make tools and collect valuble cobblestone and wood. You will also need to cut a few wheat so that you can get more food (and also breeding power) and seeds to plant for later. Do not kill villagers or iron golems, because you probably don't want to risk fighting them yet. Additionally, you can trade with villagers for valuable items.")
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=1,column=0)
        
        notebook.add(villageFrame, text='Raid a Village')

        #---TACTICS---#
        tacticFrame = Frame(notebook)
        tacticFrame.pack()
        
        subTitleLabel = Label(tacticFrame,text="Step 2: Sedentary or Nomadic Tactics",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame2 = Frame(tacticFrame)

        textbox2 = Text(frame2,bd=1,width=60,height=15,wrap="word")
        textbox2.pack(side=LEFT,fill=Y)

        scrollbar2 = Scrollbar(frame2)
        scrollbar2.pack(side=RIGHT,fill=Y)
        scrollbar2.config(command=textbox2.yview)

        textbox2.insert(END,"Your next step is to choose whether you want to live in the same village you found or whether you want to roam about. If you are saying put, replant your wheat seeds in an NPC wheat farm so that you can get more food, more ability to breed, and also more opportunities to trade with NPCs. Trade with NPCs to get melons, as melons provide another source of food as well as another staple for potion-making. Kill as many slimes as possible for experience and slime balls, another useful potion-making ingredient. Enchant all your tools. You may also want to either make a compass, a breadcrumb trail, or write down the coordinates of your home because you will need to find other NPC villages to take their things as well. If you choose to take a more nomadic approach, then dismantle the NPC village as best you can, focusing on wood and cobblestone. When wandering, find as many NPC villages as possible, following step one and then dismantling them. Once you have enough supplies, try to enchant all of your tools. Regardless of which step you choose, you will want to try to make it into the Nether.")
        textbox2.config(state="disabled")
        textbox2.config(yscrollcommand=scrollbar2.set)

        frame2.grid(row=1,column=0)
        
        notebook.add(tacticFrame, text='Tactics')

        #---NETHER---#
        netherFrame = Frame(notebook)
        netherFrame.pack()
        
        subTitleLabel = Label(netherFrame,text="Step 3: The Nether",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame3 = Frame(netherFrame)

        textbox3 = Text(frame3,bd=1,width=60,height=15,wrap="word")
        textbox3.pack(side=LEFT,fill=Y)

        scrollbar3 = Scrollbar(frame3)
        scrollbar3.pack(side=RIGHT,fill=Y)
        scrollbar3.config(command=textbox3.yview)

        textbox3.insert(END,"Before you explore the nether, make sure you have an iron or diamond sword and a full suit of iron armor. You can get flint from the gravel paths of NPC villages for a flint and steel as well as arrows (if you find chickens). When you are in the nether, be sure to collect lava (for dealing with slimes and making a cobblestone genererator), netherrack (as another building material), and any other resources you may find (netherwart and glowstone are good examples). Note that the End cannot be reached, so do not attempt for it.")
        textbox3.config(state="disabled")
        textbox3.config(yscrollcommand=scrollbar3.set)

        frame3.grid(row=1,column=0)
        
        notebook.add(netherFrame, text='Nether')

        #---TIPS---#
        tipFrame = Frame(notebook)
        tipFrame.pack()
        
        subTitleLabel = Label(tipFrame,text="Tips",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame4 = Frame(tipFrame)

        textbox4 = Text(frame4,bd=1,width=60,height=15,wrap="word")
        textbox4.pack(side=LEFT,fill=Y)

        scrollbar4 = Scrollbar(frame4)
        scrollbar4.pack(side=RIGHT,fill=Y)
        scrollbar4.config(command=textbox4.yview)

        textbox4.insert(END,"There are a few useful points that can greatly increase your chance at surviving in superflat mode. First, collect as much wheat as possible. Besides being a food source, it can be used to trade with NPCs for valuable items and can also breed animals for more food. Second, use the lava from blacksmith's shops to form obsidian and also to create a cobblestone generator. Third, trade with the villagers as much as possible. They can have valuable items that would normally be hard to find. Fourth, You can create pits, cages, and netherrack fences to keep unwanted slimes out. To make a fence that slimes can get in but not out, put alternating blocks of dirt one high, every other block around the area that you will trap slimes in. Dig a hole inside to ensure that they don't get out. To make a nethrrack fence, simply put netherrack around the perimeter of the protected area and light it on fire. Just be sure that NPCs dont wander into it.")
        textbox4.config(state="disabled")
        textbox4.config(yscrollcommand=scrollbar4.set)

        frame4.grid(row=1,column=0)
        
        notebook.add(tipFrame, text='Tips')

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=2,column=0)

    def nomadDisp(self):
        window = Toplevel()
        window.title(string="Nomadic Experience Tutorial")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')
        
        #TAB SUPPORT#
        notebook = Notebook(window)
        notebook.grid(row=1,column=0)

        titleLabel = Label(window,text="How to Survive as a Nomad",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---RULES---#
        rulesFrame = Frame(notebook)
        rulesFrame.pack()
        
        subTitleLabel = Label(rulesFrame,text="Step 1: Know the Rules",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame1 = Frame(rulesFrame)

        textbox1 = Text(frame1,bd=1,width=60,height=15,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"First a few rules of how to be a nomad. These are general rules you MUST follow if you are to have a true 'nomadic experience'.\n1) Keep Moving\n2) Keep game on hard or hardcore mode\n3) Only build shelters for 1 night\n4)Don't stay in any area for longer than 1 night\nThese rules are essential because without them, you would be cheating and not getting the full experience.")
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=1,column=0)
        
        notebook.add(rulesFrame, text='Rules')

        #---SHELTER---#
        shelterFrame = Frame(notebook)
        shelterFrame.pack()
        
        subTitleLabel = Label(shelterFrame,text="Step 2: Building a shelter",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame2 = Frame(shelterFrame)

        textbox2 = Text(frame2,bd=1,width=60,height=15,wrap="word")
        textbox2.pack(side=LEFT,fill=Y)

        scrollbar2 = Scrollbar(frame2)
        scrollbar2.pack(side=RIGHT,fill=Y)
        scrollbar2.config(command=textbox2.yview)

        textbox2.insert(END,"Building a shelter for the night is one of the most important things you will be doing, as fighting mobs all night will deplete your food and your health. You will need to save your food as much as possible, so wasting it while fighting monsters unnecessarily is a bad idea. To build a shelter, don't go for something big and fancy. Use basic, renewable resources that can be cleared in the morning efficiently, such as dirt. You may want to think about either building a hut, an emergency shelter or a pillar shelter. Do not bother on furnishing your house with such things as chests and windows or paintings as you will only be staying there one night and then never seeing it again. The most important thing you do need, however, is a bed. Not to reset a spawn, but to skip the night and avoid pesky mobs that could attack you. Also, don't waste materials on a door. Simply fill the wall with dirt. Just make sure you have a clock on you so that you can tell the time if you don't have a bed.")
        textbox2.config(state="disabled")
        textbox2.config(yscrollcommand=scrollbar2.set)

        frame2.grid(row=1,column=0)
        
        notebook.add(shelterFrame, text='Shelter')

        #---INVENTORY---#
        inventoryFrame = Frame(notebook)
        inventoryFrame.pack()
        
        subTitleLabel = Label(inventoryFrame,text="Step 3: Inventory Management",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame3 = Frame(inventoryFrame)

        textbox3 = Text(frame3,bd=1,width=60,height=15,wrap="word")
        textbox3.pack(side=LEFT,fill=Y)

        scrollbar3 = Scrollbar(frame3)
        scrollbar3.pack(side=RIGHT,fill=Y)
        scrollbar3.config(command=textbox3.yview)

        textbox3.insert(END,"At some point during your journeys, you may suddenly realize that you have run out of inventory space. There are many ways you can deal with this. If you are reasonably far in the game, you may wish to create an ender chest, as digging the chest does not drop the items you placed inside, making it a nice carrying case, sort of like a suitcase. Other things you may want to consider are stacking efficiently. Make sure all items are stacked to their stack limit. Also remember that certain items can be condensed. For instance, if you have iron ingots, you can condense them by creating iron blocks, and when you need iron, uncraft the iron block into ingots again. This allows you to hold nine times as many ingots in one slot as you normally would be able to. This works for gold and diamonds as well. Another thing you may want to think about is only having what you need. For instance, you may not need to carry around an excess of dirt, wood, or cobblestone with you because you can find these quite often. Finally, only craft what you need. Crafting an entire stack of planks so you can make a few torches only takes up more inventory space. Only craft what you need, and try not to have extra materials left over afterwards.")
        textbox3.config(state="disabled")
        textbox3.config(yscrollcommand=scrollbar3.set)

        frame3.grid(row=1,column=0)
        
        notebook.add(inventoryFrame, text='Inventory')

        #---SURVIVING---#
        survivalFrame = Frame(notebook)
        survivalFrame.pack()
        
        subTitleLabel = Label(survivalFrame,text="Step 4: Surviving",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame4 = Frame(survivalFrame)

        textbox4 = Text(frame4,bd=1,width=60,height=15,wrap="word")
        textbox4.pack(side=LEFT,fill=Y)

        scrollbar4 = Scrollbar(frame4)
        scrollbar4.pack(side=RIGHT,fill=Y)
        scrollbar4.config(command=textbox4.yview)

        textbox4.insert(END,"Surviving as a nomad can be much harder than being sedentary because of the constant need to travel. You cannot rely on basic food sources, such as wheat farms or melon farms. Any essential resources, such as iron, can be hard to come by since you probably won't spend that much time in cave systems, due to your wandering tactics. It is essential that you have enough food, as you need to survive. You can do this by fishing in lakes or rivers you come across, or by killing animals for the food they drop. You may wish to be more efficient at this by lighting them on fire and killing them while on fire (this drops the cooked version of the meat instead of the raw version). This allows you to conserve fuel and time, as well as giving you better food (cooked food supplies more hunger bars than raw). Because it takes longer to get important resources, it may be considerably longer before you are ready to go into the nether or into the end. Just remember that these are your ultimate goals.")
        textbox4.config(state="disabled")
        textbox4.config(yscrollcommand=scrollbar4.set)

        frame4.grid(row=1,column=0)
        
        notebook.add(survivalFrame, text='Surviving')

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=2,column=0)

    def netherSurvivalDisp(self):
        window = Toplevel()
        window.title(string="Nether Survival Tutorial")
        window.resizable(False, False)
        window.iconbitmap('icon.ico')
        
        #TAB SUPPORT#
        notebook = Notebook(window)
        notebook.grid(row=1,column=0)

        titleLabel = Label(window,text="How to Survive in the Nether",font="TkHeadingFont", relief="solid")
        titleLabel.grid(row=0,column=0)

        #---PREPARE---#
        prepareFrame = Frame(notebook)
        prepareFrame.pack()
        subTitleLabel = Label(prepareFrame,text="Step 1: Preparing for the Nether",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame1 = Frame(prepareFrame)

        textbox1 = Text(frame1,bd=1,width=60,height=15,wrap="word")
        textbox1.pack(side=LEFT,fill=Y)

        scrollbar1 = Scrollbar(frame1)
        scrollbar1.pack(side=RIGHT,fill=Y)
        scrollbar1.config(command=textbox1.yview)

        textbox1.insert(END,"Many people, while in their travels, opt to spend an extended period of time in the nether, rather than just brief visits whenever something is required. While this can be an exciting challenge, it can be very difficult as well. Many important resources cannot be found in the nether, such as wood and iron. As such, it is important to make sure you are prepared. The first step is to ensure you have enough supplies for your house in the nether. Although Ghasts cannot destroy nether portals, they can deactivate them, which can cause problems for you when you wish to get out. Building your base out of cobblestone is highly recommended, as Ghasts cannot easily destroy it. Other useful tools to bring would be pickaxes, shovels, and a flint and steel (or fire charges). Make sure you bring a lot of food. Bread or melons are best, but if you have bowls, you can easily craft mushroom stew, since mushrooms are abundant in the nether. Remember to bring torches to mark your paths. Using breadcumb trails to do this is highly recommended. Also, don't forget to bring a sword, a bow, and plenty of arrows. A full suit of iron armor is recommended, as well.")
        textbox1.config(state="disabled")
        textbox1.config(yscrollcommand=scrollbar1.set)

        frame1.grid(row=1,column=0)
        
        notebook.add(prepareFrame, text='Prepare')

        #---ENTER---#
        enterFrame = Frame(notebook)
        enterFrame.pack()
        
        subTitleLabel = Label(enterFrame,text="Step 2: Entering the Nether",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame2 = Frame(enterFrame)

        textbox2 = Text(frame2,bd=1,width=60,height=15,wrap="word")
        textbox2.pack(side=LEFT,fill=Y)

        scrollbar2 = Scrollbar(frame2)
        scrollbar2.pack(side=RIGHT,fill=Y)
        scrollbar2.config(command=textbox2.yview)

        textbox2.insert(END,"The nether has incredible structures. High arching cielings, vast lava lakes with fiery lavafalls pouring in them, and more. Don't get too caught up in the scenery, however, as you could easily fall to your death or get attacked by one of the various hostile mobs found here. Your first step in the nether will be to create a house to live in. Do NOT try to sleep in a bed. It will just explode and kill you. Seriously. After building your shelter, you may wish to build walls around it. You should furnish it with chests to save things you collect while in the nether, or to keep valuables from the overworld safe.")
        textbox2.config(state="disabled")
        textbox2.config(yscrollcommand=scrollbar2.set)

        frame2.grid(row=1,column=0)
        
        notebook.add(enterFrame, text='Enter')

        #---EXPLORE---#
        exploreFrame = Frame(notebook)
        exploreFrame.pack()
        
        subTitleLabel = Label(exploreFrame,text="Step 3: Exploring the Nether",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame3 = Frame(exploreFrame)

        textbox3 = Text(frame3,bd=1,width=60,height=15,wrap="word")
        textbox3.pack(side=LEFT,fill=Y)

        scrollbar3 = Scrollbar(frame3)
        scrollbar3.pack(side=RIGHT,fill=Y)
        scrollbar3.config(command=textbox3.yview)

        textbox3.insert(END,"When exploring the nether, remember a few important things. First, hostile mobs can spawn anywhere, at any time. Always be on your guard and prepared to fight. Second, Do not try to use standard navigation equiptment. Compasses will spin wildly, and the day/night cycle means nothing in the nether. As such, beds are useless (they explode). Maps are relatively useless as well, because they cannot accurately chart out all of the caverns and terrain found in the nether. Finally, build a base. This is the most important thing you can do, as it is the only place you can be truly safe from mobs. Make sure you build one out of cobblestone or stone bricks.")
        textbox3.config(state="disabled")
        textbox3.config(yscrollcommand=scrollbar3.set)

        frame3.grid(row=1,column=0)
        
        notebook.add(exploreFrame, text='Explore')

        #---POSSIBILITIES---#
        possibilitiesFrame = Frame(notebook)
        possibilitiesFrame.pack()
        
        subTitleLabel = Label(possibilitiesFrame,text="Step 4: Knowing your Possibilities",font="TkSubHeadingFont")
        subTitleLabel.grid(row=0,column=0)

        frame4 = Frame(possibilitiesFrame)

        textbox4 = Text(frame4,bd=1,width=60,height=15,wrap="word")
        textbox4.pack(side=LEFT,fill=Y)

        scrollbar4 = Scrollbar(frame4)
        scrollbar4.pack(side=RIGHT,fill=Y)
        scrollbar4.config(command=textbox4.yview)

        textbox4.insert(END,"The key to surviving in the nether is to understand the system of resources and utilizing the nether to its fullest extent. First, water cannot be placed in the nether. It simply dissolves. Second, nether bricks, nether brick stairs, and nether brick fences are resistant to ghasts' fireballs, so using them as protection against ghasts is a good idea. Third, netherrack, once lit on fire, will stay lit until put out. This makes it useful for quick light. Third, useful drops include blaze rods (from blazes), gunpowder and ghast tears (from ghasts), magma cream (from magma cubes), and rotten flesh and golden nuggets, as well as occasional golden swords and helmets (from zombie pigmen). Nether Wart and mushrooms are also located in the nether.")
        textbox4.config(state="disabled")
        textbox4.config(yscrollcommand=scrollbar4.set)

        frame4.grid(row=1,column=0)
        
        notebook.add(possibilitiesFrame, text='Possibilities')

        #---CLOSE BUTTON---#
        closeButton = Button(window,text="Close",command=window.destroy)
        closeButton.grid(row=5,column=0,columnspan=2)
