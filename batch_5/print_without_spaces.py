# Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
# Example:
# Input:         Juan Dela Cruz
# Output: Juan Dela Cruz

# Ask user to input their fullname, add several space characters at the beginning
full_name = input("Enter your full name (add spaces before input): ")

# Print input without the spaces in the beginning
print ("Full name:", full_name.lstrip())