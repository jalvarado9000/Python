'''
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print("the value of fruit is: " +  fruit)
    
'''
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    
print(student_heights)

total_heights =0
total_number = 0

for total in student_heights:
    total_heights += total
    total_number += 1
    
    
    
print(f"the total heights is: {round ((total_heights)/(total_number))}")
    

