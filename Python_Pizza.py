#Don't change the code below 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Don't change the code above 

#Write your code below this line
small_Pizza = int(15)
medium_Pizza = int(20)
large_Pizza = int(25)

s_Pepperoni = int(2)
ml_Pepperoni = int(3)
Cheese = int(1)

if size == 'S':
    if add_pepperoni == 'Y':
        small_Pizza += s_Pepperoni
        if extra_cheese == 'Y':
            small_Pizza += Cheese
    print(f"Your total for the small pizza is ${small_Pizza}")
elif size == 'M':
    if add_pepperoni == 'Y':
        medium_Pizza += ml_Pepperoni
        if extra_cheese == 'Y':
            medium_Pizza += Cheese
    print(f"Your total for the small pizza is ${medium_Pizza}")
elif size == 'L':
    if add_pepperoni == 'Y':
        large_Pizza += ml_Pepperoni
        if extra_cheese == 'Y':
            medium_Pizza += Cheese
    print(f"Your total for the small pizza is ${large_Pizza}")
else:
    print("Invalid option try again")
            
