import sys,time,os
import pyfiglet
import textwrap

os.system('color')
# window title
os.system('title Text game')
# textwrap.wrap(type, width=20)

#------ GLOBAL VARIABLES ------#
#word speed
words = 0.05
ns = 0.05
chs = 0.01
#linespeed
lines = 0.5
lns = 0.5
#color red
red = '\033[91m'
#name
namec = '\33[7m'
#color end
cend = '\033[0m'
#choice box
chbox  = '\33[36m'
#chat background
chatb = '\33[104m'
#green
green = '\33[92m'
#clear console
def clear():
    os.system('cls||clear')
    print("\n" * 100)
clear()
#------------------------------#

#------ TITLE SCREEN ------#
#good fonts - o8, epic, chunky, nancyj-fancy
title = red+pyfiglet.figlet_format("P l a c e\nH o l d e r", font = "o8")+cend
author = green+namec+"RobinBall\n"+cend
print(title)
print ('By '+author)
print("\n" * 10)
#--------------------------#

#letter by letter function
def type(x):
    for char in x:
            sys.stdout.write(char)
            sys.stdout.flush()
            if char !='\n':
                time.sleep(words)
            else:
                time.sleep(lines)


#NOT WORKING
#debugMode = 0
#while debugMode == 1:
#   ns = chs
#   lns = chs

#------  START OF THE GAME ------#

#------ inventory system ------#
inv = []
itemgot = 0
itemname = ''
#------------------------------#

#------ choice system ------#
choice1 = 'a'
choice2 = 'a'
choice3 = 'a'
choice4 = 'a'
choice5 = 'a'
def choice():
    global lines, words
    lines = chs
    words = chs
    type(chbox+'\n\n  '+desc+'\n')
    if optionmax == 1:
        type('  1. ' + choice1 + '\n' + cend)
    elif optionmax == 2:
        type('  1. ' + choice1 + '\n  2. ' + choice2 + '\n\n' + cend)
    elif optionmax == 3:
        type('  1. ' + choice1 + '\n  2. ' + choice2 + '\n  3. ' + choice3 + '\n\n' + cend)
    elif optionmax == 4:
        type('  1. ' + choice1 + '\n  2. ' + choice2 + '\n  3. ' + choice3 + '\n  4. ' + choice4 + '\n\n' + cend)
    elif optionmax == 5:
        type('  1. ' + choice1 + '\n  2. ' + choice2 + '\n  3. ' + choice3 + '\n  4. ' + choice4 + '\n  5. ' + choice5 + '\n\n' + cend)
    else:
        None
    words = ns
    lines = lns
screen_code = "\033[1A[\033[2K"
#---------------------------#

#------ option system ------#
def option():
    while len(set(choicelist)) < optionmax:
        option = input('  ').lower()

        if optionmax >= 1 and (option == '1' or option == choice1):
            choicelist.append(option)
            #print(option)
            type(option1)
            if itemgot == 1 and itemname not in inv:
                inv.append(itemname)
            if len(set(choicelist)) < optionmax:
                choice()

        elif optionmax >= 2 and (option == '2' or option == choice2):
            choicelist.append(option)
            #print(option)
            type(option2)
            if itemgot == 2 and itemname not in inv:
                inv.append(itemname)
            if len(set(choicelist)) < optionmax:
                choice()

        elif optionmax >= 3 and (option == '3' or option == choice3):
            choicelist.append(option)
            #print(option)
            type(option3)
            if itemgot == 3 and itemname not in inv:
                inv.append(itemname)
            if len(set(choicelist)) < optionmax:
                choice()

        elif optionmax >= 4 and (option == '4' or option == choice4):
            choicelist.append(option)
            #print(option)
            type(option4)
            if itemgot == 4 and itemname not in inv:
                inv.append(itemname)
            if len(set(choicelist)) < optionmax:
                choice()

        elif optionmax >= 5 and (option == '5' or option == choice5):
            choicelist.append(option)
            #print(option)
            type(option5)
            if itemgot == 5 and itemname not in inv:
                inv.append(itemname)
            if len(set(choicelist)) < optionmax:
                choice()

        #------ commands ------#
        elif option == 'inventory' or option == 'inv' or option == 'i':
            print(namec+green+'\n  Inventory:'+cend)
            for item in inv:
                type(green+'  '+item+cend)
            if len(set(choicelist)) < optionmax:
                choice()
        #----------------------#
        else:
            type(chbox+'  there is no such option nor a command'+cend)

            #check if all options chosen
            if len(set(choicelist)) < optionmax:
                choice()
#---------------------------#

print(chbox+'  Enter you name:\n'+cend)
name = input('  ')
name = namec+name.capitalize()+cend

type('This is a place holder '+name+' be careful bruh\n')

type('Another placeholder here too')
#inventory
itemgot = 1
itemname = 'flashlight'
#choice list, option max number
choicelist = []
optionmax = 3
#description and choices
desc = 'What do you do?'
choice1 = 'get flashlight'
choice2 = 'look to the left'
choice3 = 'look to the right'
#options
option1 = 'got '+green+'flashlight'+cend
option2 = 'you took a look to the left'
option3 = 'you have gazed at the right direction'
choice()
option()
print('\n')

type('here there is another choice')
#inventory
itemgot = 0
itemname = ''
#choice list, option max number
choicelist = []
optionmax = 4
#description and choices
desc = 'Am I in your house?'
choice1 = 'yes'
choice2 = 'no'
choice3 = '*youre'
choice4 = 'youre mom'
#options
option1 = 'indeed'
option2 = 'look behind you'
option3 = 'bruh'
option4 = 'oh god'
choice()
option()
print('\n')

input(chbox+'\n\n\n  Exit by pressing enter...   '+cend)
