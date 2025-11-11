# PRODUCT CODES

def cleaner(text):
    # TEXT kinda looks like cG23mH-9s
    # WE WANT GH14
    upper_case = ""
    positives = ""
    negatives = "" 
    total_sum = 0
    for item in text:
        if item.isalpha() and item.isupper():
            upper_case += item
            if len(positives) > 0: 
                total_sum += int(positives)
                positives = ""
            if len(negatives) > 0:
                total_sum += int(negatives)
                negatives = ""
        elif item == "-":
            if len(negatives) > 0:
                total_sum += int(negatives)
                negatives = "-"
            else:
                negatives = "-"
        elif item.isdigit():
            if len(negatives) > 0:
                negatives += item
            else:
                positives += item
    # end of for loop

    # if text ended with a digit
    if len(positives) > 0:
        total_sum += int(positives)   
    if len(negatives) > 0:
        total_sum += int(negatives)
    
    product_code = upper_case + str(total_sum)
    return product_code