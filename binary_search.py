#In a sorted array "arr", function accept tthe arr and the number to be searched
#The fuction returns the index of n if present and -1 if not
#This is the iterative process

def bin_search(arr, n):
    l = 0
    h = len(arr) - 1

    while h >= l:
        mid = (l + h)//2

        if arr[mid] > n:
            h = mid - 1

        elif arr[mid] < n:
            l = mid + 1

        else:
            return mid

    return -1


#test
if __name__ == "__main__":

    arr = [15, 17, 19, 21, 30, 33]
    bin_search(arr, 17)
    bin_search(arr, 30)
    bin_search(arr, 13)
    bin_search(arr, 35)
    



#this is the recursive approach
def rec_binary_search(arr, n, l, h):
    if h >= l:
        mid = (l + h)//2

        if arr[mid] == n:
            return mid
            
        elif arr[mid] < n:
            return rec_binary_search(arr, n, mid+1, h)

        else:
            return rec_binary_search(arr, n, l, mid-1)
            
    else:
        return -1

#Test recusive binanry search
if __name__ == "__main__":

    arr = [15, 17, 19, 21, 30, 33]
    l = 0
    h = len(arr)-1
    rec_binary_search(arr, 17, l, h)
    rec_binary_search(arr, 30, l, h)
    rec_binary_search(arr, 13, l, h)
    rec_binary_search(arr, 35, l, h)

    

    
    



