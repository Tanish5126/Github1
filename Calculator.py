while True:
    op = input("Enter operation: ")
    if op == 'q':
        print("Goodbye!")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == "**":
        print("Result:", a**b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '%':
        print("Result:", a % b)    
    elif op == '/':
        if b == 0:
            print("Error! Division by zero.")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operation!")