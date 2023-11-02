# Palindrome Checker
#
# A palindrome checker is a program or function that determines whether a given string or
# sequence of characters reads the same forward and backward.

def is_palindrome(s):

    # Remove spaces and convert to lowercase for a case-insensitive check
    s = s.replace(" ","").lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage:
input_str = input("Enter the string : ")
if is_palindrome(input_str):
    print(f"{input_str} is a palindrome")
else:
    print(f"{input_str} is not palindrome")