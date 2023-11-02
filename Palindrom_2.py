# This code also checks if a string is a palindrome by removing spaces and converting it to lowercase for case insensitivity.
# It then uses two pointers to compare characters from the start and end of the string, moving towards the center.
# If at any point the characters don('t match, it returns False. '
# 'If the loop completes without finding a mismatch, it returns True)

def is_Palindrome(str):
    # Remove spaces and convert to lowercase for case insensitivity
    str = str.replace(" ","").lower()

    # Initialize pointer for start and end, moving towards the center

    start = 0
    end = len(str) - 1

    # Check characters from the start and end, moving towards the center
    while start < end:
        if str[start] != str[end]:
            return False
        else:
            return True
        start += 1
        end -= 1
    return True

# Test the function
str = input("Enter a string : ")
if is_Palindrome(str):
    print(str,"Palindrome")
else:
    print(str,"Not Palindrome")