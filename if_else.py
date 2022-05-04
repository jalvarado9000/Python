print("Hi welcome to the ticket booth")
height =int(input("what is your height"))

kid_price = int(5)
teen_price = int(7)
adult_price = int(12)
photo = int(3)

if height  < 120:
    print("Please come back later you are not tall enough")
elif height >= 120:
    print("Thanks, enjoy the ride")
    age = int(input("what is your age?"))
    if age < 12:
        answer = input(f"Do you want a photo for ${photo}?")
        if answer == 'Y':
            kid_price+=photo
        print(f"your ticket is ${kid_price}")
    elif age <= 18:
        answer = input(f"Do you want a photo for ${photo}?")
        if answer == 'Y':
            teen_price+=photo
        print(f"your ticket is ${teen_price}")
    elif age >= 45 and age <= 55:
        adult_price = 0
        print(f"your ticket is ${adult_price}") 
    else:
        answer = input(f"Do you want a photo for ${photo}?")
        if answer == 'Y':
            adult_price+=photo
        print(f"your ticket is ${adult_price}")
else:
    print("invalid option")