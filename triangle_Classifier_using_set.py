# In this approach, we create a set side_lengths to store the unique side lengths of the triangle.
# Then, we check the length of the set to determine if the triangle is equilateral (all side lengths are the same),
# isosceles (two side lengths are the same), or scalene (all side lengths are different).
# This approach eliminates the need for nested if-else statements and provides a more concise solution.

side_1 = float(input("Enter side 1 :"))
side_2 = float(input("Enetr side 2 :"))
side_3 = float(input("Enetr side 3 :"))

side_lengths = {side_1,side_2,side_3}

if len(side_lengths) == 1:
    print("Equilateral")
elif len(side_lengths) == 2:
    print("Iso")
else:
    print("Scalene")