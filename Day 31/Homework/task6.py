#6. შექმენი ფუნქცია, რომელსაც არგუმენტად გადასცემ რიცხვს (სტრინგად), შემდეგ ფუნქციაში გადაქციე ეს სტრინგი ინტეჯერად, და დაპრინტე მასზე 5-ჯერ მეტი რიცხვი.
def gamravleba(num):
    num_int = int(num)
    result = num_int * 5
    print(result)

number = input("Please enter a number: ")
gamravleba(number)