def is_leap_year():
    year = int(input("Введіть рік: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"Рік {year} є високосним.")
    else:
        print(f"Рік {year} не є високосним.")
is_leap_year()

def print_reverse_order():
    N = int(input("Введіть число N: "))
    for i in range(N, 0, -1):
        print(i, end=" ")
print_reverse_order()

def stop_at_25():
    for i in range(1, 51):
        if i == 25:
            print(f"Зупинка на числі {i}")
            break
        print(i, end=" ")
stop_at_25()

