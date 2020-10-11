import random

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


def stoogesort(arr, i=0, j=None):
    if j is None:
        j = len(arr) - 1
    if arr[j] < arr[i]:
        print(f'Swapping: i={i} and j={j}')
        swap(arr, i, j)
        print(f'After swap: {arr}')
    if j-i > 1:
        temp = (j-i+1)//3
        stoogesort(arr, i, j-temp)
        stoogesort(arr, i+temp, j)
        stoogesort(arr, i, j-temp)
    return arr



random_numbers = random.sample(range(100), 10)

print(f'Array before: {random_numbers}')
print(stoogesort(random_numbers))
