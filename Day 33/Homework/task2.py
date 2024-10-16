
def sum_third_and_fourth(elements):
    if len(elements) < 4:
        print("სიის უნდა იყოს მინიმუმ 5 ელემენტი.")
        return
    total = elements[2] + elements[3]
    print("მე-3 და მე-4 ელემენტის ჯამი:", total)
sum_third_and_fourth([10, 20, 30, 40, 50])