  #  Don't change the code below 
row1 = ["⬜️","⬜","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# Don't change the code above 

#Write your code below this row 
if position[0] == '3':
    if position[1] == '3':
        row3.insert(2,'X')
    
    elif position[1] == '2':
        row3.insert(1,'X')
    
    elif position[1] == '1':
        row3.insert(0,'X')
    

elif position[0] == '2':
    if position[1] == '3':
        row2.insert(2,'X')
    
    elif position[1] == '2':
        row2.insert(1,'X')
    
    elif position[1] == '1':
        row2.insert(0,'X')
        
elif position[0] == '1':
    if position[1] == '3':
        row1.insert(2,'X')
    
    elif position[1] == '2':
        row1.insert(1,'X')
    
    elif position[1] == '1':
        row1.insert(0,'X')
else:
    print(f"{position} is a invalid option")
    





#Write your code above this row 

# Don't change the code below 
print(f"{row1}\n{row2}\n{row3}")