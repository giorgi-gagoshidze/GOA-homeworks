#მომხმარებელს შემოატანინეთ 2 რიცხვი და ოპერატორი ანუ მაგ:პირველი რიცხვი - 10მეორე რიცხვი- 15ოპერატორი - +და შეასრულეთ მოქმედება კალკულატორის სტილში მომხმარებელს უნდა შეეძლოს +,-,/,* შემოტანა ასევე გაითვალისწინეთ რომ 0ზე გაყოფა არ შეიძლება
def is_valid_number(num_str):
    """Helper function to check if the input is a valid number."""
    try:
        float(num_str) 
        return True
    except:
        return False
def calculate():
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")
    operator = input("Enter the operator (+, -, *, /): ")
    if not is_valid_number(num1_str) or not is_valid_number(num2_str):
        print("Error: Please enter valid numbers!")
        return
    num1 = float(num1_str)
    num2 = float(num2_str)
    if operator == '/' and num2 == 0:
        print("Error: Division by zero is not allowed!")
        return
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Error: Invalid operator! Use +, -, *, or /.")
        return
    print(f"The result of {num1} {operator} {num2} = {result}")
calculate()

