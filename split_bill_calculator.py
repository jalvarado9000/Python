#build a tip calculator
#ask total of bill,split the bill(ppl), give a porcentage of tip,

print("Welcome to the tip calculator")
total_bill = float(input("What was the total of the bill: "))
print(total_bill)
total_person = int(input("How many people to split the bill?"))
print(total_person)
print("What percentage tip would you like to give?")
total_tip = int(input("10,12,15"))

split_bill = float(total_bill/total_person)
#split_tip = float(total_tip/total_person)
tip = float(total_tip/100)
each_tip = float(split_bill*tip)

each_pay = each_tip + split_bill

print(f"Each Person should Pay {round(each_pay,2)}")


                       