class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None



class doublyLinkedList:
    def __init__(self):
        self.head = None


    #Insertion
    def insertHead(self, new_Node):
        cur = self.head
        if not self.head:
            newNode = Node(new_Node)
            self.head = newNode
            

        else:
            newNode = Node(new_Node)
            cur.prev = newNode
            newNode.next = cur
            self.head = newNode



    def append(self, new_Node):
        cur = self.head
        
        if  not cur:
            newNode = Node(new_Node)
            doublyLinkedList.insertHead(newNode)
            return

        else:
            while cur.next:
                cur = cur.next
            newNode = Node(new_Node)
            cur.next = newNode
            newNode.prev = cur
            newNode.next = None





    def insertBefore(self, key, new_Node):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # newNode = Node(new_Node)
                self.insertHead(new_Node)
                return
        
            elif cur.data == key:
                prev = cur.prev
                newNode = Node(new_Node)
                prev.next = newNode
                newNode.prev = prev
                newNode.next = cur
                cur.prev = newNode
            cur = cur.next



    def insertAfter(self, key, new_Node):
        cur = self.head
        while cur:
            if cur.data == key and cur.next is None:
                # newNode = Node(new_Node)
                self.append(new_Node)
                return

            elif cur.data == key and cur.next is not None:
                next = cur.next
                newNode = Node(new_Node)
                cur.next = newNode
                newNode.prev = cur
                newNode.next = next 
                next.prev = newNode
            cur = cur.next

    def listLength(self):
        cur = self.head
        Length = 0
        while cur:
            cur = cur.next
            Length += 1
        return Length

    def insertAt(self, position, new_Node):
        cur = self.head
        if position<0 or position>self.listLength():
            print('invalid position')
            return

        elif position == 0:
            self.insertHead(new_Node)
            return


        else:
            curPosition = 0
            while True:
                if position==self.listLength():
                    self.append(new_Node)
                    break

                if curPosition == position:  
                    newNode = Node(new_Node)               
                    cur.prev = newNode
                    prev.next = newNode 
                    newNode.prev = prev
                    newNode.next = cur
                    break
                prev = cur
                cur = cur.next
                curPosition += 1

    #Deletion

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data==key and cur==self.head:
                #case1
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                #case2
                else:
                    next = cur.next
                    cur.next = None
                    next.prev = None
                    cur = None
                    self.head = next 
                    return

            #case3
            elif cur.data==key:
                if not cur.next:
                    prev = cur.prev
                    cur.prev = None
                    prev.next = None
                    cur = None
                    return

            #case4
                else:
                    prev = cur.prev
                    next = cur.next
                    prev.next = next
                    next.prev = None
                    cur.prev = None
                    cur.next = None
                    cur = None
                    return
            cur = cur.next 



        
    def printList(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next




        






            