#5. Write a Python program that takes a sentence as input and finds the most frequent word.
def program(wordis):
    words = wordis.split()
    wordis = wordis.lower()
    count = 0
    counted_word = ""
    for y in words:
        word_count = words.count(y)
        if word_count > count:
            count = word_count
            counted_word = y
    return counted_word
print(program(input()))