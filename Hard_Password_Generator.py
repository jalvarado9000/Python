#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random.seed(874, )
n = random.randint(1,100)
random.seed(n)


total_character = nr_letters + nr_symbols + nr_numbers

letter_acc = " "

l_acc = n_acc = s_acc = 0

 



for l in range(1,total_character+1):
    select = random.randint(1,3)
    if select == 1 and l_acc <= nr_letters :
        random_letters = random.randint(0,47)
        letter_acc += letters[random_letters]
        l_acc += 1
    elif select == 2 and n_acc <= nr_numbers:
        random_numbers = random.randint(0,9)
        letter_acc += numbers[random_numbers]
        n_acc += 1
    elif select == 3 and s_acc <= nr_symbols:
        random_symbols = random.randint(0,8)
        letter_acc += symbols[random_symbols]
        s_acc += 1
    else:
        l -= 1
    
    
print(f"Here is your password: {len(letter_acc)}")
print("password: " + letter_acc)
