import random
import math

#TODO: Make this into a proper test file

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        smaller = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(smaller) + [pivot] + quicksort(greater)

def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]


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


def bubblesort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr


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



random_numbers = random.sample(range(100), 10)
lenght = len(random_numbers)

print(f'Array before: {random_numbers}')
#print(stoogesort(random_numbers, 0, lenght-1))
print(mergesort(random_numbers))
