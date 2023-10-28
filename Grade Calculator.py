# Write a program that calculates and displays the letter grade for
# a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# If, elif, else

# Get the numerical score from user
score = int(input("Enter the numerical score:"))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
else:
    grade = "F"

# Display the letter grade

print("The letter grade is :",grade)