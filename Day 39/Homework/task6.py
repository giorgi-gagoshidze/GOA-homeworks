def analyze_list(numbers):
    if len(numbers) < 5:
        print("Error: List must contain at least 5 numbers.")
        return
    max_num = max(numbers)
    min_num = min(numbers)
    total_sum = sum(numbers)
    length = len(numbers)
    print(f"Max number: {max_num}")
    print(f"Min number: {min_num}")
    print(f"Sum of numbers: {total_sum}")
    print(f"Length of list: {length}")
user_input = input("Please enter at least 5 numbers separated by spaces: ")
number_list = list(map(int, user_input.split()))
analyze_list(number_list)
