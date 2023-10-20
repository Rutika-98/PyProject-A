#Table from 1-10 without taking input from user

print(f"*Multiplication Table*")

for n in range(1,11):
    print("-----------------------")
    for i in range(1, 11):
        product = n * i
        print(f"{n} x {i} = {product}")