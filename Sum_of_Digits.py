# Sum of Digits:
#
# Create a function that calculates the sum of the digits of a positive integer.
#
# Examples : 1) n = 12345, sum = 15 2) n = 123, sum = 6


def sum_of_digits(n):

    total = 0

    n_str = str(n)

    for digits in n_str:
        total += int(digits)

    return total

n1 = int(input("Enetr the number : "))
sum1 = sum_of_digits(n1)
print(f"n = {n1}\nsum = {sum1}")

n1 = 12345
sum1 = sum_of_digits(n1)
print(f"n = {n1}\nsum = {sum1}")

n2 = 123
sum2 = sum_of_digits(n2)
print(f"n = {n2}\nsum = {sum2}")