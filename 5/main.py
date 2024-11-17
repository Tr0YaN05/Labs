def get_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return positive_numbers


print(get_positive_numbers([1, -2, 3, -4, 5]))
print(get_positive_numbers([-10, 0, 7, 8, -5]))

def is_number_in_list(numbers, target):
    return target in numbers

print(is_number_in_list([1, 2, 3, 4, 5], 3))
print(is_number_in_list([1, 2, 3, 4, 5], 6))

from math import prod, pow

def geometric_mean(numbers):
    if not numbers:
        return None  
    product = prod(numbers)
    n = len(numbers)
    return pow(product, 1/n)


print(geometric_mean([1, 2, 3, 4, 5]))
print(geometric_mean([2, 8]))

