class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next=next

class circularLinkedlist:
    def __init__(self):
        self.head = None

    #insertion
    def insertHead(self, new_Node):
        if not self.head:
            newNode =  Node(new_Node)
            self.head = newNode
            self.head.next = self.head
           
            
        else:
            cur = self.head
            newNode =  Node(new_Node)
            newNode.next = cur
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            self.head = newNode
                
               


    def append(self, new_Node):
        if not self.head:
            newNode =  Node(new_Node)
            self.head = newNode
            self.head.next = self.head
           

        else:
            newNode =  Node(new_Node)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head

    #deletion
    def delete(self, key):
        if self.head.data==key:
            cur = self.head
            while cur.next!=self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next  = cur.next
                    cur = cur.next


    #print
    def printList(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break
            
linkedlist = circularLinkedlist()
# linkedlist.insertHead(5)
# linkedlist.printList() 
# linkedlist.append(10)  
