# Write a Python program to multiply all numbers in a list

def multiply_numbers(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

list = [1,2,3,4,5,6,7,8,9]
multiplication = multiply_numbers(list)
print("Multiplication of numbers : ",multiplication)