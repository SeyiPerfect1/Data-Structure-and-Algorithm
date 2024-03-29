# implementation of queue data structure initializing with the capacity of the queue
class queue:
    def __init__(self, size):
        self.size = size
        self.arr = [None]*self.size
        self.front = -1
        self.rear = -1


    def add(self, element):
        if (self.rear == self.size-1):
            return "queue is already full"

        if (self.rear == -1):
            self.rear=0
            self.front=0
            self.arr[self.rear]=element
            return

        self.rear+=1
        self.arr[self.rear]=element


    def delete(self):
        if(self.rear==-1):
            return 'The queue is empty'

        if(self.front==self.rear):
            temp = self.arr[self.front]
            self.front=-1
            self.rear=-1
            return temp

        temp = self.arr[self.front]
        self.front+=1
        return temp


    def printQueue(self):
        for i in range(self.front, self.rear+1):
            print(self.arr[i])


# #test
# myQueue = queue(5)
# myQueue.add(4)
# myQueue.add(9)
# myQueue.add(12)
# myQueue.add(13)
# myQueue.add(17)
# myQueue.add(20)
# myQueue.printQueue()
# myQueue.delete()
# myQueue.printQueue()


#Circular queue
    def addCircularQueue(self, element):
        if (self.rear == self.size-1):
            return "queue is already full"

        if (self.rear == -1):
            self.rear=0
            self.front=0
            self.arr[0]=element
            return

        self.rear+=1%len(self.arr)
        self.arr[self.rear]=element


    def deleteCircularQueue(self):
        if(self.rear==-1):
            return 'The queue is empty'

        if(self.front==self.rear):
            temp = self.arr[self.front]
            self.front=-1
            self.rear=-1
            return temp

        temp = self.arr[self.front]
        self.front+=1%len(self.arr)
        return temp


# #test
# myQueue = queue(5)
# myQueue.addCircularQueue(4)
# myQueue.addCircularQueue(9)
# myQueue.addCircularQueue(12)
# myQueue.addCircularQueue(13)
# myQueue.addCircularQueue(17)
# myQueue.addCircularQueue(20)
# myQueue.printQueue()
# myQueue.deleteCircularQueue()
# myQueue.printQueue()


