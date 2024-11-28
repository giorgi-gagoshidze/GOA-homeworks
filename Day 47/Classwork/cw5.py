#მომხმარებელს შემოატანინეთ რიცხვი და while ციკლის გამოყენებით დაპრინტეთ ამ რიცხვის ფაქტორიალი
number = int(input(f"plz whrite a number:"))
factorialiudris = 1
while number > 1:
    factorialiudris *= number
    number -= 1
print(f"factolrial issss: {factorialiudris}")
