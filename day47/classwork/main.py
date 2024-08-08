def filter_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers
my_list = [1, 2, 3, 4, 5, 6]
filtered_list = filter_even_numbers(my_list)
print(filtered_list)  # Output: [2, 4, 6]