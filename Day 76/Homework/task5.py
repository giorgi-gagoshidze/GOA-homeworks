#5. Create a function that finds the longest word in a sentence. (მოიძიეთ ინფრომაცია split()-ზე.
def LETS_FIND_DE_LONGEST_WORD(sentence):
    words = sentence.split() 
    longest_word = ""  
    for word in words:  
        if len(word) > len(longest_word): 
            longest_word = word 
    return longest_word 
print(LETS_FIND_DE_LONGEST_WORD("IMTHELONGEST NOIAMTHELONGEST!!!! NAHHHIAMSTOPLYINGGG WELLIAMIFYOULOOKCLOSELY LETSSEEWHOSTHELONGESTWORDITHINKITSME NOITSNOTYOUITSMEBCIAMTHELONGESTLIKESWWETATTHEENDANDTHISTIMELONGESTATTHEEND:))"))
