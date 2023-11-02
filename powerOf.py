# Create a Function with a Parameter which can do x^y
def power(x,y):
    result = x ** y
    return result

base = 2
exponant = 3
result = power(base, exponant)
print(f"{base} ^ {exponant} = {result}")

