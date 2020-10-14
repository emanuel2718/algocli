swap_function = ("# helper function\n"
                 "def swap(arr, i, j):\n"
                 "  arr[i], arr[j] = arr[j], arr[i]\n\n")


functions = {"binarysearch":  ("# iterative Algorithm:\n"
                               "def binarysearch(arr, item):\n"
                               "    low = 0\n"
                               "    high = len(arr)-1\n"
                               "    while low <= high:\n"
                               "        mid = (low + high)/2 \n"
                               "        guess = arr[mid]\n"
                               "        if guess == item:\n"
                               "            return mid\n"
                               "        if guess > item:\n"
                               "            high = mid -1\n"
                               "        else:\n"
                               "            low = mid + 1\n"
                               "    return None\n"
                               ),

             "insertionsort": ("def insertionsort(arr):\n"
                               "    for i in range(1, len(arr)):\n"
                               "        key = arr[i]\n"
                               "        j = i - 1\n"
                               "        while j >= 0 and key < arr[j]:\n"
                               "            arr[j+1] = arr[j]\n"
                               "            j -= 1\n"
                               "        arr[j+1] = key\n"
                               ),

             "quicksort":     ("def quicksort(arr):\n"
                               "    if len(arr) < 2:\n"
                               "        return arr\n"
                               "    else:\n"
                               "        pivot = arr[0]\n"
                               "        smaller = [i for i in [1:] if i <= pivot]\n"
                               "        greater = [i for i in [1:] if i > pivot]\n"
                               "   return quicksort(smaller) + [pivot] + quicksort(greater)\n"
                               ),

             "selectionsort": ("def findSmallestIndex(arr):\n"
                               "    smallest = arr[0]\n"
                               "    smallest_index = 0\n"
                               "    for i in range(1, len(arr)):\n"
                               "        if arr[i] < smallest:\n"
                               "            smallest = arr[i]\n"
                               "            smallest_index = i\n"
                               "    return smallest_index\n\n"

                               "def selectionSort(arr):\n"
                               "    temp_arr = []\n"
                               "    for i in range(len(arr)):\n"
                               "        smallest = findSmallestIndex(arr)\n"
                               "        temp_arr.append(arr.pop(smallest))\n"
                               "    return temp_arr\n"
                               ),

             "stoogesort":    (swap_function +
                               "# low: first index of arr\n"
                               "# high: last index of arr\n\n"
                               "def stoogesort(arr, low, high):\n"
                               "    n = high - low + 1\n"
                               "    if n == 2 and arr[low] > arr[high]:\n"
                               "        swap(arr, low, high)\n"
                               "    elif n > 2:\n"
                               "        mid = math.floor(n/3)\n"
                               "        stoogesort(arr, low, high-mid)\n"
                               "        stoogesort(arr, low+mid, high)\n"
                               "        stoogesort(arr, low, high-mid)\n"
                               "    return arr"
                               )
             }

