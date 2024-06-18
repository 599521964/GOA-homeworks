# Ask the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Initialize variables for sum and product
sum_result = 0
product_result = 1

# Ensure num1 is the smaller number and num2 is the larger number
start = min(num1, num2)
end = max(num1, num2)

# Use a for loop to calculate the sum and product of all numbers between num1 and num2
for i in range(start, end + 1):
    sum_result += i
    product_result *= i

# Print the results
print(f"The sum of all numbers between {num1} and {num2} is: {sum_result}")
print(f"The product of all numbers between {num1} and {num2} is: {product_result}")