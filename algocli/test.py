import random
import math

#TODO: Make this into a proper test file

# QUICKSORT
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        smaller = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(smaller) + [pivot] + quicksort(greater)


# STOOGESORT
def stoogesort(arr, low, high):
    n = high - low + 1
    if n == 2 and arr[low] > arr[high]:
        swap(arr, low, high)
    elif n > 2:
        mid = math.floor(n/3)
        stoogesort(arr, low, high-mid)
        stoogesort(arr, low+mid, high)
        stoogesort(arr, low, high-mid)
    return arr

def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]


# BUBBLESORT
def bubblesort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr


# MERGESORT
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return list(merge(left, right))


def merge(left, right):
    arr = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            arr.append(left[left_index])
            left_index += 1
        else:
            arr.append(right[right_index])
            right_index += 1

    if left_index < len(left):
        arr.extend(left[left_index:])
    if right_index < len(right):
        arr.extend(right[right_index:])

    return arr


# HEAPSORT
def heapsort(arr):
    # heapify
    for start in range((len(arr)-2)//2, -1, -1):
        siftdown(arr, start, len(arr)-1)

    for end in range(len(arr)-1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        siftdown(arr, 0, end-1)
    return arr

def siftdown(arr, start, end):
    root = start
    while True:
        child = root*2+1 # left child

        if child > end:
            break
        if child+1 <= end and arr[child] < arr[child+1]:
            child += 1
        if arr[root] < arr[child]:
            arr[child], arr[root] = arr[root], arr[child]
            root = child
        else:
            break

# BOGOSORT
def bogosort(arr):
    length = len(arr)
    while not is_sorted(arr):
        suffle(arr)
    return arr

def suffle(arr):
    length = len(arr)
    for i in range(0, length):
        rand = random.randint(0, length-1)
        arr[i], arr[rand] = arr[rand], arr[i]

def is_sorted(arr):
    length = len(arr)
    for i in range(0, length-1):
        if arr[i] > arr[i+1]:
            return False
    return True




# RADIXSORT
def radixsort(arr, index=None, size=None):
    if size == None:
        size = len(str(max(arr)))
    if index == None:
        index = size
    i = size - index

    if i >= size:
        return arr
    bins = [[] for _ in range(10)]
    for e in arr:
        dest = int(str(e).zfill(size)[i])
        bins[dest] += [e]

    result = []
    for bin in bins:
        if bin == []:
            continue
        result.append(radixsort(bin, index-1, size))

    flat_result = flatten(result)
    return flat_result

def flatten(old_list):
    new_list = []
    for i in old_list:
        new_list += i
    return new_list


# GNOMESORT
def gnomesort(arr):
    i = 1
    j = 2
    size = len(arr)
    while i < size:
        if arr[i] >= arr[i-1]:
            i, j = j, j+1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
            if i == 0:
                i, j = j, j+1
    return arr



l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
random_numbers = random.sample(range(100), 5)
length = len(random_numbers)

#print(f'Array before: {random_numbers}')
#print(stoogesort(random_numbers, 0, lenght-1))
#print(radixsort(random_numbers))
#print(random_numbers)

print(f'Array before: {l}')
print(gnomesort(l))
