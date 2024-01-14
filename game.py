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

#------ TITLE SCREEN ------#
title = red+pyfiglet.figlet_format("P l a c e\nH o l d e r", font = "o8")+cend           # o8, epic, chunky, nancyj-fancy
author = green+namec+"RobinBall\n"+cend
print(title)
print ('By '+author)
print("\n" * 10)

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
# choice system
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
#option system
def option():
    while len(set(choicelist)) < optionmax:
        option = input('  ')

        if optionmax >= 1 and (option == '1' or option == choice1):
            choicelist.append(option)
            #print(option)
            type(option1)
            if len(set(choicelist)) < optionmax:
                choice()

        elif optionmax >= 2 and (option == '2' or option == choice2):
            choicelist.append(option)
            #print(option)
            type(option2)
            if len(set(choicelist)) < optionmax:
                choice()

        elif optionmax >= 3 and (option == '3' or option == choice3):
            choicelist.append(option)
            #print(option)
            type(option3)
            if len(set(choicelist)) < optionmax:
                choice()

        elif optionmax >= 4 and (option == '4' or option == choice4):
            choicelist.append(option)
            #print(option)
            type(option3)
            if len(set(choicelist)) < optionmax:
                choice()

        elif optionmax >= 5 and (option == '5' or option == choice5):
            choicelist.append(option)
            #print(option)
            type(option3)
            if len(set(choicelist)) < optionmax:
                choice()
        else:
            type(chbox+'  there is no such option'+cend)

            #check if all options chosen
            if len(set(choicelist)) < optionmax:
                choice()

print(chbox+'  Enter you name:\n'+cend)
name = input('  ')
name = namec+name.capitalize()+cend

type('This is a place holder '+name+' be careful bruh\n')
type('Another placeholder here too')
#description and choices
desc = 'A'
choice1 = 'a'
choice2 = 'b'
choice3 = 'c'
#options
option1 = 'chose a'
option2 = 'chose b'
option3 = 'chose c'
#choice list, option max number
choicelist = []
optionmax = 3
choice()
option()
print('\n')

type('here there is another choice')
#description and choices
desc = 'B'
choice1 = 'd'
choice2 = 'e'
choice3 = 'f'
choice4 = 'g'
#options
option1 = 'chose d'
option2 = 'chose e'
option3 = 'chose f'
option4 = 'chose g'
#choice list, option max number
choicelist = []
optionmax = 4
choice()
option()
print('\n')

input(chbox+'\n\n\n  Exit by pressing enter...   '+cend)
