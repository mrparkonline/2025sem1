# String stuff
# tacocat is a palindrome :)
# like doggod
# like 906609
# like 0101010 ... which is 42 in binary ... the meaning of life!
def is_palindrome(word):
    # checks is argument word is a palindrome
    return word == word[::-1]

text = input("Fam pls enter a word: ")
if is_palindrome(text):
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is BORING~")