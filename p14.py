# CCC 2025 - J3
# Product Codes
unclean = input("Enter product code: ")
lowercase = ""
uppercase = ""
non_letters = ""
for item in unclean:
    if item.isalpha() and item.islower():
        lowercase += item
    elif item.isalpha() and item.isupper():
        uppercase += item
    else:
        non_letters += item
print(lowercase, uppercase, non_letters)