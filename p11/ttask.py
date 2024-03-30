#1
x1 = 77
x2 = 'ТИп данних'
x3 = 14,97
x4 = False
#2
my_tuple = (2, 6,9, 'KOrtEj')
my_spisok = [32, 13, 55, 'СПиСОк']
my_slovnuk = {'x': 'снек', 'VOW': 'HorochO'}


print(my_slovnuk['VOW'])

my_slovnuk['x'] = 834
print(my_slovnuk)


for x in my_spisok:
    print(x)

for y in my_tuple:
    print(y)

for v in my_slovnuk:
    print(my_slovnuk[v])

numbers = (1, 3, 6, 8, 0, 12, 5, 7)

for n in numbers:
    if n % 2 == 0:
        print(n * 2)
    else:
        print(n * 3)
