import random
#the partition algorithm 
#the partition fuvtion receives three parameters
#the array, the index of the first index(l) of the array and the last index(h) of the array
#the pivot could be taken at any position but in this solution, it is taken at the last index
def partition(arr, l, h):
    #set pivot to the last array
    pivot = arr[h]
    pt = l
    for i in range(l, h):

        if arr[i]<=pivot:
            #swap
            arr[i],  arr[pt] = arr[pt], arr[i]
            pt += 1
    #swap
    arr[pt], arr[h] = arr[h],  arr[pt]
    return pt



def quicksort(arr, l, h):
    if len(arr) == 1:
        return arr
    if l<h:
        p = partition(arr, l, h)
        quicksort(arr, l, p-1)
        quicksort(arr, p+1, h)
       
    return arr
    


#test
if __name__ == "__main__":
    N = 10
    arr = [random.randint(1, 100) for i in range(N)]
    print(arr)
    print(partition(arr, 0, len(arr)-1))
    print(quicksort(arr, 0, len(arr)-1))
