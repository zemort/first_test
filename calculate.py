addition = '1. Сложение'
subtraction = '2. Вычитание'
division = '3. Деление'
multiplication = '4. Умножение'
exit_program = '0. Выход из программы'
message_exit = ''
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
        addition_finish = first_number + second_number
        print('Ответ:', addition_finish)
    if selected_operation == 2:
        subtraction_finish = first_number - second_number
        print('Ответ:', subtraction_finish)
    if selected_operation == 3:
        while second_number == 0:
            print("Ошибка! Введите верное число!")
            second_number = float(input())
        else:
            division_finish = first_number / second_number
            print('Ответ:', division_finish)
        # active = True
        # while active:
        #     if second_number != 0:
        #         division_finish = first_number / second_number
        #         print('Ответ:', division_finish)
        #         break
        #     else:
        #         print('Ошибка! Введите верное число!')
        #         second_number = float(input())
        #         if second_number != 0:
        #             active = False
    if selected_operation == 4:
        multiplication_finish = first_number * second_number
        print('Ответ:', multiplication_finish)
print('Завершение программы! Будем рады видеть Вас снова!')
