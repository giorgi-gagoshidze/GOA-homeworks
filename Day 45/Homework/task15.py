#15. გაიხსენეთ ყველა list-ის და string-ის მეთოდები და გამოიყენეთ თავისი მაგალითებით.
#esaa listi
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits) 

fruits = ["apple", "banana"]
more_fruits = ["cherry", "orange"]
fruits.extend(more_fruits)
print(fruits)  

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits)  

fruits = ["apple", "banana", "cherry"]
popped_item = fruits.pop(1)
print(fruits)  # ['apple', 'cherry']
print(popped_item)  # 'banana'

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
