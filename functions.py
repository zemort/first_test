import datetime

def fold(num1, num2):
    """"Сложение двух переменных"""
    result = num1 + num2
    return result


def subtract(num1, num2):
    """"Вычитание двух переменных"""
    result = num1 - num2
    return result


def divide(num1, num2):
    """"Деление двух переменных"""
    result = num1 / num2
    return result


def multiply(num1, num2):
    """"Умножение двух переменных"""
    result = num1 * num2
    return result("operation_history")


def create_history(num1, operation, num2, res):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history_entry = f"{timestamp} {num1} {operation} {num2} = {res}"
    return history_entry


def display_history(operation_history):
    if not operation_history:
        print("История пуста.")
    else:
        print("История операций: ")
        for entry in operation_history:
            print(entry)
