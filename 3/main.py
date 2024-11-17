def calculate_percentage(a, b):
    try:
        result = (a / b) * 100
        print(f"Відсоткове співвідношення: {result:.2f}%")
    except ZeroDivisionError:
        print("Помилка: ділення на нуль.")

calculate_percentage(50, 200)
calculate_percentage(100, 0)

def check_odd_number():
    try:
        number = int(input("Введіть число: "))
        if number % 2 != 0:
            print("Число є непарним.")
        else:
            print("Число є парним.")
    except ValueError:
        print("Помилка: введено некоректне значення.")

check_odd_number()

def calculate_cube_volume():
    try:
        side = float(input("Введіть довжину сторони куба: "))
        if side <= 0:
            raise ValueError("Довжина сторони повинна бути додатньою.")
        volume = side ** 3
        print(f"Об'єм куба: {volume:.2f}")
    except ValueError as e:
        print(f"Помилка: {e}")

calculate_cube_volume()


