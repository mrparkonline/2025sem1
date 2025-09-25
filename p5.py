# git branching tutorial
num = int(input("Enter a number:"))
divider = 1
counter = 0
while divider < num:
    if num % divider == 0:
        counter += 1
    divider += 1
print(f"{num} has {counter} proper factors.")