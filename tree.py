class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, new_Node):
        if self.root is None:
            self.root = Node(new_Node)

        else:
            self._insert(new_Node, self.root)


    def _insert(self, value, currentNode):
        if value<currentNode.data:
            if currentNode.left is None:
                currentNode.left = Node(value)

            else:
                self._insert(value, currentNode.left)

        elif value>currentNode.data:
            if currentNode.right is None:
                currentNode.right = Node(value)

            else:
                self._insert(value, currentNode.right)

        else:
            return "data already exists"



    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, currentNode):
        if currentNode:
            self._inorder_print_tree(currentNode.left)
            print(currentNode.data)
            self._inorder_print_tree(currentNode.right)


    # deletion

    def _minvalueNode(self, currentNode):
        while currentNode.left:
            current = currentNode.left
        return current


    # def delete(self, key):
    #     if self.root is None:
    #         return
    #     else:
    #         self._delete(key, self.root)


    # def _delete(self, key, currentNode):
        
    #     if key<currentNode.data:
    #         self._delete(key, currentNode.left)

    #     elif key>currentNode.data:
    #         self._delete(key, currentNode.right)

    #     else:
    #         if currentNode.left is None:
    #             temp = currentNode.right
    #             currentNode  = temp
    #             currentNode.right = None
    #             return temp

    #         elif currentNode.right is None:
    #             temp = currentNode.left
    #             currentNode  = temp
    #             currentNode.left = None
    #             return temp

    #         elif currentNode.right is None and currentNode.left is None:
    #             currentNode = None

    #         # node with two children
    #         #get the inorder succesor, that is, the smallest node in the right subtree
    #         else:
    #             temp = self._minvalueNode(currentNode.right)
    #             currentNode = temp
    #             return temp


    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, currentNode):
        if data > currentNode.data and currentNode.right:
            return self._find(data, currentNode.right)
        elif data < currentNode.data and currentNode.left:
            return self._find(data, currentNode.left)
        if data == currentNode.data:
            return True
            



        



   




# test
myTree = Tree()
myTree.insert(40)
myTree.insert(20)
myTree.insert(10)
myTree.insert(25)
myTree.insert(30)
myTree.insert(22)
myTree.insert(50)
myTree.inorder_print_tree()
myTree.delete(10)






    



        