def odd_even(numbers_list):
    for number in numbers_list:
        if number % 2 == 0:
            print(f"Even: {number}")
        else:
            print(f"Odd: {number}")

# Example usage: გამოყენების მაგალითი   
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_even(numbers)         