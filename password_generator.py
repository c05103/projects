#Password Generator Project created by Collin 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))



select = ""
select2 = ""
select3 = ""

#for loop to select the inputted letters 


for i in range (0,nr_letters):
  
  ran = random.choice(letters)
  select += ran


#for loop to select the inputted numbers 
  
for i in range (0,nr_numbers):
  
  ran = random.choice(numbers)
  select2 += ran

#for loop to select the inputted symbols 

for i in range (0,nr_symbols):
  
  ran = random.choice(symbols)
  select3 += ran

# prints the outcome of the password

print(f"{select}{select2}{select3}")



combo = [(select),(select2),(select3)]


#end of code 
#this prints password with the current layout defined in order which for loops runs 






  
