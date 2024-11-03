#5. შექმენით 4 სხვადასხვა list-ი, თითოში დაამატეთ მინიმუმ 10 ელემენტი და დაპრინტეთ: 1) პირველ list-ის პირველიდან მეოთხე ელემენტამდე ცვლადები.2) მეორე list-ის მეოთხედან მერვე ელემენტამდე ცვლადები ფორ ციკლის          გამოყენებით.3) მესამე list-ის მეცხრედან მეექვსე ელემენტამდე ცვლადები გაითვალისწინეთ არა 6დან 9მდე არამედ 9დან 6მდე გამოიყენეთ უარყოფითი რიცხვები. 4) მეოთხე list-ში დაპრინტეთ მისი ყველა ცვლადი while ცოკლის გამოყენებით.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
list4 = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
print("First list elements (1st to 4th):", list1[0:4])
print("Second list elements (4th to 8th):", end=' ')
for i in range(3, 8):  
    print(list2[i], end=' ')
print()
print("Third list elements (9th to 6th) with negative numbers:", end=' ')
for i in range(9, 5, -1):  
    print(-list3[i], end=' ')
print()
print("Fourth list elements:")
index = 0
while index < len(list4):
    print(list4[index])
    index += 1
