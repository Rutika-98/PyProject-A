def count_vowels_and_consonant(text):
    # Initialize counters for vowels and consonants to 0
    vowel_count = 0
    consonant_count = 0

    # Define a set of vowels (both lowercase and uppercase)
    Vowels = "aeiouAEIOU"

    # Iterate through each character in the input text
    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            if char in Vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

# Example usage
input_text = input("Enter a string : ")
vowels, consonants = count_vowels_and_consonant(input_text)

print("Vowels : ",vowels)
print("Consonants : ",consonants)