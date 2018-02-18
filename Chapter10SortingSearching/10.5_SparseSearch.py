# Given a sorted array of strings that is interspersed with empty strings
# write  a method tha will return the index of a given string

# Ex. Input: ball, {"at","","","",ball,"",cat}

import math
import pdb


def SearchHelper(start, end, word, arr):
    mid = int(math.floor((end + start) / 2))
    mid_left = mid
    mid_right = mid
    current_left = arr[mid_left]
    current_right = arr[mid_right]
    # iterate left and right until we find a non empty string
    while(arr[mid_left] is '' and arr[mid_right] is ''):
        mid_left -= 1
        mid_right += 1
    if(arr[mid_left]):
        if(arr[mid_left] == word):
            return mid_left
        elif (word < arr[mid_left]):
            return SearchHelper(start, mid_left - 1, word, arr)
        else:
            return SearchHelper(mid_left + 1, end, word, arr)
    else:
        if(arr[mid_right] == word):
            return mid_right
        elif (word < arr[mid_right]):
            return SearchHelper(start, mid_right - 1, word, arr)
        else:
            return SearchHelper(mid_right + 1, end, word, arr)


def SearchStringSortedArray(word, arr):
    return SearchHelper(0, len(arr), word, arr)


target = "fido"
inArr = ["ann", "", "", "cat", "", "dog", "", "fido", "lee"]
x = SearchStringSortedArray(target, inArr)
print x
