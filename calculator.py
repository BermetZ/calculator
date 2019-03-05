choice = input("Pick an operation to be performed('+','-','*','/'):")

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

if choice == '+':
    print(x + y)

if choice == '-':
    print(x - y)

if choice == '*':
    print(x * y)

if choice == '/' and y == 0:
    print("Can't divide by zero")
else:
    print(x / y)








