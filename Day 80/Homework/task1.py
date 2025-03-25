def guess_number():
    """try to guess theee numberrrrrrr"""
    secret_number = 23 
    attempts = 0
    while True:
        ask = int(input("take a guess 1-100: "))
        attempts += 1
        if ask < secret_number:
            print("number is higher ")
        elif ask > secret_number:
            print("number is lowerr")
        else:
            print(f"concratulatins you guessd in {attempts} attepmts!!!!!!!")
guess_number()
