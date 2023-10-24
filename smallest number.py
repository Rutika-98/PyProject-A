#To find the smallest number:

a = 10
b = 20
c = 30

if a < b and b < c:
    smallest = a
elif b < a and b < c:
    smallest = b
else:
    smallest = c

print("The smallest number is ",smallest)