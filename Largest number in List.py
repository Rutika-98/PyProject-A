# Write a Python program to find the largest number in a list.

# list = [11, 55, 88, 99, 66, 22, 11]
#
# print(max(list))


def find_largest_number(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

numbers = [11, 55, 88, 99, 66, 22, 11]
largest_number = find_largest_number(numbers)

if largest_number is not None:
    print(f"The largest number in the list is: {largest_number}")
else:
    print("The List is Empty")
