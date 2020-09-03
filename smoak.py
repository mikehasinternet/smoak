pos = 100
go = None
do = None
string = None
line = None

#script
msg_help = "You can travel \"north\" (n), \"south\" (s), \"east\" (e), or \"west\" (w). You can also \"look\" (l) to repeat the description of the area. You can attempt to \"take\" items to add them to your inventory or \"investigate\" items for more information. You can see the items you have on hand with \"inventory\" (i) and can \"use\" items to perform an action. Quit the game with \"quit\" (q). Type \"help\" (?) to show this message again.\nWhat would you like to do?"
msg_death = "*** YOU HAVE DIED ***\nDon't feel too bad, it's probably just because you suck."
pnotN = "You can't go north from here,"
pnotS = "You can't go south from here,"
pnotE = "You can't go east from here,"
pnotW = "You can't go west from here,"
ptrees1 = "The trees are too thick to the"
ptrees2 = "You are unable to penatrate the forest in that direction."
pcliff1 = "There is a tall cliff to your"
pcliff2 = "The face of the rock is too steep to attempt to climb."

p100 = "CLEARING\nYou're on the south side of a clearing. The sky is overcast, but bright. It seems to be the middle of the day. The trees that surround you are tall, ancient oak trees, and there is a much younger-looking birch tree in the middle of the clearing. Next to it, you can see what appears to be a concrete box with a metal door bearing an inscription."
p100_01 = "As you investigate the box, you realize it is retrofitted with a number pad. The inscription has no text, but contains three symbols. The first appears to be a tulip, the second, waves of water, and the third, the tip of a fountain pen. Under each symbol is a pair of zeroes."

p101 = "FOOTPATH\nYou are at the end of a small footpath. The path leads uphill to the west. To the east, there is a small clearing with a birch tree and a concrete box in the center."

p102 = "HILLTOP\nYou have reached the top of a hill. You can see a river to the north, and a path leading east. There is a cliff face to the west. There is a picnic table here, with a tall grey cylinder in the center."
p102_01 = "As you approach the table, you realize that the cylinder is hollow and made of concrete. There is an inscription on the side."
p102_02 = "The inscription is in a language you recognize. It reads: \"This stone vase is to commemorate the twenty seven flowers that were exchanged as a peace offering between the Weh'amu people and Alhuva settlers in Year Fourteen of the Discovery Age.\""
p102_03 = "You attempt to remove the object to no avail. It appears to be bolted to the table."
p102_04 =  "The picnic table is far to heavy too move."

p103 = "RIVER\nYou arrive at the foot of a bridge that proceeds to the north. The structure is decrepit, and looks rather old. The majority of the planks have rotted out, leaving only a rusted skeleton of handrails and substructure. The bridge crosses a river that emerges from a cave in the rock face to the west. The river runs east, and you can see it curve north before plunging down a cliff."
p104 = "BRIDGE\nYou are on the south end of the bridge. There seem to be fewer and fewer places to step. As the water rushes below you, your instincts tell you to turn back."
p104_01 = "You proceed north along what's left of the bridge. Suddenly, you hear a loud creaking sound as the metal frame twists and collapses under your weight. As you fall into the river, something large and heavy collides with your head and your vision goes dark.",msg_death

p105 = "BEND\nYou are at the bend in a river. You can see a vertical post a few feet from the shore, sticking straight out of the river. There is a heavy piece of cloth caught around it. There is a firepit here, and a pile of long branches on the ground next to it. The river flows from the west, and curves north to a cliff. You can hear the falls rushing northward."
p105_01 = "You can't reach the cloth from here. Perhaps if you had a long object to help you reach it..."
p105_02 = "You take a single branch. You consider taking the entire stack, but realize that would be an impractical use of energy."
p105_03 = "You manuever the branch to catch the cloth. Just as you successsfully force the cloth around the stick, the river takes it under and whisks it away. On the post, you can see an inscription: \"PARSEC 73\""

p106 = "FALLS\nYou are at the top of a waterfall. Nothing much here."

p107 = "EAST FOREST\nYou are in a dense forest. There appears to be a clearing to the south. You can hear water rushing to the north. To the east, you see the stump of what was seemingly once a massive tree. On the stump is a small grey object."
p107_01 = "You look closely at the object and you recognize it to be an inkwell. Unlike other inkwells you have used in the past, this one is made of solid concrete and bears an inscription. It reads: Here, Xivian penned the famous thirty two words that made their way to the Monarch and became the start of a new Age of Discovery."
p107_02 = "You attempt to remove the object to no avail. It appears to be bolted to the stump."

p108 ="WEST FOREST\nYou are in a dense forest. It continues to get darker in every direction except east."

#intro
print("                                     Welcome to... \n\n                                               `` ~ __: S M O A K :__~``\n\n" + p100 + "\n\n" + msg_help)


while True:
    userInput = input('\n> ')
    line = (userInput.casefold())
#game controls
    if line == '/pos':
        print(pos)
        continue
    if line == '/do':
        print(do)
        continue
    if line == 'investigate':
        do = 'invg'
        continue
    if line in ['n', 'north']:
        do = 'n'
    if line in ['s', 'south']:
        do = 's'
    if line in ['e', 'east']:
        do = 'e'
    if line in ['w', 'west']:
        do = 'w'
    if line in ['l', 'look']:
        do = 'l'
#exit control
    if line in ['quit','q']:
        exit = input ("Are you sure you want to quit? Y/N\n> ")
        if exit == "y":
            print('Goodbye!')
            quit()
        elif exit == "n":
            line = None
            print('What would you like to do?')
            continue
        else:
            print('Command not recognized.\nWhat would you like to do?')
            continue
    if line == "wq":
        print("Force quit.")
        quit()
##########
#clearing
    if pos == 100:
        if do == 'l':
            print(p100)
        if do == 'n':
            print(pnotN + "there's a birch tree in your way.")
            continue
        if do == 's' :
            print(ptrees1,"south.",ptrees2)
            continue
        if do == 'e' :
            print(ptrees1,"east.",ptrees2)
            continue
        if do == 'w':
            pos = 101
            print(p101)
            continue
        if do == 'invg':
                pos = 100.01
                print(p100_01)
                continue
        continue
##########
#path
    if pos == 101:
        if do == 'l':
            print(p101)
        if do == 'n':
            print(ptrees1,"north.",ptrees2)
            continue
        if do == 's' :
            print(ptrees1,"south.",ptrees2)
            continue
        if do == 'e' :
            print(p101)
            pos = 100
            continue
        if do == 'w':
            print("You follow the path as it winds to the west. As you continue along the path, you notice it begins to incline upward.\n\n" + p102)
            pos = 102
            continue
##########
#hilltop
    if pos == 102:
        if do == 'l':
            print(p102)
        if do == 'n':
            print(p103)
            pos = 103
            continue
        if do == 's' :
            print(ptrees1,"south.",ptrees2)
#            pos = 100
            continue
        if do == 'e' :
            print(p101)
            pos = 101
            continue
        if do == 'w':
            print(p108)
            pos = 108
            continue
##########
#west forest
    if pos == 108:
        if do == 'l':
            print(p108)
        if do == 'n':
            print(ptrees1,"north.",ptrees2)
#            pos = 103
            continue
        if do == 's' :
            print(ptrees1,"south.",ptrees2)
#            pos = 100
            continue
        if do == 'e' :
            print(p102)
            pos = 102
            continue
        if do == 'w':
            print(ptrees1,"west.",ptrees2)
#            pos = 100
            continue
##########
#river
    if pos == 103:
        if do == 'l':
            print(p103)
        if do == 'n':
            print(p104)
            pos = 104
            continue
        if do == 's' :
            print(p108)
            pos = 108
            continue
        if do == 'e' :
            print(p105)
            pos = 105
            continue
        if do == 'w':
            print(pcliff1,"west.",pcliff2)
#            pos = 100
            continue
##########
#bridge
    if pos == 104:
        if do == 'l':
            print(p104)
        if do == 'n':
            print(msg_death)
#            pos = 100
            continue
        if do == 's' :
            print(p103)
            pos = 103
            continue
        if do == 'e' :
            print("The bridge is narrow, you are unable to travel perpendicular to it.")
#            pos = 100
            continue
        if do == 'w':
            print("The bridge is narrow, you are unable to travel perpendicular to it.")
#            pos = 100
            continue
##########
#bend
    if pos == 105:
        if do == 'l':
            print(p105)
        if do == 'n':
            print("This room has not been written yet!")
#            pos = 100
            continue
        if do == 's' :
            print("This room has not been written yet!")
#            pos = 100
            continue
        if do == 'e' :
            print("This room has not been written yet!")
#            pos = 100
            continue
        if do == 'w':
            print("This room has not been written yet!")
#            pos = 100
            continue
##########
#falls
    if pos == 106:
        if do == 'l':
            print(p106)
        if do == 'n':
            print("This room has not been written yet!")
#            pos = 100
            continue
        if do == 's' :
            print("This room has not been written yet!")
#            pos = 100
            continue
        if do == 'e' :
            print("This room has not been written yet!")
#            pos = 100
            continue
        if do == 'w':
            print("This room has not been written yet!")
#            pos = 100
            continue
##########
#east forest
    if pos == 107:
        if do == 'l':
            print(p107)
        if do == 'n':
            print("This room has not been written yet!")
#            pos = 100
            continue
        if do == 's' :
            print("This room has not been written yet!")
#            pos = 100
            continue
        if do == 'e' :
            print("This room has not been written yet!")
#            pos = 100
            continue
        if do == 'w':
            print("This room has not been written yet!")
#            pos = 100
            continue

##########
#error resolution
    else:
        print('Command not recognized!')
        continue




# while pos == 102:
#     if
#         if line  'l':
#             print("You're on the south side of a clearing. The sky is overcast, but bright. It seems to be the middle of the day. The trees that surround you are tall, ancient oak trees, and there is a much younger-looking birch tree in the middle of the clearing. Next to it, you can see what appears to be a small safe bearing an inscription.")
#             continue
#         if line == 's' :
#             print("The trees are too thick to the south. You are unable to penatrate the forest in that direction.")
#             continue
#         if line == 'e' :
#             print("The trees are too thick to the east. You are unable to penatrate the forest in that direction.")
#             continue
#         if line == 'w':
#             print("You're at the end of a small footpath. The path leads uphill to the west. To the east, there is a small clearing with a birch tree in the center.")
#             continue
#         if line == 'n' :
#
#         if line == 'quit':
#             exit = input ("Are you sure you want to quit? Y/N")
#             if exit == "y":
#                 break
#             if exit == "n":
#                 continue
#     else:
#         print("Command not recognized.")
#         continue
