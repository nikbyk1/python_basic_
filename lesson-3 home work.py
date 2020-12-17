# 1

def my_function_div():
    """  функция принимает два числа и выполняет их деление."""
    try:
        var1 = int(input('Введите делимое число'))
        var2 = int(input('Введите делитель'))
    except var2 == 0:
        return
    var_result = var1 / var2
    return var_result

div_result = my_function_div()
print(div_result)

# 2

def user_data():
    """
     функция принимает несколько параметров:
     имя, фамилия, год рождения, город проживания, email, телефон.
     вывод данных о пользователе одной строкой.
    """
    name = input('Введите свое имя')
    second_name = input('Введите фамилию')
    year_of_birht = input('Введите год рождения')
    city = input('Введите город проживания')
    email = input('Введите сой email')
    telephone = input('Введите свой телефон')
    print(f'Пользователь {name} {second_name}, год рождения - {year_of_birht}, город проживания - {city},'
          f'email полльзователя - {email}, телефон - {telephone}.')

user_data()

# 3

def max_sum_func(var_1, var_2, var_3):
    """ функция принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов """
    if var_1 > var_3 and var_2 > var_3:
        return var_1 + var_2
    elif var_1 > var_2 and var_3 > var_2:
        return var_1 + var_3
    elif var_2 > var_1 and var_2 > var_1:
        return var_2 + var_3

print(max_sum_func(10, 20, 30))

# 4

def exponentiation(x, y):
    return x ** abs(y)

print(exponentiation(2, -3))

def exponentiation_1(x, y):
    result = 1
    for _ in range(abs(y)):
        result *= x
    return result
print(exponentiation_1(2, -3))

# 5

def sum_numbers():
    result = 0
    l = True
    while l == True:
        numbers = input('Введите числа которые хотите сложить или "F" чтобы выйти').split()
        sum = 0
        for n in range(len(numbers)):
            if numbers[n] == 'f' or numbers[n] == 'F':
                l = False
                break
            else:
                sum += int(numbers[n])
        result += sum
        print(f'сумма равна - {result}')
    print(f'Финальная сумма равна - {result}')

sum_numbers()

# 6

def function(text):
    return ''.join((text[0].upper(), text[1:]))

print(function('texttttt'))





