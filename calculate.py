addition = '1. Сложение'
subtraction = '2. Вычитание'
division = '3. Деление'
multiplication = '4. Умножение'
exit_program = '0. Выход из программы'
message_exit = ''
def fold(num1, num2):
    """"Сложение двух переменных"""
    result = num1 + num2
    return result

def subtract(num1,num2):
    """"Вычитание двух переменных"""
    result = num1 - num2
    return result

def divide(num1, num2):
    """"Деление двух переменных"""
    result = num1 / num2
    return result

def multiply(num1,num2):
    """"Умножение двух переменных"""
    result = num1 * num2
    return result

while message_exit != exit_program:
    print("Пожалуйста, выберите операцию:",addition, subtraction, division, multiplication,exit_program, sep='\n')
    selected_operation = int(input())
    if selected_operation == 0:
        break
    else:
        print('Введите первое число: ')
        first_number = float(input())
        print('Введите второе число: ')
        second_number = float(input())
    if selected_operation == 1:
        addition_finish = fold(first_number,second_number)
        print('Ответ:', addition_finish)
    if selected_operation == 2:
        subtraction_finish = fold(first_number, second_number)
        print('Ответ:', subtraction_finish)
    if selected_operation == 3:
        while second_number == 0:
            print("Ошибка! Введите верное число!")
            second_number = float(input())
        division_finish = fold(first_number,second_number)
        print('Ответ:', division_finish)
    if selected_operation == 4:
        multiplication_finish = fold(first_number, second_number)
        print('Ответ:', multiplication_finish)
print('Завершение программы! Будем рады видеть Вас снова!')
