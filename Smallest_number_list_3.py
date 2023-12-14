def find_smallest_number(numbers):
    if len(numbers) == 0:
        return None

    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest

list = [33,4455,4234,123,678,8987,33,4]
smallest = find_smallest_number(list)
if smallest is not None:
    print("The smallest number in the list is : ",smallest)
else:
    print("The list is empty")
