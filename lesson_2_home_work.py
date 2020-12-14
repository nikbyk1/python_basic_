#1

some_list = [1, 2, 3, 'text', 3.7]
for i in some_list:
    print(i, type(i))

#2

some_list = []
list_length = int(input('Сколько элементов будет в списке? Введите число.'))

while list_length > 0:
    some_list.append(input(f'Введите {list_length} элемент списка'))
    list_length -= 1

print(some_list)

n = 0
for i in range(int(len(some_list) / 2)):
    some_list[n], some_list[n + 1] = some_list[n + 1], some_list[n]
    n += 2

print(some_list)

# 3

calendar_list = ['зима', 'весна', 'лето', 'осень']
calendar_dict = {1: 'зима',
                 2: 'весна',
                 3: 'лето',
                 4: 'осенЬ',
                 }

month_number = int(input('Введите номер месяца '))

if month_number == 12 or  month_number == 1 or month_number == 2:
    print(calendar_list[0])
    print(calendar_dict[1])

if month_number == 3 or  month_number == 4 or month_number == 5:
    print(calendar_list[1])
    print(calendar_dict[2])

if month_number == 6 or  month_number == 7 or month_number == 8:
    print(calendar_list[2])
    print(calendar_dict[3])

if month_number == 9 or  month_number == 10 or month_number == 11:
    print(calendar_list[3])
    print(calendar_dict[4])


# 4

user_str = input('Введите строку из нескольких слов')
my_word = []
num = 1
for i in range(user_str.count(' ') + 1):
    my_word = user_str.split()
    if len(str(my_word)) <= 10:
        print(f' {num} {my_word [i]}')
        num += 1
    else:
        print(f' {num} {my_word [i] [0:10]}')
        num += 1

# 5

my_list = [1, 2, 3]
print(f'Рейтинг - {my_list}')
new_number = int(input("Введите число "))
for i in range(len(my_list)):
    if my_list[i] == new_number:
        my_list.insert(i + 1, new_number)
        break
    elif my_list[0] < new_number:
        my_list.insert(0, new_number)
    elif my_list[-1] > new_number:
        my_list.append(new_number)
    elif my_list[i] > new_number and my_list[i + 1] < new_number:
        my_list.insert(i + 1, new_number)
    print(f'Измененный список - {my_list}')
    new_number = int(input("Введите число "))
































