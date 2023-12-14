# Write a Python program to multiply all numbers in a list

from functools import reduce

def multiply_numbers(numbers):
    if len(numbers) == 0:
        return None

    result = reduce(lambda x, y: x * y, numbers)
    return result

list = [1,2,3,4,5,6,7,8,9]
product_of_numbers = multiply_numbers(list)
if product_of_numbers is not None:
    print("The product is:",product_of_numbers)
else:
    print("The list is empty")