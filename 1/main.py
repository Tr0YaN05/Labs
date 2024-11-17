import math

def calculate_circle_area():
    radius = float(input("Введіть радіус круга: "))
    area = math.pi * (radius ** 2)
    print(f"Площа круга з радіусом {radius} дорівнює {area:.2f}")
calculate_circle_area()

def calculate_square():
    number = float(input("Введіть число: "))
    square_1 = number ** 2
    square_2 = pow(number, 2)
    print(f"Квадрат числа {number} (оператор `**`): {square_1}")
    print(f"Квадрат числа {number} (функція `pow`): {square_2}")
calculate_square()

def check_priority():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    result_1 = a + b * c
    result_2 = (a + b) * c
    print(f"Результат без зміни пріоритету: {result_1}")
    print(f"Результат зі зміненим пріоритетом: {result_2}")
check_priority()

