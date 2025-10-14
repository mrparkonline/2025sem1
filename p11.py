# String Practice

# Cleaning
def clean(text):
    # to return a string with everything lowercased
    # and without special characters nor numbers
    result = ""
    i = 0 # avoid index b/c it is a function/method name
    while i < len(text):
        # .isalpha() returns True if the given character is 
        # alphabetical
        if text[i].isalpha():
            result = result + text[i].lower()
        i += 1
    # end while loop
    return result

# First Algorithm Learned: Linear Search
'''
let X represent a string, T be a target character to search
let I represent index of a string
while i < len(X), if X[i] == T then return i else i + 1
if T is not found, return -1
'''
def str_lin_search(text, target):
    if not text: # len(text) == 0
        return -1
    else:
        i = 0
        while i < len(text):
            if text[i] == target:
                return i
            i += 1
        # end of while
        return -1

print("Jasper... where is p?", str_lin_search("Jasper", "p"))
