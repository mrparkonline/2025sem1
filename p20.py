# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Assume that n is the length the array
def missing(array):
    # alternate solution --> slower
    # for i in range(0, limit+1):
    #     if i not in array:
    #         return i

    limit = len(array)
    freq_table = {}
    for x in array:
        freq_table[x] = 1
    for i in range(0, limit+1):
        if i not in freq_table:
            return i
    return -1 # error code

print(missing([3,0,1]))
print(missing([9,6,4,2,3,5,7,0,1]))
            
# Exponent
# Expressing X ^ N as a recursion
# Recipe:
# Base Case, Work Towards Base, Call the function again and again
def exponent(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * exponent(base, exp-1)

# Anagram Revisited
def anagram_check(word1, word2):
    # assuming word1 and word2 are cleaned
    # all uppercase, no special characters, no numbers
    # Technique -> frequency table
    # letter : count 
    freq_table = {} # empty dict
    for c in word1:
        if c in freq_table:
            freq_table[c] += 1
        else:
            freq_table[c] = 1
    for c in word2:
        if c not in freq_table:
            return False
        else:
            freq_table[c] -= 1
            if freq_table[c] < 0:
                return False
    for key, value in freq_table.items():
        if value != 0:
            return False    
    return True