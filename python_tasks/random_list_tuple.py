import random

random_list = []
for i in range(0, 5):
    r = random.randint(1, 23)
    random_list.append(r)
print(random_list)
# Next comes another way of realisation
input_value = input("Enter your values")
list = input_value.split()
tuple = tuple(list)
print(tuple, list)
