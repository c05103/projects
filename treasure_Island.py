print('''
created by Collin 


88                     88                      88                          
88                     88                      88                          
88                     88                      88                          
88,dPPYba,  ,adPPYYba, 88,dPPYba,  8b       d8 88  ,adPPYba,  8b,dPPYba,   
88P'    "8a ""     `Y8 88P'    "8a `8b     d8' 88 a8"     "8a 88P'   `"8a  
88       d8 ,adPPPPP88 88       d8  `8b   d8'  88 8b       d8 88       88  
88b,   ,a8" 88,    ,88 88b,   ,a8"   `8b,d8'   88 "8a,   ,a8" 88       88  
8Y"Ybbd8"'  `"8bbdP"Y8 8Y"Ybbd8"'      Y88'    88  `"YbbdP"'  88       88  
                                       d8'                                 
                                      d8'                                  


''')

print("Welcome to Babylon")
print("Your mission is to survive to see another day")

first_input = input("You are at a cross roads. Where do you want to go? type 'Left' or 'Right' \n").lower()

if first_input != "left" :
    print("You fell into a hole R.I.P")
elif first_input == "left" :
    sec_input = input("There is an island in the middle of the lake. Type 'wait' to wait for a boat/ type 'swim' to swim across.\n").lower()
    if sec_input != "wait" :
        print("You were attacked by a goldfish and died. R.I.P.")
    elif sec_input == "wait" :
        third_input = input("There are 3 doors. 'Red', 'Blue' , 'pink', choose one.\n").lower()
        if third_input == "red":
            print("You were burnt by fire, RIP.")
        elif third_input == "blue":
            print("You meant you Ex's crazy spouse, they stab you to death. RIP.")
        elif third_input == "pink" :

            forth_input = int(input("well well well, you've come this far. There is a special unicorn sitting at the end of the room. She looks at you asks... what is 5 to the power of 5. :D. Is it '3125' / '3499' / '5844'. \n"))
            if forth_input == 3125 :
                print('''The unicorn stands on its 2 feet, and applaudes you. reaches behind its back and pulls a bottle of bubbly, sprays you with it in glory... but you suddenly wake up in a puddle of pee in your bed. :( why you still peeing your bed. You Win ?? 
                                    \.
     \'.      ;.
      \ '. ,--''-.~-~-'-,
       \,-' ,-.   '.~-~-~~,
     ,-'   (###)    \-~'~=-.
 _,-'       '-'      \=~-"~~',
/o                    \~-""~=-,
\__                    \=-,~"-~,
   """===-----.         \~=-"~-.
               \         \*=~-"
          rs    \         "=====----
                 \
                  \
''')
            elif forth_input != 3125 :
                print ("dumb dumb... go back to school. You scared the unicorn away with your dumb dumbness. Game over !! you lose")
        else : 
            print ("can you not use a keyboard and type? i dont even want you to keep playing. Game over!!!")
            
            
            
            
#End of code 
