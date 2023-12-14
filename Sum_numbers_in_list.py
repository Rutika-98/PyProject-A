# Write a Python program to sum all numbers in a list.

def total_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

list = [1,2,3,4,5,6,7,8,9]
sum = total_sum(list)
print("Total sum all numbers in a list",sum)