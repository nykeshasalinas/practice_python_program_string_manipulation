# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuanDelaCruz

# Ask user to input their fullname in incorrect casing
full_name = input("Enter your full name in incorrect casing: ")

# Print input in pascal case
print ((full_name.title().replace(" ", "")))