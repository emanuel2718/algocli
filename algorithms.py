sorters = {"insertionsort": ("def insertionsort(arr):\n"
                             "    for i in range(1, len(arr)):\n"
                             "        key = arr[i]\n"
                             "        j = i - 1\n"
                             "        while j >= 0 and key < arr[j]:\n"
                             "            arr[j+1] = arr[j]\n"
                             "            j -= 1\n"
                             "        arr[j+1] = key\n"
                             )
           }


search = {"binarysearch": ("# iterative Algorithm:\n"
                           "def binarysearch(list, item):\n"
                           "    low = 0\n"
                           "    high = len(list)-1\n"
                           "    while low <= high:\n"
                           "        mid = (low + high)/2 \n"
                           "        guess = list[mid]\n"
                           "        if guess == item:\n"
                           "            return mid\n"
                           "        if guess > item:\n"
                           "            high = mid -1\n"
                           "        else:\n"
                           "            low = mid + 1\n"
                           "    return None\n"
                           )
          }
