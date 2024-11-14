def vending_machine(products, prices, balance):
    print("თქვენი ბალანსი:", balance)
    print("შესაბამისად, ხელმისაწვდომი პროდუქტები:")
    for i, product in enumerate(products):
        print(f"{i + 1}. {product} - {prices[i]} ლარი")
    choice = int(input("აირჩიეთ პროდუქტის ნომერი: ")) - 1
    if choice < 0 or choice >= len(products):
        print("არასწორი არჩევანი.")
        return
    if balance >= prices[choice]:
        balance -= prices[choice]
        print(f"თქვენ აირჩიეთ {products[choice]} და გადაიხადეთ {prices[choice]} ლარი.")
        print("მოპოვებული პროდუქტით ბედნიერებას გისურვებთ!")
        print(f"სადაც დარჩა ბალანსი: {balance} ლარი.")
    else:
        print("გთხოვთ, შეამოწმეთ ბალანსი. საკმარისი ფული არ გაქვტ!")
products = ["კოკა-კოლა", "ჩიფსი", "შოკოლადი", "თვითმფრინავის ბილეთი"]
prices = [2.5, 1.0, 3.0, 20.0]
balance = 5.0
vending_machine(products, prices, balance )
