# Count vowels and consonants in a String
# aeiou
# input = pramod
# vol = 2

#  Convert the input to lowercase to make it case-insensitive
input_string = input("Enter a string: ").lower()

# Initialize counters
vowel_count = 0
consonant_count = 0

# Define a set of vowels
vowels = "aeiou"

# Iterate through each character in the input string
for char in input_string:
    if char.isalpha():  # Check if the character is an alphabet
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Print the counts
print("Vowels count:",vowel_count)
print("Consonant count:",consonant_count)