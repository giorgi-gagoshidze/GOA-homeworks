# Create a function that checks if a word is a palindrome. A palindrome is a word that reads the same forward and backward, like 'racecar' or 'level', ignoring capitalization.
def LETS_SEE_IF_IT_CAN_REVERSE(word):
    word = word.lower() 
    return word == word[::-1]
print(LETS_SEE_IF_IT_CAN_REVERSE("racecar"))
print(LETS_SEE_IF_IT_CAN_REVERSE("level"))
print(LETS_SEE_IF_IT_CAN_REVERSE("html"))
print(LETS_SEE_IF_IT_CAN_REVERSE("ana"))
print(LETS_SEE_IF_IT_CAN_REVERSE("kiwi"))