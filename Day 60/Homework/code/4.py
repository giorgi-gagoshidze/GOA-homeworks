"https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python"
#Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    count_positives = 0
    sum_negatives = 0
    
    for number in arr:
        if number > 0:
            count_positives += 1
        else: 
            sum_negatives += number
        
    return[count_positives,sum_negatives]