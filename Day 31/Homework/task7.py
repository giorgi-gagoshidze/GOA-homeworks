#7. შექმენი ფუნქცია, რომელსაც არგუმენტად გადასცემ სამ რიცხვს, შემდეგ დაპრინტე ამ სამი რიცხვის ნამრავლი, განაყოფი, სხვაობა, ჯამი.
def calculate_operations(num1, num2, num3):
    total_sum = num1 + num2 + num3
    product = num1 * num2 * num3
    difference = num1 - num2 - num3
    try:
        division = num1 / num2 / num3
    except ZeroDivisionError:
        division = "undefined (division by zero)"
    print(f"Sum: {total_sum}")
    print(f"Product: {product}")
    print(f"Difference: {difference}")
    print(f"Division: {division}")
calculate_operations(10, 5, 2)