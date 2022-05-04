#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random.seed(8787)


total_character = nr_letters + nr_symbols + nr_numbers
partial_character = nr_letters + nr_numbers
l_acc = n_acc = s_acc = 0


letter_acc = [] 

for l in range(1,total_character+1):
    if l <= nr_letters and l_acc < nr_letters:
        random_letters = random.randint(0,47)
        letter_acc.append(letters[random_letters])
        l_acc += 1 
    elif l <= partial_character and n_acc < nr_numbers:
        random_numbers = random.randint(0,9)
        letter_acc.append(numbers[random_numbers])
        n_acc += 1
    else:
        random_symbols = random.randint(0,8)
        letter_acc.append(symbols[random_symbols])
        
    
    
print(f"Here is your password: {letter_acc}")
random.shuffle(letter_acc)
print(f"Here is your password shuffle : {letter_acc}")

words = " "
for letras in letter_acc:
    words += letras
print(words)

'''
random_letter = random.randint(0,47)
random_number = random.randint(0,9)
random_symbols = random.randint(0,8)
'''
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P