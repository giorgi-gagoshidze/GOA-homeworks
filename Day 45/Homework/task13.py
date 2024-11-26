#13. შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია,თქვენი მოვალეობააა გამოითვალე ამ სიის საშუალო არითმეტიკული. test case: [1,3,4,5,2] | output: 3
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average
numbers = [1, 3, 4, 5, 2]
result = calculate_average(numbers)
print(result)  
