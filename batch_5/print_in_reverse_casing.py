# Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuaN deLA cRuz

# Ask user to input their fullname in incorrect casing
full_name = input("Enter your full name in incorrect casing: ")

# Print input in reverse casing
print ("Full name:", full_name.swapcase())