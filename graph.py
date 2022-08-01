from lib2to3.pgen2.pgen import DFAState


class Node:
    ''' 
        The Node class represents each vertex of the graph 
        The attribute value represents the stored data
        The list of neighbors attribute represents the vertices with which exists a connection 
    '''
    def __init__(self, value, neighbors=None):
        self.value = value
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors

    ''' Return True if the vertex is connected with at least one vertex
    otherwiee returns false '''
    def has_neighbors(self):
        if len(self.neighbors) == 0:
            return False
        return True

    ''' Returns the number of vertices with which has a connection '''
    def number_of_neighbors(self):
        return len(self.neighbors)

    ''' Adds a new connection to the neighboor list'''
    def add_neighboor(self, neighboor):
        self.neighbors.append(neighboor)


    def __str__(self):
        returned_string = f"{self.value} -> "
        if self.has_neighbors():
            for neighboor in self.neighbors:
                returned_string += f"{neighboor[0].value} -> "  
     
        returned_string += "None"     
        return returned_string


class Graph:
    '''
        Graph class represents the graph data structure. 
        It contains a nodes attribute (list) with all the nodes of the graph
    '''
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes


    ''' Add a new node (vertex) in the grpah'''
    def add_node(self, value, neighboors=None):
        self.nodes.append(Node(value, neighboors))


    '''Return True if the node with the given value exists. Otherwise it returns False'''
    def find_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node 
        return None


    '''Add a new edge between two nodes'''
    def add_edge(self, value1, value2, weight=1):
        node1 = self.find_node(value1)        
        node2 = self.find_node(value2)

        if (node1 is not None) and (node2 is not None):
            node1.add_neighboor((node2, weight))
            node2.add_neighboor((node1, weight))
        else:
            print("Error: One or more nodes were not found")


    '''Return the number of nodes of the graph'''
    def number_of_nodes(self):
        return f"The graph has {len(self.nodes)} nodes"


    ''' Return True if the given nodes are connected. Otherwise return false'''
    def are_connected(self, node_one, node_two):
        node_one = self.find_node(node_one)
        node_two = self.find_node(node_two)

        for neighboor in node_one.neighbors:
            if neighboor[0].value == node_two.value:
                return True
        return False


    ''' Print the nodes '''
    def __str__(self):
        graph = ""
        for node in self.nodes:
            graph += f"{node.__str__()}\n" 
        return graph



#test using a social media model
# Create the graph
social_book = Graph()

# Add the nodes in the graph
social_book.add_node("John")
social_book.add_node("Mary")
social_book.add_node("Helen")
social_book.add_node("Nick")
social_book.add_node("Anne")

# Add the verices between nodes
social_book.add_edge("John", "Mary")
social_book.add_edge("John", "Nick")
social_book.add_edge("Mary", "Anne")
social_book.add_edge("Mary", "Helen")
social_book.add_edge("Anne", "Nick")
social_book.add_edge("Nick", "Helen")

# Check the connections between the users
print(f"John is connected with Mary? {social_book.are_connected('John', 'Mary')}")
print(f"John is connected with Anne? {social_book.are_connected('John', 'Anne')}")
print(f"Helen is connected with Mary? {social_book.are_connected('Helen', 'Mary')}")
print(f"Nick is connected with Mary? {social_book.are_connected('Nick', 'Mary')}")
print(f"Anne is connected with Helen? {social_book.are_connected('Anne', 'Helen')}")

# John is connected with Mary? True
# John is connected with Anne? False 
# Helen is connected with Mary? True 
# Nick is connected with Mary? False 
# Anne is connected with Helen? False

print("\nAdjacent List of hte given graph")
print(social_book)

# Adjacent List of hte given graph
# John -> Mary -> Nick -> None
# Mary -> John -> Anne -> Helen -> None
# Helen -> Mary -> Nick -> None
# Nick -> John -> Anne -> Helen -> None
# Anne -> Mary -> Nick -> Non



#Graph traversal
#BFS
# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
# Driver code
 
# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)



# DFS
# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')