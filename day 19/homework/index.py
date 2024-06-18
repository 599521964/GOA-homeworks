# Ask the user to enter a number
number = int(input("Enter a number: "))

# Initialize the sum variable
total_sum = 0

# Use a for loop to calculate the sum of all numbers up to the entered number
for i in range(1, number + 1):
    total_sum += i

# Print the result
print(f"The sum of all numbers up to {number} is: {total_sum}")