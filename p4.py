import math
start = 1 # hehe poopoo
num = int(input("Enter a value: "))
new_stop = int(math.sqrt(num)) + 1
factor_count = 0
while start < new_stop:
    if num % start == 0:
        dividend = num // start
        if start != dividend:
            factor_count += 2
        else:
            factor_count += 1
    start += 1
print(f"{num} has {factor_count} many factors.")