"""
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
    1. The elements of the first array are all factors of the integer being considered
    2. The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.
"""

def getTotalX(arr, brr):
    m = max(arr+brr)
    factors = []
    for i in range(max(arr), min(brr)+1):
        if m % i == 0:
            factors.append(i)
    copy = factors.copy()
    for i in factors:
        for a in arr:
            if i % a != 0:
                copy.remove(i)
                break
        if i in copy:
            for b in brr:
                if b % i != 0:
                    copy.remove(i)  
                    break    
    return len(copy)

arr = [3, 4]
brr = [24, 48]

print(getTotalX(arr, brr))