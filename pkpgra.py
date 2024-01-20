import sys,time,os
import pyfiglet
import textwrap

os.system('color')
# window title
os.system('title Text game')

#------ GLOBAL VARIABLES ------#
#word speed
words = 0.07
wns = 0.07
chs = 0.01
#linespeed
lines = 0.5
lns = 0.5
#choices
desc = ''
choice1 = '' ; choice2 = '' ; choice3 = '' ; choice4 = '' ; choice5 = ''
namec = '\33[47m'+'\33[30m'
authorc = '\33[42m'+'\33[30m'
#color end
cend = '\033[0m'+'\x1b[0m'
#choice box
chbox  = '\33[36m'
#chat background
chatb = '\33[30m'+'\33[46m'
#colors
red = '\033[91m'
green = '\33[92m'
yellow = '\33[33m'
yellowb = '\33[43m'+'\33[30m'
grey = '\33[100m'
bold = '\33[1m'
#clear console
def line():
    #os.system('cls||clear')
    print('\n'+"@#%" * 40 + '\n')
#letter by letter function
def type(x):
    for char in x:
            sys.stdout.write(char)
            sys.stdout.flush()
            if char !='\n':
                time.sleep(words)
            else:
                time.sleep(lines)
#------ START CUTSCENE ------#
cutscene = 0
# a quick placeholder like cutscene for now
if cutscene == 1:
    os.system('cls||clear')
    time.sleep(1)
    print(grey)
    lines = 0.8
    words = wns
    type('Nie powinno mnie tu być')
    words = 0.5
    type('...\n')
    words = 0.09
    type('Znalazłem się w złym miejscu o złym czasie, ale teraz nie ma powrotu.\n')
    type('Chyba psycha mi siada,\n')
    time.sleep(1)
    words = 0.15
    type('jak ja miałem na imię?')
    words = 0.5
    type('...\n')
    words = 0.07
    lines = 0.5
    print(cend)
    time.sleep(1)
else: os.system('cls||clear')
#------ TITLE SCREEN ------#
line()
lines = chs
words = chs
#good fonts - o8, epic, chunky, nancyj-fancy
title = red+pyfiglet.figlet_format("P K P", font = "o8")
subtitle = pyfiglet.figlet_format("Intercity", font = "chunky")+cend
author = authorc+"RobinBall"+cend
print(title+subtitle)
train = """
   _____                 . . . . . o o o o o
  __|[_]|__ ___________ _______    ____      o
 |[] [] []| [] [] [] [] [_____(__  ][]]_n_n__][.
_|________|_[_________]_[________]_|__|________)<
  oo    oo 'oo      oo ' oo    oo 'oo 0000---oo\_
"""
print(train)
print('Stworzone przez: '+author)
print(yellow)
print('\nZamknięty w bezkresnym stalowym pudle, bez możliwości ucieczki, bez nikogo do pomocy.\nMiała to być tylko krótka podróż do pracy.')
print(cend)
line()

name = input(chbox+'Podaj swoje imię: '+cend)
name = namec+name.capitalize()+cend
os.system('cls||clear')
#------ instructions ------#
line()
print('Używaj terminala z opcją scrollowania i z obsługą kolorów, dla najlepszych wrażeń,')
print('zawsze możesz sprawdzić historie gry poprzez scrollowanie.\n')
print(bold+'KOMENDY:'+cend+yellow+'\neq'+cend+'         otwórz ekwipunek\n')
print(bold+'LEGENDA:'+cend)
print(grey+'szary'+cend+'      przedstawia myśli')
print(green+'green'+cend+'      przedstawia akcje inwentarzu')
print(yellow+'yellow'+cend+'     przedstawia konwersacje')
print(chbox+'cyan'+cend+'       przedstawia systemowe wiadomości')
print("\n" * 1)
line()
#--------------------------#
input(chbox+'Continue... '+cend)
os.system('cls||clear')
#NOT WORKING
#debugMode = 0
#while debugMode == 1:
#   wns = chs
#   lns = chs

#------ inventory system ------#
inv = []
#state option to add item
itemgot = 0
itemname = ''
#------ choice system ------#
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
    else: None
    words = wns
    lines = lns
screen_code = "\033[1A[\033[2K"
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
            else: input(chbox+'\n\nContinue... '+cend)

        elif optionmax >= 2 and (option == '2' or option == choice2):
            choicelist.append(option)
            #print(option)
            type(option2)
            if itemgot == 2 and itemname not in inv:
                inv.append(itemname)
            if len(set(choicelist)) < optionmax:
                choice()
            else: input(chbox+'\n\nContinue... '+cend)

        elif optionmax >= 3 and (option == '3' or option == choice3):
            choicelist.append(option)
            #print(option)
            type(option3)
            if itemgot == 3 and itemname not in inv:
                inv.append(itemname)
            if len(set(choicelist)) < optionmax:
                choice()
            else: input(chbox+'\n\nContinue... '+cend)

        elif optionmax >= 4 and (option == '4' or option == choice4):
            choicelist.append(option)
            #print(option)
            type(option4)
            if itemgot == 4 and itemname not in inv:
                inv.append(itemname)
            if len(set(choicelist)) < optionmax:
                choice()
            else: input(chbox+'\n\nContinue... '+cend)

        elif optionmax >= 5 and (option == '5' or option == choice5):
            choicelist.append(option)
            #print(option)
            type(option5)
            if itemgot == 5 and itemname not in inv:
                inv.append(itemname)
            if len(set(choicelist)) < optionmax:
                choice()
            else: input(chbox+'\n\nContinue... '+cend)

        #------ commands ------#
        elif option == 'inventory' or option == 'eq' or option == 'inwentarz':
            print(namec+green+'\n  Inventory:'+cend)
            if len(inv) > 0:
                for item in inv:
                    type(green+'  '+item+cend)
            else:
                type(green+'  no items'+cend)
            if len(set(choicelist)) < optionmax:
                choice()
            else: input(chbox+'\n\nContinue... '+cend)
        #----------------------#
        else:
            type(chbox+'  there is no such option nor a command'+cend)
            #check if all options chosen
            if len(set(choicelist)) < optionmax:
                choice()
            else: input(chbox+'\n\nContinue... '+cend)

#------  START OF THE GAME ------#
words = 0.07
lines = 0.5
time.sleep(1)
type('\nThis is a place holder '+name+' be careful bruh\n')
type('Another placeholder here too')
#inventory
itemgot = 1
itemname = 'flashlight'
#choice list, option max number
choicelist = []
optionmax = 3
#description and choices
desc = chatb+'What do you do?'+cend
choice1 = 'get flashlight'
choice2 = 'look to the left'
choice3 = 'look to the right'
#options
option1 = 'got '+green+itemname+cend
option2 = 'you took a look to the left'
option3 = 'you have gazed at the right direction'
choice()
option()
print('\n')
#~~~~~~~~~~~~#
time.sleep(1)
line()
#speaker system
speaker = 'yourmom'
speakerlen = len(speaker) + 2
speaker = yellowb+speaker+':'+cend+' '
type(speaker+yellow+'Here there is another choice\n'+' '*speakerlen+'test of the speaker function'+cend)
#inventory
itemgot = 0
itemname = ''
#choice list, option max number
choicelist = []
optionmax = 4
#description and choices
desc = chatb+'Am I in your house?'+cend
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
#~~~~~~~~~~~~#

input(chbox+'\n\n\n  Exit by pressing enter...   '+cend)
