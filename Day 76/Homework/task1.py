#1. Write a function that takes three numbers and returns the largest one without using max().
def functio(num1,num2,num3):
    num1 = int(input())
    num2 = int(input())
    num2 = int(input())
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(functio)