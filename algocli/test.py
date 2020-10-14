import random
import math

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



random_numbers = random.sample(range(100), 10)
lenght = len(random_numbers)

print(f'Array before: {random_numbers}')
print(stoogesort(random_numbers, 0, lenght-1))