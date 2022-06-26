class stack:
    def __init__(self, size):
        self.capacity = size
        self.arr = [None]*self.capacity
        self.top = -1

    def isFull(self):
        return self.top==self.capacity-1

    def isEmpty(self):
        return self.top==-1


    def push(self, element):
        if self.isFull():
            return 'This stack is already full'
        
        self.top+=1
        self.arr[self.top] = element

    def pop(self):
        if self.isEmpty():
            return 'stack is empty!!!'

        temp = self.arr[self.top]
        self.top-=1
        return temp

    
    def printStack(self):
        for i in range(self.top+1):
            print(self.arr[i])

# test
myStack = stack(5)
myStack.push(4)
myStack.push(9)
myStack.push(12)
myStack.push(13)
myStack.push(17)
myStack.push(20)
myStack.printStack()
myStack.pop()