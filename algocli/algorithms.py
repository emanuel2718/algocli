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
                               "    return None"
                               ),
             "bogosort":      ("import random\n\n"
                               "def bogosort(arr):\n"
                               "    length = len(arr)\n"
                               "    while not is_sorted(arr):\n"
                               "        suffle(arr)\n"
                               "    return arr\n\n"

                               "def suffle(arr):\n"
                               "    length = len(arr)\n"
                               "    for i in range(0, length):\n"
                               "        rand = random.randint(0, length-1)\n"
                               "        arr[i], arr[rand] = arr[rand], arr[i]\n\n"

                               "def is_sorted(arr):\n"
                               "    length = len(arr)\n"
                               "    for i in range(0, length-1):\n"
                               "        if arr[i] > arr[i+1]:\n"
                               "            return False\n"
                               "    return True"
                               ),

             "bubblesort":    ("def bubble sort(arr):\n"
                               "    swapped = True\n"
                               "    while swapped:\n"
                               "        swapped = False\n"
                               "        for i in range(len(arr)-1):\n"
                               "            if arr[i] > arr[i+1]:\n"
                               "                arr[i], arr[i+1] = arr[i+1], arr[i]\n"
                               "                swapped = True\n"
                               "    return arr\n"
                               ),

             "cocktailsort":  ("def cocktailsort(arr):\n"
                               "    for i in range(len(arr)//2):\n"
                               "        swapped = False\n"
                               "        for j in range(1+i, len(arr)-i):\n"
                               "            if arr[j-1] > arr[j]:\n"
                               "                arr[j-1], arr[j] = arr[j], arr[j-1]\n"
                               "                swapped = True\n"
                               "        if not swapped:\n"
                               "            break\n"
                               "        swapped = False\n"
                               "        for j in range(len(arr)-i-1, i, -1):\n"
                               "            if arr[j-1] > arr[j]:\n"
                               "                arr[j-1], arr[j]  = arr[j], arr[j-1]\n"
                               "                swapped = True\n"
                               "        if not swapped:\n"
                               "            break\n"
                               "    return arr"
                               ),

             "cyclesort":     ("def cyclesort(arr):\n"
                               "    for start, item in enumerate(arr):\n"
                               "        position = start\n"
                               "        for item2 in arr[start+1:]:\n"
                               "            if item > item2:\n"
                               "                position += 1\n"
                               "        if position == start:\n"
                               "            continue\n\n"

                               "        while item == arr[position]:\n"
                               "            position += 1\n"
                               "        arr[position], item = item, arr[position]\n\n"

                               "        while position != start:\n"
                               "            position = start\n"
                               "            for item2 in arr[start+1:]:\n"
                               "                if item > item2:\n"
                               "                    position += 1\n"
                               "            while item == arr[position]:\n"
                               "                position += 1\n"
                               "            arr[position], item = item, arr[position]\n"
                               "    return arr"
                               ),

             "gnomesort":     ("def gnomesort(arr):\n"
                               "    i = 1\n"
                               "    j = 2\n"
                               "    size = len(arr)\n"
                               "    while i < size:\n"
                               "        if arr[i] >= arr[i-1]:\n"
                               "            i, j = j, j+1\n"
                               "        else:\n"
                               "            arr[i], arr[i-1] = arr[i-1], arr[i]\n"
                               "            i -= 1\n"
                               "            if i == 0:\n"
                               "                i, j = j, j+1\n"
                               "    return arr"
                               ),

             "heapsort":      ("def heapsort(arr):\n"
                               "    # heapify\n"
                               "    for start in range((len(arr)-2)//2, -1, -1):\n"
                               "        siftdown(arr, start, len(arr)-1)\n\n"

                               "    for end in range(len(arr)-1, 0, -1):\n"
                               "        arr[0], arr[end] = arr[end], arr[0]\n"
                               "        siftdown(arr, 0, end-1)\n"
                               "    return arr\n\n"

                               "def siftdown(arr, start, end):\n"
                               "    root = start\n"
                               "    while True:\n"
                               "        child = root*2+1 # left child\n\n"

                               "        if child > end:\n"
                               "            break\n"
                               "        if child+1 <= end and arr[child] < arr[child+1]:\n"
                               "            child += 1\n"
                               "        if arr[root] < arr[child]:\n"
                               "            arr[child], arr[root] = arr[root], arr[child]\n"
                               "            root = child\n"
                               "        else:\n"
                               "            break"
                               ),

             "insertionsort": ("def insertionsort(arr):\n"
                               "    for i in range(1, len(arr)):\n"
                               "        key = arr[i]\n"
                               "        j = i - 1\n"
                               "        while j >= 0 and key < arr[j]:\n"
                               "            arr[j+1] = arr[j]\n"
                               "            j -= 1\n"
                               "        arr[j+1] = key"
                               ),

             "mergesort":     ("def mergesort(arr):\n"
                               "    if len(arr) <= 1:\n"
                               "        return arr\n"
                               "    mid = len(arr) // 2\n"
                               "    left = arr[:mid]\n"
                               "    right = arr[mid:]\n\n"

                               "    left = mergesort(left)\n"
                               "    right = mergesort(right)\n"
                               "    return list(merge_helper(left, right))\n\n\n"

                               "def merge_helper(left, right):\n"
                               "    arr = []\n"
                               "    left_index, right_index = 0, 0\n\n"
                               "    while left_index < len(left) and right_index < len(right):\n"
                               "        if left[left_index] <= right[right_index]:\n"
                               "            arr.append(left[left_index])\n"
                               "            left_index += 1\n"
                               "        else:\n"
                               "            arr.append(right[right_index])\n"
                               "            right_index += 1\n\n"

                               "    if left_index < len(left):\n"
                               "        arr.extend(left[left_index:])\n"
                               "    if right_index < len(right):\n"
                               "        arr.extend(right[right_index:])\n"

                               "    return arr"
                               ),

             "quicksort":     ("def quicksort(arr):\n"
                               "    if len(arr) < 2:\n"
                               "        return arr\n"
                               "    else:\n"
                               "        pivot = arr[0]\n"
                               "        smaller = [i for i in [1:] if i <= pivot]\n"
                               "        greater = [i for i in [1:] if i > pivot]\n"
                               "   return quicksort(smaller) + [pivot] + quicksort(greater)"
                               ),
             "radixsort":     ("def radixsort(arr, index=None, size=None):\n"
                               "    if size == None:\n"
                               "        size = len(str(max(arr)))\n"
                               "    if index == None:\n"
                               "        index = size\n\n"

                               "    i = size - index\n"
                               "    if i >= size:\n"
                               "        return arr\n\n"

                               "    bins = [[] for _ in range(10)]\n"
                               "    for e in arr:\n"
                               "        dest = int(str(e).zfill(size)[i])\n"
                               "        bins[dest] += [e]\n\n"

                               "    result = []\n"
                               "    for bin in bins:\n"
                               "        if bin == []:\n"
                               "            continue\n"
                               "        result.append(radixsort(bin, index-1, size))\n\n"

                               "    flat_result = flatten(result)\n"
                               "    return flat_result\n\n"

                               "def flatten(old_list):\n"
                               "    new_list = []\n"
                               "    for i in old_list:\n"
                               "        new_list += i\n"
                               "    return new_list"
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
                               "    return temp_arr"
                               ),

             "shellsort":      ("def shellsort(arr):\n"
                                "   increment = len(arr)//2\n"
                                "   while increment:\n"
                                "       for i, element in enumerate(arr[increment:], increment):\n"
                                "           while i >= increment and arr[i-increment] > element:\n"
                                "               arr[i] = arr[i-increment]\n"
                                "               i -= increment\n"
                                "           arr[i] = element\n"
                                "       if increment == 2:\n"
                                "           increment = 1\n"
                                "       else:\n"
                                "           increment = increment*5 // 11\n"
                                "   return arr"
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

