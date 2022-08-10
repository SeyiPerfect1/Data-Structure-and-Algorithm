// dijkstra
const graph = {
    a: { b: 5, c: 2 },
    b: { a: 5, c: 7, d: 8},
    c: { a: 2, b: 7, d: 4, e: 8 },
    d: { b: 8, c: 4, e: 6, f: 4},
    e: { c: 8, d: 6, f: 3},
    f: { e: 3, d: 4}
}

const formatGraph = (g) => {
    const tmp = {}
    Object.keys(g).forEach((k) => {
        const obj = g[k];
        const arr = [];
        Object.keys(obj).forEach((v) => {
            arr.push({ vertex: v, cost: obj[v]})
        })
        tmp[k] = arr
    })
    return tmp
}

// console.log(formatGraph(graph))
const dijkstra = (graph, start, end) => {
    var map = formatGraph(graph)

    var visited = new set()
    var unvisited = [start]
    var shortestDistances = { [start]: { vertex: start, cost: 0 } }

    var vertex

    while (vertex = unvisited.shift()){
        // explore unvisited neighbours
        var neighbours = map[vertex].filter((n) => !visited.includes(n.vertex))

        // add neighbours to the unvisited list
        unvisited.push(...neighbours.map((n) => n.vertex))

        var costToVertex = shortestDistances[vertex].cost

        for (let {vertex: to, cost } of neighbours) {
            var currCostToNeighbour = shortestDistances[to] && shortestDistances[to].cost
            var newCostToNeigbour = costToVertex + cost
            if(currCostToNeighbour == undefined || newCostToNeigbour < currCostToNeighbour){
                //update the table
                shortestDistances[to] = {vertex, cost: newCostToNeigbour}
            }
        } 
        visited.push(vertex)
    }
}



//unionfind
class UnionFind {
    constructor(elements) {
       // Number of disconnected components
       this.count = elements.length;
 
       // Keep Track of connected components
       this.parent = {};
 
       // Initialize the data structure such that all
       // elements have themselves as parents
       elements.forEach(e => (this.parent[e] = e));
    }
 
    union(a, b) {
       let rootA = this.find(a);
       let rootB = this.find(b);
 
       // Roots are same so these are already connected.
       if (rootA === rootB) return;
 
       // Always make the element with smaller root the parent.
       if (rootA < rootB) {
          if (this.parent[b] != b) this.union(this.parent[b], a);
          this.parent[b] = this.parent[a];
       } else {
          if (this.parent[a] != a) this.union(this.parent[a], b);
          this.parent[a] = this.parent[b];
       }
    }
 
    // Returns final parent of a node
    find(a) {
       while (this.parent[a] !== a) {
          a = this.parent[a];
       }
       return a;
    }
 
    // Checks connectivity of the 2 nodes
    connected(a, b) {
       return this.find(a) === this.find(b);
    }
 }



 //Kruskal algorithm
 kruskalsMST() {
    // Initialize graph that'll contain the MST

    this.nodes.forEach(node => MST.addNode(node));
    if (this.nodes.length === 0) {
       return MST;
    }
 
    // Create a Priority Queue
    edgeQueue = new PriorityQueue(this.nodes.length * this.nodes.length);
 
    // Add all edges to the Queue:
    for (let node in this.edges) {
       this.edges[node].forEach(edge => {
          edgeQueue.enqueue([node, edge.node], edge.weight);
       });
    }
 
    let uf = new UnionFind(this.nodes);
 
    // Loop until either we explore all nodes or queue is empty
    while (!edgeQueue.isEmpty()) {
       // Get the edge data using destructuring
       let nextEdge = edgeQueue.dequeue();
       let nodes = nextEdge.data;
       let weight = nextEdge.priority;
 
       if (!uf.connected(nodes[0], nodes[1])) {
          MST.addEdge(nodes[0], nodes[1], weight);
          uf.union(nodes[0], nodes[1]);
       }
    }
    return MST;
 }


 //prims algorithm
 primsMST() {
    // Initialize graph that'll contain the MST
    const MST = new Graph();
    if (this.nodes.length === 0) {
       return MST;
    }
 
 
    // Select first node as starting node
    let s = this.nodes[0];
 
 
    // Create a Priority Queue and explored set
    let edgeQueue = new PriorityQueue(this.nodes.length * this.nodes.length);
    let explored = new Set();
    explored.add(s);
    MST.addNode(s);
 
 
    // Add all edges from this starting node to the PQ taking weights as priority
    this.edges[s].forEach(edge => {
       edgeQueue.enqueue([s, edge.node], edge.weight);
    });
 
 
    // Take the smallest edge and add that to the new graph
    let currentMinEdge = edgeQueue.dequeue();
    while (!edgeQueue.isEmpty()) {
 
 
       // COntinue removing edges till we get an edge with an unexplored node
       while (!edgeQueue.isEmpty() && explored.has(currentMinEdge.data[1])) {
          currentMinEdge = edgeQueue.dequeue();
       }
       let nextNode = currentMinEdge.data[1];
 
 
       // Check again as queue might get empty without giving back unexplored element
       if (!explored.has(nextNode)) {
          MST.addNode(nextNode);
          MST.addEdge(currentMinEdge.data[0], nextNode, currentMinEdge.priority);
          // Again add all edges to the PQ
          this.edges[nextNode].forEach(edge => {
             edgeQueue.enqueue([nextNode, edge.node], edge.weight);
          });
 
 
          // Mark this node as explored explored.add(nextNode);
          s = nextNode;
       }
    }
    return MST;
 }


