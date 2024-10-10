#8. შექმენი ფუნქცია, რომელსაც არგუმენტად გადასცემ 5 ელემენტიან სიას, შემდეგ დაპრინტე ამ სიის მე-3 ინდექსზე მყოფი ელემენტი.
def elementidex(elements):
    if len(elements) >= 5:
        print(elements[3])
    else:
        print("The list Must contain at least 5 elements!.")
numlist = [10, 20, 30, 40, 50]
elementidex(numlist)
