sorters = {"insertionsort": ("def insertionsort(arr):\n"
                             "    for i in range(1, len(arr)):\n"
                             "        key = arr[i]\n"
                             "        j = i - 1\n"
                             "        while j >= 0 and key < arr[j]:\n"
                             "            arr[j+1] = arr[j]\n"
                             "            j -= 1\n"
                             "        arr[j+1] = key\n"
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
                             )
           }


search = {"binarysearch": ("# iterative Algorithm:\n"
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
                           )
          }
