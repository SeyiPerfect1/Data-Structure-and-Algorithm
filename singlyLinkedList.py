class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.Head = None

    def listLength(self):
        currentNode = self.Head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length



    def append(self, newNode):
        if self.Head is None:
            self.Head = newNode
        else:
            currentNode = self.Head
            while True:
                if currentNode.next is None:
                    break
                currentNode = currentNode.next
            currentNode.next = newNode
        



    def printList(self):
        if self.Head is None:
            print('List is empty!!!')
            return
        currentNode = self.Head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next
        # while True:
        #     if currentNode is None:
        #         break
        #     print(currentNode.data)
        #     currentNode = currentNode.next


    def insertHead(self, newArray):
        temporaryNode = self.Head
        self.Head = newArray
        self.Head.next = temporaryNode
        del temporaryNode


    def insertAt(self, newNode, position):
        if position<0 or position>self.listLength():
            print('invalid Node position!!!')
            return
        
        if position == 0:
            linkedList.insertHead(newNode)
            return

        currentNode = self.Head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode

                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    
    def delete(self):
        if self.Head is None:
            print('Empty List!!!')
            return

        lastNode = self.Head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None
        # return linkedList.printList()


    def isListEmpty(self):
        if self.Head is None:
            return True
        else:
            return False

    
    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead = self.Head
            self.Head = self.Head.next
            previousHead = None
            return linkedList.printList()
        else:    
            print('Empty List!!!')
            return


    def deleteAt(self, position):
        if position<0 or position>=self.listLength():
            print('wrong position!!!')
            return

        if self.isListEmpty() is False:
            if position is 0:
                self.deleteHead()
                return
            lastNode = self.Head
            currentposition = 0
            while True:
                if currentposition == position:
                    previousNode.next = lastNode.next
                    lastNode.next = None
                    break
                previousNode = lastNode
                lastNode = lastNode.next
                currentposition += 1
            # return linkedList.printList()

        else:
            print('Empty List!!!')
            return





            



firstNode = Node('Oluseyi')
linkedList = LinkedList()
linkedList.append(firstNode)
secondNode = Node('Adeoye')
linkedList.append(secondNode)
thirdNode = Node('Emmanuel')
linkedList.insertHead(thirdNode)
fourthNode = Node('Adeegbe')
linkedList.insertAt(fourthNode, 1)

# linkedList.printList()

