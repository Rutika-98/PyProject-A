#Multiplication using formatting
n = int(input("Enter the number : "))

print(f"Multiplication of Number { n }")

for i in range(1, 11):
    product = n * i;
    print(f"{n} x {i} = {product}")