# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Check the age range and print the corresponding category
if age > 5 and age < 12:
    print("You are a child.")
elif age >= 12 and age < 18:
    print("You are a teenager.")
elif age >= 18:
    print("You are an adult.")
else:
    print("Invalid age entered.")