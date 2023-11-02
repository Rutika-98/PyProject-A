#Create a Lambda expression to triple power 2**3 a number

# Define the Lambda expression

triple_power_of_2_to_3 = lambda x: (2 ** 3) * x

# Test the Lambda expression
n = 5   # You can change this to any number you'd like
result = triple_power_of_2_to_3(n)
print(f"triple the power of 2^3 for {n} is: {result}")