def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
    else:
        return "Invalid operation"


if __name__ == "__main__":
    
    num1 = float(input("Enter the first number of your choice: "))
    num2 = float(input("Enter the second number of your choice: "))
    operation = input("Choose the operation (add, subtract, multiply, divide): ").lower()

   
    result = calculate(num1, num2, operation)

    
    print(f"The result is: {result}")
