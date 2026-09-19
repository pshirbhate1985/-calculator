def calc(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
operation=input("Enter operation (add, subtract, multiply, divide): ")
result = calc(a, b, operation)
print(f"The result of {operation}ing {a} and {b} is: {result}")