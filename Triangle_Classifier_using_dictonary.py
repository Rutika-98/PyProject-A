# In this approach, we create a dictionary triangle_types to map the count of unique side lengths to the corresponding triangle types.
# We then count the unique side lengths, and based on that count, we look up the triangle type in the dictionary.
# This approach avoids explicit if-else statements and provides a more compact way to classify the triangle.

# Input the side lengths of the triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Create a dictionary to map the count of unique side lengths to triangle types
triangle_types = {1: "Eq.", 2: "Iso", 3: "Scalene"}

# Create a set to store unique side lengths
side_lengths = {side1, side2, side3}

# Check if it's a valid triangle
if len(side_lengths) == 3:
    unique_counts = 3
elif len(side_lengths) == 2:
    unique_counts = 2
else:
    unique_counts = 1

# Determine the triangle type using the dictionary
print(triangle_types[unique_counts])



