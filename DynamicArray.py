import ctypes

class DynamicArray(object):
    
    def __init__(self):  
        self.n = 0                  #count the actual number of element
        self.capacity = 1           #capacity of the array
        self.A = self.make_array(self.capacity)
        

    def __len__(self):
        return self.n


    def __getitem__(self, k):
        if not 0<= k <=self.n:
            return IndexError('k is out of bounds')
        
        return self.A[k]
        

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
            
        self.A[self.n] = ele
        self.n += 1
        


    def insertAt(self, item, index):
        if index<0 or index>self.n:
            print('please enter the appropriate index')
        
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        
        for i in range(self.n-1, index-1, -1):
            self.A[i+1] = self.A[i]
            '''
            for val in range(10, 1, -2):
                print(val, end=',')
            
            output = 10, 8, 6, 4, 2
            '''
        self.A[index] = item
        self.n+=1
        


    def delete(self):
        if self.n == 0:
            print('Array is empty, deletion not possible')
            return
        
        self.A[self.n-1] = 0
        self.n-=1
        


    def removeAt(self, index):
        if self.n == 0:
            print('Array is empty, deletion not possible')
            
        if index<0 or index>=self.n:
            print('please enter the appropriate index')
            
        if index == self.n-1:
            self.A[index] = 0
            self.n-=1
            return
        
        for i in range(index, self.n-1):
            self.A[i] = self.A[i+1]
            
        self.A[self.n-1] = 0
        self.n-=1
        

    def _resize(self, new_cap):
        B = self.make_array(new_cap)
    
        for k in range(self.n):
            B[k] = self.A[k]
    
        self.A = B
        self.capacity = new_cap
    


    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()




myList = DynamicArray()    

myList.append(3)
print(myList)

myList.__len__()

myList.append(4)

myList.__len__()

myList.delete()

myList.__len__()

myList.insertAt(22, 1)
myList.__len__()
myList.__getitem__(1)



    
    
    
            
        
        
        
        
        
        
        