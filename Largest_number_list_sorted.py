numbers = [11, 55, 88, 99, 66, 22, 11]

# Using the sorted() function to find the largest number
if numbers:     # Check if the list is not empty
    sorted_numbers = sorted(numbers, reverse=True)
    largest_number = sorted_numbers[0]
    print(f"Largest numbers {largest_number}")
else:
    print("The list is empty")
