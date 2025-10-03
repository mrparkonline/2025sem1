# Perfect Number
def is_perfect(num):
    divider = 1
    total = 0
    while divider < num:
        if num % divider == 0:
            total += divider # total = total + divider
        divider += 1
    return total == num
# end of is_perfect()
num = 1
while num <= 1000000:
    if is_perfect(num):
    #if is_perfect(num) == True:
        print(f"{num} is perfect.")
    num += 1