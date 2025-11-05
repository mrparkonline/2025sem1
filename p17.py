# List Test Prep Q3 Solutions
def bubble(a_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(a_list)):
            if a_list[i] < a_list[i-1]:
                a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
                swapped = True
    return a_list

def i_sort(a_list):
    # insertion sort
    for i in range(1, len(a_list)):
        for j in range(i, 0, -1):
            if a_list[j] < a_list[j-1]:
                a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
            else:
                break
    return a_list

def selection1(a_list):
    # non-destructive selection sort
    for i in range(len(a_list)-1):
        smallest = a_list[i]
        new_location = i
        for j in range(i+1, len(a_list)):
            if a_list[j] < smallest:
                new_location = j
                smallest = a_list[j]
        # end of inner for
        a_list[i], a_list[new_location] = a_list[new_location], a_list[i]

    return a_list

def selection2(a_list):
    # destructive selection sort
    new_list = []
    while len(a_list) > 0:
        smallest = min(a_list)
        a_list.remove(smallest)
        new_list.append(smallest)
    
    return new_list
# end of sorting functions

# testing sorting functions
from random import randrange

test_list = []
for i in range(12):
    test_list.append(randrange(-100, 100))

test_list2 = test_list.copy() # copying a list method 1
test_list3 = test_list[:] # copying a list method 2
test_list4 = test_list.copy()

print(f"{test_list} sorted with Bubble Sort: {bubble(test_list)}")
print(f"{test_list2} sorted with Insertion Sort: {i_sort(test_list)}")
print(f"{test_list3} sorted with Non-destructive Selection Sort: {selection1(test_list)}")
print(f"{test_list4} sorted with Destructive Selection Sort: {selection2(test_list)}")
# end of testing sorting functions

# Test Prep Q3

def scrabble(word):
    score = 1
    for char in word:
        if char in "AEIOULNSTR":
            score += 1
        elif char in "DG":
            score += 2
        elif char in "BCMP":
            score += 3
        elif char in "FHVWY":
            score += 4
        elif char in "JX":
            score += 8
        elif char in "QZ":
            score += 10
        elif char == "K":
            score += 5
        
    return score
# end of scrabble

def word_scores(word_list):
    score_list = []
    for word in word_list:
        score = scrabble(word)
        score_list.append(score)
    
    return score_list
# end of word_score

def sort_words(word_list):
    score_list = word_scores(word_list)

    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(score_list)):
            # remember that we are going from greatest to least
            if score_list[i] > score_list[i-1]:
                score_list[i], score_list[i-1] = score_list[i-1], score_list[i]
                # whenever the score_list needs to swap, word_list must swap too at the same index
                word_list[i], word_list[i-1] = word_list[i-1], word_list[i]
                swapped = True
    
    return word_list

test_list5 = ["CAT", "DOG", "SUN", "BED", "QUIZ"]
print(f"{test_list5} sorted in scrabble points order: {sort_words(test_list5)}")