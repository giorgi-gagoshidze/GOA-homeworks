#9. შექმენი ფუნცია, რომელსაც პირველ არგუმენტად გადასცემ 5 ელემენტიან სიას, ხოლო მეორე არგუმენტად გადასცემ რაიმე რიცხვს, შემდეგ დაპრინტე ამ სიიდან ის ინდექსი, რომელი რიცხვიც მეორე არგუმენტად გადაეცი.
def find_index(elements, number):
    if len(elements) >= 5:
        try:
            index = elements.index(number)
            print(f"The index of {number} is: {index}")
        except ValueError:
            print(f"{number} is not in the list.")
    else:
        print("The list must contain at least 5 elements.")

list = [10, 20, 30, 40, 50]
numbertofind = 30 
find_index(list, numbertofind)