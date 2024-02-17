import random
# my_list = [[77, 66], [9, 8, [6, 0]], 65.9009, 'AWPDragonLore']

#or item in my_list:
    #print(item)

# sring = "Trali Vali"
 #for s in string
     #print(s)

#number_list = [2, 6, 9, 0, 1]
#print(number_list)

#number_list.append(88)
#print(number_list)

#1 = len(number_list)
#print(1)

random_number_list = []

for i in range(222223):
    n = random.randint(0 ,100)
    random_number_list.append(n)

print(random_number_list)

sum = 0
for i in random_number_list:
    sum += i

for i in random_number_list:
    print('\u2588'*i)

print('Sum = ',sum)

