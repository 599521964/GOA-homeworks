choice = input("please enter operation(+, -, *, /): ")
num1 = int(input("please enter operation: "))
num2 = int(input("please second operation: "))

if choice == '+':
    print(num1 + num2)
elif choice == '-':
    print(num1 - num2)
elif choice == '*':
    print(num1 * num2)
elif choice == '/':
    print(num1 / num2)
else:
    print("invalid opreration")