# Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

#Write your code below this line
#TRUE LOVE

low_name1 = name1.lower()
low_name2 = name2.lower()

T_count_name1 = low_name1.count("t")
R_count_name1 = low_name1.count("r")
U_count_name1 = low_name1.count("u")
E_count_name1 = low_name1.count("e")

T_count_name2 = low_name2.count("t")
R_count_name2 = low_name2.count("r")
U_count_name2 = low_name2.count("u")
E_count_name2 = low_name2.count("e")

true1_total = T_count_name1 + R_count_name1 + U_count_name1 + E_count_name1
true2_total = T_count_name2 + R_count_name2 + U_count_name2 + E_count_name2

Final_True_total = str(true1_total + true2_total)

L_count_name1 = low_name1.count("l")
O_count_name1 = low_name1.count("o")
V_count_name1 = low_name1.count("v")
E_count_name1 = low_name1.count("e")

L_count_name2 = low_name2.count("l")
O_count_name2 = low_name2.count("o")
V_count_name2 = low_name2.count("v")
E_count_name2 = low_name2.count("e")

love1_total = L_count_name1 + O_count_name1 + V_count_name1 + E_count_name1
love2_total = L_count_name2 + O_count_name2 + V_count_name2 + E_count_name2

Final_Love_total = str(love1_total + love2_total)

print(name1 + " " + name2 + " have a %" + Final_True_total + Final_Love_total + " of finding true love")
  
percent = int(Final_True_total + Final_Love_total)
'''
For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

'''

if (percent < 10) or (percent > 90):
    print(f"Your score is {percent}, you go together like coke and mentos.")
elif percent >= 40 and percent <=50:
    print(f"Your score is {percent}, you are alright together.")   
else:
    print(f"Your score is {percent}.")


