# Initialize the number variable to 0
number = 0

# Start the while loop that continues as long as the number is less than or equal to 10
while number <= 10:
    # Use if-else statement to check if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    
    # Increment the number by 1
    number += 1