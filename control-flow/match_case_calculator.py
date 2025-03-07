#Using match case statements to handle arithmetic operations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ").strip()

match operator:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")    
    case "*":
        result = num1 * num2
        print(f"The result is {result}")    
    case "/":
        if num2 == 0: #Division by zero check
              print("Cannot divide by zero")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation")
    
