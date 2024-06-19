number = 20
while number >= 1:
    print(number)
    number -= 1

    number = 0
while number <= 10:
    if number % 2 != 0:  # Check if the number is odd
        print(number)
    number += 1

    number = 0
total_sum = 0

while number <= 10:
    total_sum += number
    number += 1

print("The sum of all numbers from 0 to 10 is:", total_sum)