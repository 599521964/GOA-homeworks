# Start a while loop that will continue until the user is over 18 years old
while True:
    # Prompt the user to enter their age
    age = int(input("Please enter your age: "))
    
    # Check if the entered age is greater than 18
    if age > 18:
        # If the age is greater than 18, print a success message and break the loop
        print("You can enter the program.")
        break
    else:
        # If the age is less than or equal to 18, print an error message
        print("You cannot enter the program because you are under 18.")