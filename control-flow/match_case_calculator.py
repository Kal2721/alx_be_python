num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2)
    case "-":
        result = num1 - num2)
    case "*":
        result = num1 * num2)
    case "/":
        if num2 == 0:
            print("Invalid operation")
        else:
            result = num1 / num2
    case _:
        print("No number provided")
print("The result is:", result)