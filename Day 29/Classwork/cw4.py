#შექმენით 1 ლისტი და გამოიყენეთ ყველა ფუნქცია რაც დღეს გავიარეთ
list = [3, 1, 4, 1, 5]

list.append(9)
print("append() ->", list)

list.insert(2, 8)
print("insert() ->", list)

list.remove(1)
print("remove() ->", list)

popped_element = list.pop()
print("pop() ->", list, ", popped element:", popped_element)

list.reverse()
print("reverse() ->", list)
