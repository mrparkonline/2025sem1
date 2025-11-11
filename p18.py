a_list = [1,1,2,3,4,5,6,9]
target = 6
# method 5 beats all the previous methods

def two_pointer(array, goal):
    left = 0
    right = len(array) - 1
    while left < right:
        total = array[left] + array[right]
        if total == goal:
            return True
        else:
            if total < goal:
                left += 1
            else:
                right -= 1
    return False 


# method 3 --> linear search method (method 3 would be improved)
# with binary search since a_list is guaranteed to be sorted
for i in range(len(a_list)-1):
    diff = target - a_list[i]
    for j in range(i+1, len(a_list)):
        if a_list[j] == diff:
            print(f"{target} happens at ({i}, {j})")

# method 2
for i in range(len(a_list)-1):
    for j in range(i+1, len(a_list)):
        if (a_list[i] + alist[j]) == target:
            print(f"{target} happens at ({i}, {j})")

# method 1
for i in range(len(a_list)):
    for j in range(len(a_list)):
        if i != j and (a_list[i] + alist[j]) == target:
            print(f"{target} happens at ({i}, {j})")
