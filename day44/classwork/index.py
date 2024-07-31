#Here are examples and explanations of how the capitalize, upper, lower, count, and title 
#methods work in Python. I'll also explain the difference between a method and a function.
text = "hello world "

# Capitalize method
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: "Hello world"

# Upper method
upper_text = text.upper()
print(upper_text)  # Output: "HELLO WORLD"

# Lower method
lower_text = text.lower()
print(lower_text)  # Output: "hello world"

# Count method
count_l = text.count('l')
print(count_l)  # Output: 3

# Title method
title_text = text.title()
print(title_text)  # Output: "Hello World"

#Explanations:
#capitalize Method:

#Converts the first character of the string to uppercase and all other characters to lowercase.
#Example: "hello world" becomes "Hello world".
#upper Method:

#Converts all characters in the string to uppercase.
#Example: "hello world" becomes "HELLO WORLD".
#lower Method:

#Converts all characters in the string to lowercase.
#Example: "HELLO WORLD" becomes "hello world".
#count Method:

#Counts the number of occurrences of a specified substring in the string.
#Example: The count of 'l' in "hello world" is 3.
#title Method:

#Converts the first character of each word to uppercase and all other characters to lowercase.
#Example: "hello world" becomes "Hello World".
#Method vs. Function:
#Method:

#A method is a function that is associated with an object. It is called on an object and can access and modify the object's state. Methods are defined within a class.
#Example: text.capitalize(). Here, capitalize is a method of the str class.
#Function:

#A function is a block of code that performs a specific task. It can be called independently and does not necessarily operate on objects.
#Example: len(text). Here, len is a built-in function in Python that returns the length of an object.
#In summary, methods are functions that belong to objects and can operate on those objects, whereas functions are standalone blocks of code that can take input and return output.

