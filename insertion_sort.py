#an insertion sort function that takes in an array and return the sorted array
from array import array


def insertionSort(arr):
    for i in range (1, len(arr)):
        key = arr[i]
        j = i - 1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr



#test
arr = [10, 2, 11, 5, 6, 1, 8, 9, 7, 3, 4, 16, 17, 14, 15]
insertionSort(arr)
