# 1

name = 'Andrey'
age = 44
progect_name = input('Введите название проекта: ')

print('имя пользователя -', name, 'Название проекта -', progect_name)

# 2
seconds = int(input('Введите время в секундах'))
hours = (seconds / 3600)
minets = (seconds / 60)

print(f'Вы ввели {seconds} секунд - это {hours} часов, {minets} минут, или {seconds} секунд')

# 3

var_n = int(input('Введите число n'))
var_result = (var_n + int(str(var_n) + str(var_n)) + int(str(var_n) + str(var_n) + str(var_n)))
print(f'Зезультат выражения var_n + var_nn + var_nnn равен {var_result}')

# 4

var_integer = int(input('Введите целое положительное число '))
var_max = var_integer % 10
while var_integer >= 1:
    var_integer = var_integer // 10
    if var_integer % 10 > var_max:
        var_max = var_integer % 10
    if var_integer > 9:
        continue
    else:
        print('Максимальное цифра в числе ', var_max)
        break

# 5

var_proceeds = int(input('Введите выручку '))
var_cost = int(input('Введите издержки '))
var_profit = var_proceeds - var_cost

if var_proceeds > var_cost:
    print('Вы работаете с прибылью и рентабильность равна:', (var_profit / var_proceeds) * 100, 'процентов')
    var_workers = int(input('Введите количество работников'))
    print('Прибыль в расчете на одного работника равна:', var_profit / var_workers)
else:
    print('Вы работаете в убыток')

#6

start_kilometres = int(input('Введите сколько километров вы пробегаете в день '))
result_kilometres = int(input('А теперь какого результата вы хотите достичь '))
var_days = 1
while result_kilometres >= start_kilometres:
    start_kilometres = start_kilometres * 1.1
    var_days = var_days + 1
    if start_kilometres > result_kilometres:
        print(f'Вы достигнете желаемого результата на {var_days} день')
        break
