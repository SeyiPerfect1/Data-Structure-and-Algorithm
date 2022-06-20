#bubble sort algorithm which takes in an array and returns the sorted array
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1): 
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                
    return[arr]


#test
arr = [12, 3, 24, 83, 1, 29, 50, 10, 44]
bubble_sort(arr)
