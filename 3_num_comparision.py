# Use the ternary operator to find the maximum of three numbers entered by the user.

# Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Use the ternary operator to find the maximum
max_num = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)

# Print the maximum number
print("The maximum number is:", max_num)