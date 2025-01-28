addition = '1. Сложение'
subtraction = '2. Вычитание'
division = '3. Деление'
multiplication = '4. Умножение'
print("Пожалуйста, выберите операцию:",addition, subtraction, division, multiplication, sep='\n')
selected_operation = int(input())
print('Введите первое число: ')
first_number = float(input())
print('Введите второе число: ')
second_number = float(input())
if selected_operation == 1:
    addition_finish = first_number + second_number
    print('Ответ:', round(addition_finish))
if selected_operation == 2:
    subtraction_finish = first_number - second_number
    print('Ответ:', round(subtraction_finish))
if selected_operation == 3:
    if second_number != 0:
        division_finish = first_number // second_number
        print('Ответ:', round(division_finish))
    else:
        print('Ошибка, на ноль делить нельзя!')
if selected_operation == 4:
    multiplication_finish = first_number * second_number
    print('Ответ:', round(multiplication_finish))
print('Завершение программы!')
