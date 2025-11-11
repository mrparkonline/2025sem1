# CHALLENGE
def sort_it(a_list, b_list):
    pass



# Non-Destructive Selection Sort with Lists
def select(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        i = 0
        while i < len(a_list):
            smallest = a_list[i] # then prove it is or it is not
            # lets go hunting
            j = i + 1 # search from i + 1 onwards
            new_location = i # initialize to i
            while j < len(a_list):
                new_value = a_list[j]
                if new_value < smallest:
                    smallest = new_value
                    new_location = j
                j += 1
            # end of hunting
            # swap the smallest into the proper location
            temporary = a_list[i]
            a_list[i] = smallest
            a_list[new_location] = temporary
            # Python way
            #a_list[i], a_list[new_location] = a_list[new_location], a_list[i]
            i += 1
        return a_list
# end of select

def bubble(a_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(a_list)):
            if a_list[i-1] > a_list[i]:
                swapped = True
                a_list[i-1], a_list[i] = a_list[i], a_list[i-1]
        # end of inner for
    # end of outer while
    return a_list

def inserty(a_list):
    i = 1
    while i < len(a_list):
        j = i
        while j > 0:
            if a_list[j-1] > a_list[j]:
                a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
            else:
                break
            j -= 1 # j = j - 1
        i += 1













# def bubble(a_list):
#     swap_happened = True
#     while swap_happened:
#         swap_happened = False
#         i = 1
#         while i < len(a_list):
#             left = a_list[i-1]
#             right = a_list[i]
#             if left > right:
#                 swap_happened = True
#                 a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
#             i += 1
#     return a_list

# def inserty(a_list):
#     i = 1
#     while i < a_list:
#         j = i
#         while j > 0:
#             if a_list[j] > a_list[j-1]:
#                 a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
#             else:
#                 break
#             j -= 1
#         i += 1
#     return a_list
