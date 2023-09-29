def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Деление на ноль недопустимо"
    else:
        return a / b

# Функция для выполнения операции
def perform_operation():
    while True:
        # Запрос ввода чисел и операции
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            print("Доступные операции:")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Выйти")

            operation = int(input("Выберите операцию (введите соответствующий номер): "))

            if operation == 1:
                print("Результат сложения:", addition(num1, num2))
            elif operation == 2:
                print("Результат вычитания:", subtraction(num1, num2))
            elif operation == 3:
                print("Результат умножения:", multiplication(num1, num2))
            elif operation == 4:
                print("Результат деления:", division(num1, num2))
            elif operation == 5:
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор операции. Попробуйте ещё раз.")

        except ValueError:
            print("Ошибка: Введите корректное число.")
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль недопустимо.")

# Запуск программы
perform_operation()
