import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# Don't change the code above 

#Write your code below this line
tamano = len(names)

random_integer = random.randint(0,(tamano-1))

print(names[random_integer] + " is going to buy the meal today")


