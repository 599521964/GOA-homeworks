# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Define the minimum age required to participate in elections
voting_age = 18

# Check if the user's age meets the eligibility criteria
if age >= voting_age:
    print("You are eligible to participate in the elections.")
else:
    print("You are not eligible to participate in the elections.")