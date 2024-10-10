#5. შექმენი ფუნქცია, სადაც პირველ არგუმენტად input()-ის გამოყენებით გადასცემ ასაკს, მეორე არგუმენტად კი input()-ის გამოყენებით გადასცემ სახელს, შემდეგ დაპრინტე, თუ რა ქვია მომხმარებელს და რამდენი წლის არის ის.
def user_info():
    age = input("Please enter your age: ")
    name = input("Please enter your name: ")
    print(f"{name} is {age} years old.")
user_info()