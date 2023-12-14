#  Write a Python program to find the smallest number in a list.

def find_smallest_number(numbers):
    if not numbers:
        return None

    smallest = numbers[0]

    for n in numbers:
        if n < smallest:
            smallest = n

    return smallest

list = [33,4455,4234,123,678,8987,3]
smallest_number = find_smallest_number(list)


if smallest_number is not None:
    print(f"The smallest number : {smallest_number}")
else:
    print("The list is empty")
