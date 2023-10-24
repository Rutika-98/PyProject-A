#To check if all three numbers are equal:

a = input("Number 1 = ")
b = input("Number 2 = ")
c = input("Number 3 = ")

# if a == b == c:
#     print("a, b & c are equal")
# else:
#     print("not equal")

if a == b and a == c:
    are_equal = True
else:
    are_equal = False

if are_equal:
    print("All three numbers are equal")
else:
    print("All three numbers are not equal")