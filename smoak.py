print("                                     Welcome to... \n\n                                               `` ~ __: S M O A K :__~``\n\n")
print("You're on the south side of a clearing. The sky is overcast, but bright. It seems to be the middle of the day. The trees that surround you are tall, ancient oak trees, and there is a much younger-looking birch tree in the middle of the clearing. Next to it, you can see what appears to be a small safe bearing an inscription.")
pos = 100
go = None
do = None
string = None
line = None

while True:
    userInput = input('> ')
    line = (userInput.casefold())
#game controls
    if line == '/pos':
        print(pos)
        continue
    if line == '/do':
        print(do)
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

#clearing
    if pos == 100:
        if do == 'l':
            print("You're on the south side of a clearing. The sky is overcast, but bright. It seems to be the middle of the day. The trees that surround you are tall, ancient oak trees, and there is a much younger-looking birch tree in the middle of the clearing. Next to it, you can see what appears to be a small safe bearing an inscription.")
        if do == 'n':
            print("You can't go north from here, there's a birch tree in your way.")
            continue
        if do == 's' :
            print("The trees are too thick to the south. You are unable to penetrate the forest in that direction.")
            continue
        if do == 'e' :
            print("The trees are too thick to the east. You are unable to penetrate the forest in that direction.")
            continue
        if do == 'w':
            print("You're at the end of a small footpath. The path leads uphill to the west. To the east, there is a small clearing with a birch tree in the center.")
            pos = 101
            continue
        continue

    if pos == 101:
        if do == 'l':
            print("You're at the end of a small footpath. The path leads uphill to the west. To the east, there is a small clearing with a birch tree in the center.")
        if do == 'n':
            print("The trees are too thick to the north. You are unable to penetrate the forest in that direction.")
            continue
        if do == 's' :
            print("The trees are too thick to the south. You are unable to penetrate the forest in that direction.")
            continue
        if do == 'e' :
            print("You're on the south side of a clearing. The sky is overcast, but bright. It seems to be the middle of the day. The trees that surround you are tall, ancient oak trees, and there is a much younger-looking birch tree in the middle of the clearing. Next to it, you can see what appears to be a small safe bearing an inscription.")
            pos = 100
            continue
        if do == 'w':
            print("You follow the path as it winds to the west. As you continue along the path, you notice it begins to incline upward.")
            pos = 102
            continue
    if pos == 101:

        continue
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
