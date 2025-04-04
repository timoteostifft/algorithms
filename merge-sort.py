import random

def merge_sort(array: list[int]):
    if len(array) == 1: 
       return array
    
    mid = len(array) // 2

    left = merge_sort(array[:mid])
    right =  merge_sort(array[mid:])

    return merge(left, right)

def merge(left: list[int], right: list[int]):
    merge = []
  
    i = 0
    j = 0

    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1

    merge.extend(left[i:])
    merge.extend(right[j:])

    return merge
    
numbers = list(range(1, 101))

random.shuffle(numbers)
    
sort = merge_sort(numbers)

print(sort)