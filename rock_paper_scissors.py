#Created by Collin Chimbwanda


import random 




rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#main code 



choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

#list for computer choice 
game = ["r" , "p" , "s"]

#random choice function
ai = random.choice(game)


#declaring the patterns of the choices 

if ai == "r":
    ai = rock 
elif ai == "p":
    ai = paper
elif ai == "s":
    ai = scissors

    
# if function for the game 
    
if choice == 0:
    print(rock)
    print(f"Computer chose: \n{ai}")
    if ai == rock :
        print("Its a tie")
    elif ai == paper :
        print("You lose")
    elif ai == scissors :
        print ("You win")

elif choice == 1:
    print(paper)
    print(f"Computer chose: \n{ai}")
    if ai == rock :
        print("You win")
    elif ai == paper :
        print("Its a tie")
    elif ai == scissors :
        print ("You lose")

elif choice == 2:
    print(scissors)
    print(f"Computer chose: \n{ai}")
    if ai == rock :
        print("You lose")
    elif ai == paper :
        print("You win")
    elif ai == scissors :
        print ("Its a tie")


        
        

#there are definetly numerous ways to complete this task
    
#end of code 






   















