# Method 2
cache = {1:1} # key is the number, each value is the length
def c_seq2(num):
    if num in cache:
        return cache[num]
    else:
        size = 1
        start = num
        while start > 1:
            # Get next num
            if start % 2 == 0:
                start = start // 2
            else:
                start *= 3
                start += 1
            # end of getting the next num
            if start in cache:
                cache[num] = size + cache[start]
                return size + cache[start]
            else:
                size += 1
        # end of while
        cache[num] = size
        return cache[num]

# Collatz
def collatz_seq(num):
    size = 1
    start = num
    while start > 1:
        if start % 2 == 0:
            start = start // 2
        else:
            start *= 3
            start += 1
        size += 1
    return size
# end of collatz_seq

import time
longest_length = 0
answer = 0
start_time = time.time()

for num in range(1, 1000000):
    #result = collatz_seq(num)
    result = c_seq2(num)
    if result > longest_length:
        longest_length = result
        answer = num

end_time = time.time()
elapsed_time = end_time - start_time

print(f"{answer} created the longest sequence with {longest_length}")
print(f"Solution took {elapsed_time:.4f} seconds")

