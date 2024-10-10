#10. შექმენი ფუნქცია, რომელსაც არგუმენტად გადასცემ რიცხვს, შემდეგ დაპრინტე 0-იდან ამ რიცხვამდე ყველა რიცხვი, გამოიყენე for loop().
def print_numbers_up_to(n):
    for i in range(n + 1):
        print(i)

number = int(input("Please enter a number: "))
print_numbers_up_to(number)
