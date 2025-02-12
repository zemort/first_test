import datetime
from functions import fold
from functions import subtract
from functions import divide
from functions import multiply
addition = '1. Сложение'
subtraction = '2. Вычитание'
division = '3. Деление'
multiplication = '4. Умножение'
history = '5. История'
exit_program = '0. Выход из программы'
operation_history = []
while True:
    print("Пожалуйста, выберите операцию:",addition, subtraction, division, multiplication,history,exit_program, sep='\n')
    selected_operation = int(input())
    if selected_operation == 0:
        break
    elif selected_operation == 5:
        if not operation_history:
            print("История пуста.")
        else:
            print("История операций: ")
            for entry in operation_history:
                print(entry)
        continue
    else:
        print('Введите первое число: ')
        first_number = float(input())
        print('Введите второе число: ')
        second_number = float(input())
    if selected_operation == 1:
        operation = "+"
        result = fold(first_number,second_number)
    elif selected_operation == 2:
        operation = "-"
        result = subtract(first_number, second_number)
    elif selected_operation == 3:
        operation = "/"
        while second_number == 0:
            print("Ошибка! Введите верное число!")
            second_number = float(input())
        result = divide(first_number,second_number)
    elif selected_operation == 4:
        operation = "*"
        result = multiply(first_number, second_number)
    else:
        print("Неверный выбор операции!")
        continue
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history_entry = f"{timestamp} {first_number} {operation} {second_number} = {result}"
    operation_history.append(history_entry)
    print(f"Ответ: {result}")
print('Завершение программы! Будем рады видеть Вас снова!')
