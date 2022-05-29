from singlyLinkedList import Node, LinkedList

def mergeLists(firstList, secondList, mergedList):
    currentFirst = firstList.Head
    currentSecond = secondList.Head
    while True:
        if currentFirst is None:
            mergedList.append(currentSecond)
            break

        if currentSecond is None:
            mergedList.append(currentFirst)
            break

        if currentFirst.data < currentSecond.data:
            currentFirstNext = currentFirst.next
            currentFirst.next = None
            mergedList.append(currentFirst)
            currentFirst =  currentFirstNext

        else:
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mergedList.append(currentSecond)
            currentSecond = currentSecondNext


#FIRSTLIST
firstNode = Node(4)
secondNode = Node(6)
thirdNode =  Node(8)
firstList = LinkedList()
firstList.append(firstNode)
firstList.append(secondNode)
firstList.append(thirdNode)


#SECONDLIST
fourthNode = Node(5)
fifthNode = Node(7)
sixthNode = Node(9)
secondList =  LinkedList()
secondList.append(fourthNode)
secondList.append(fifthNode)
secondList.append(sixthNode)

#MERGEDLIST
mergedList = LinkedList()


firstList.printList()
secondList.printList()

mergeLists(firstList, secondList, mergedList)

del firstList
del secondList

mergedList.printList()







