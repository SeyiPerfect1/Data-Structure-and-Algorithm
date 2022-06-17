#algorithm for merging two lists
def merge(arr, l, m, h):

    #divide the array into two using m and find the length of either side
    n1 = m-l+1
    n2 = h-m

    #create an array of size n1 and n2 respectively
    L = [0] * n1
    R = [0] * n2

    #copy original array into the new created array
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m+1+j]

    i = 0
    j = 0
    k = l

    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    
    while i<n1:
        arr[k] = L[i]
        i+=1
        k+=1
    
    while j<n2:
        arr[k] = R[j]
        j+=1
        k+=1
    


def mergesort(arr, l, h):
    if l<h:
        m =(l+h)//2
        mergesort(arr, l, m)
        mergesort(arr, m+1, h)
        merge(arr, l, m, h)
    return arr

    


#test
arr = [8, 5, 1, 3, 6, 2, 8, 9, 11, 10]
l = 0
h = len(arr)-1
m = (l+h)//2
mergesort(arr, l, h)
