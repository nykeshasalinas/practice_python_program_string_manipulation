# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
# Example:
# Input: We will weather the weather whatever the weather whether we like it or not
# Output: 14

# Ask user to input a complete statement
statement = input("Enter your full name in incorrect casing: ")

# Print number of words in the input
print (len(statement.split()))