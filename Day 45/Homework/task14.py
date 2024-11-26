#14. შექმენით ფუნქცია რომელსაც გადაეცემა  რიცხვების სია,თქვენი მოვალეობააა შექმნათ ახალი სია და ამ ახალ სიაში გამოიტანოთ ყოველი რიცხვის კვადრატი (append) და შემდეგ დააბრუნეთ ახალი სია. test case: [3,12,5,2,6] | output: [9,144,25,4,36]
def square_numbers(numbers):
    squared_numbers = []  
    for num in numbers:
        squared_numbers.append(num ** 2)  
    return squared_numbers  
numbers = [3, 12, 5, 2, 6]
result = square_numbers(numbers)
print(result)  
