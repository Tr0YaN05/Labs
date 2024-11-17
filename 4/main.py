import math

def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]


def check_number_in_list(numbers, x):
    return x in numbers


def geometric_mean(numbers):
    if not numbers or any(num <= 0 for num in numbers):
        return None
    product = math.prod(numbers)
    return product ** (1 / len(numbers))


test_list = [-5, 0, 3, 10, -2, 7]
test_number = 3


positive_numbers = filter_positive_numbers(test_list)
print("Позитивні числа:", positive_numbers)


is_in_list = check_number_in_list(test_list, test_number)
print(f"Число {test_number} входить до списку:", is_in_list)


geometric_mean_result = geometric_mean(positive_numbers)
print("Середнє геометричне позитивних чисел:", geometric_mean_result)
