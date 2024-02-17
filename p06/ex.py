import random

random_number_list_1 = []
for i in range(5):
    n = random.randint(0 ,10)
    random_number_list_1.append(n)

print(random_number_list_1)

random_number_list_2 = []
for i in range(5):
    n = random.randint(0 ,10)
    random_number_list_2.append(n)

print(random_number_list_2)

list_3 = []

for i in random_number_list_1:
    if i in random_number_list_2:
        list_3.append(i)

print(list_3)