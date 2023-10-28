# In this approach, we use a dictionary grading_scale to map score ranges to letter grades.
# We iterate through the dictionary to find the appropriate letter grade based on the input score.
# If the score is not within any of the defined ranges, it will output "Invalid score. Please enter a score between 0 and 100."

# Create a Dictionary to map the score ranges to letter grades
grading_scale={
    (90,100): "A",
    (80,89): "B",
    (70,79): "C",
    (60,69): "D",
    (0,59): "F"
}

# Get the numerical score from the user
score = int(input("Enter the numerical score:"))

# Initialize the grade to None
grade = None

# Determine the letter grade based on the score
for (lower, upper), letter in grading_scale.items():
    if lower <= score <= upper:
        grade = letter
        break

# Display the letter grade
if grade is not None:
    print("The letter grade is:", grade)
else:
    print("Invalid score. Please enter a score between 0 and 100")