# git branching tutorial
num = int(input("Enter a number:"))
divider = 2 # changed from 1
counter = 1 # we always have 1 as a factor
#while divider < num:
while divider < int(num**0.5) + 1:
    if num % divider == 0 and divider != num // divider:
        counter += 2
    elif num % divider == 0:
        counter += 1
    divider += 1
print(f"{num} has {counter} proper factors.")