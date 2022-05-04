import random
import my_module

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)



random_integer = random.randint(0,1)
print(random_integer)

if random_integer == 1:
    print("Head")
else:
    print("Tail")
'''
random_float = random.random()
print(random_float)

love_score = random.randint(1,100)
print(f'Your love is {love_score}')

'''
