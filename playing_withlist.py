my_list = ['p', 'r', 'o', 'b', 'e']

print(my_list)

my_list.append('a')

print(my_list)

my_list.extend(['b','c','d'])

print(my_list)

my_list.insert(3,'q')

print(my_list)

my_list.remove('p')
print(my_list)

if 'l' in my_list:
    my_list.remove('l')
    print("that item was deleted from the list")
    print(my_list)
else:
    print("s was not in the list")
    
my_list.pop()
print(my_list)

my_list.pop(1)
print(my_list)

print(my_list.count('b'))

my_list.reverse()
print(my_list)



    
    





