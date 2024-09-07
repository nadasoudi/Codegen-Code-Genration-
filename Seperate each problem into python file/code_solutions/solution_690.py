import random

def missing_number(arr):
    for i in range(10,21):
        if i not in arr:
            return i

arr = [10,20,30,40,50,60,70,80,90,100]
print(missing_number(arr))

# Output: 30

# Explanation:
# 10 is missing in the array, so it is not present in the array.
# 20 is missing in the array,