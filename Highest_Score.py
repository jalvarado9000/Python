student_scores = input("Input a list of student heights ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
print(student_scores)

#list = 78 65 89 86 55 91 64 89

total_number = 0
for number in student_scores:
    total_number += 1
    
h_score = 0;
n = 0
for score in student_scores:
    if h_score < student_scores[n]:
        h_score = student_scores[n]
    n+=1
        
print(f"the highest score is: {h_score}")
    