import math  # Підключення бібліотеки

def task_integer13():
    """Task 1: Дано тризначне число. 
    У ньому закреслили першу зліва цифру і приписали її справа."""
    try:
        number = int(input("Завдання 1: Введіть тризначне число: "))
        if not (100 <= abs(number) <= 999):
            raise ValueError("Число повинно бути тризначним!")
    except ValueError as e:
        print("Помилка:", e)
    else:
        first_digit = number // 100
        remaining_part = number % 100
        result = remaining_part * 10 + first_digit
        print("Результат:", result)

def task_math_expression():
    """Task 2: Обчислення заданого математичного виразу"""
    try:
        x = float(input("Завдання 2: Введіть значення x: "))
        if x == 0:
            raise ValueError("x не може дорівнювати 0 (для логарифма)!")
    except ValueError as e:
        print("Помилка:", e)
    else:
        try:
            angle_in_radians = math.radians(43)
            numerator = 2 * math.exp(x + 5) * math.sqrt(abs(3 * x - 2 * math.tan(5 * x - angle_in_radians)))
            x_cubed = x ** 3
            sin_squared = math.sin(x_cubed) ** 2
            log_base_5 = math.log(abs(x_cubed), 5)
            denominator = math.pow(sin_squared * log_base_5, 1/3)
            y = numerator / denominator
        except (ValueError, ZeroDivisionError) as e:
            print("Помилка обчислень:", e)
        else:
            print("Результат:", y)

def task_boolean22():
    """Task 3: Дано тризначне число.
    Перевірити істинність висловлювання: «Цифри утворюють зростаючу або спадаючу послідовність»."""
    try:
        number = int(input("Завдання 3: Введіть тризначне число: "))
        if not (100 <= abs(number) <= 999):
            raise ValueError("Число повинно бути тризначним!")
    except ValueError as e:
        print("Помилка:", e)
    else:
        a = number // 100
        b = (number // 10) % 10
        c = number % 10
        is_increasing = a < b < c
        is_decreasing = a > b > c
        result = is_increasing or is_decreasing
        print("Цифри утворюють послідовність:", result)

# Меню вибору завдань
def main():
    while True:
        print("\nОберіть завдання для виконання:")
        print("1 - Завдання 1: Закреслили першу цифру і приписали її справа")
        print("2 - Завдання 2: Обчислення математичного виразу")
        print("3 - Завдання 3: Перевірити послідовність цифр")
        print("0 - Вихід")

        choice = input("Ваш вибір: ")
        if choice == "1":
            task_integer13()
        elif choice == "2":
            task_math_expression()
        elif choice == "3":
            task_boolean22()
        elif choice == "0":
            print("Вихід з програми. До побачення!")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

# Запуск програми
if __name__ == "__main__":
    main()
