# Ex3_OOP_Graphs
* *Made by Or Cohen and Shlomi Lantser*

## Introduction

  In this project, we implement :
   - Directed weighted graph.
   - Algorithms on the graph,
   - Plot graph.
   - Comparing a time measurement between the graph realized here and the graph from the     previous project realized in Java.


# implementation


* We were required in the current project to implements interfaces.

The interfaces are :

| *Interfaces* | *Details* | 
|--------------|-----------|
|GraphInterface|Represent a directional weighted graph|
|GraphAlgoInterface|Represent a directional weighted graph theory algorithms|

## DiGraph class : Implement GraphInterface
<details>
  <summary>Click to expand</summary>
 
  
   ##### Each DiGraph contains two fields:
   - Nodes :
     - Key - Contain vertex id
     - Value - Contain a list of 2 variables: 
       - Tuple - Position in space (x,y,z)
       - Int - A variable to to use in algorithms (tag)
   - Edges :
     - Key - Contain tuple (src,dest) that represet directed edge.
     - Value - Contain weight (float)
  
  
  
| *Methods* | *Details* | *Time complexity* |
|--------------------|-----------|--------|
| `v_size()`    |Returns the number of vertices in this graph|O(1)|
| `e_size()` | Returns the number of edges in this graph |O(1)|
| `get_all_v()` | Returns a dictionary of all the nodes in the Graph, each node is represented using a pair(node_id, node_data)|O(\|V\|) : \|V\| = num of nodes|
| `all_in_edges_of_node(id1: int)`   | Returns a dictionary of all the nodes connected to (into) id1 ,each node is represented using a pair (other_node_id, weight)|O(k) : k = num of in edges of given id|
| `all_out_edges_of_node(id1: int)`  | Returns a dictionary of all the nodes connected from id1 , each node is represented using a pair (other_node_id, weight)|O(k) : k = num of out edges of given id|
| ` get_mc() ` | Returns the current version of this graph , on every change in the graph state - the MC should be increased|O(1)|
| `add_edge(id1: int, id2: int, weight: float)`  | Returns true if the edge was added successfully or just updated weight of curr edge given, else return false|O(1)|
| `add_node(node_id: int, pos: tuple = None)`| Returns true if the node was add successfully else return false if the node id already exists|O(1)|
| `remove_node(node_id: int)`| Returns true if the node was successfully removed and all edges were inside and outside this node were also deleted , otherwise return false|O(k) : k = all out and in edges of given node id|
| ` remove_edge(node_id1: int , node_id2: int) `| Returns true if the edge was successfully removed , otherwise false returns|O(1)|
 
  
</details>

## GraphAlgo class : implement GraphAlgoInterface
<details>
  <summary>Click to expand</summary><br/>
  
  This class represents a directed (positive) weighted Graph and implement Theory Algorithms including: init, shortedPath , center , tsp and save&load with JSON file.

  
 ##### Each GraphAlgo contain DiGraph
  
| *Methods* | *Details* | *Time complexity* |
|--------------------|-----------|--------|
|`get_graph()`| Return the directed weighted graph on which the algorithms work on|O(1)|
|`load_from_json`|Return true if load successfuly else false | O(\|V\| + \|E\|) \|V\|=Vertices  \|E\|=Edges|
|`save_from_json`|Return true if save successfuly else false | O(\|V\| + \|E\|) \|V\|=Vertices  \|E\|=Edges|
|`shortest_path(id1: int, id2: int)`|Return (float,list) ,float- represent weight of path, list- represent shorest path between id1 to id2| O(\|V\| + \|E\|*Log\|V\|) \|V\|=Vertices  \|E\|=Edges| 
|`TSP(node_lst: list[int])`|Return (list[int],float) ,list[int] - represent path between all cities, float - represent weight of path |Worst case if the number of edges is \|V\|^2 -> O(V^4)|
|`centerPoint()`|Return (int,float) ,int - node id of the center ,float - Lowest of all maximum distances|O(\|V\|^2 + \|V\|*\|E\|*Log\|V\|) \|V\|=Vertices  \|E\|=Edges|
  
  
### Algorithm explanation
  
  ```shortestPath(id1: int,id2: int)```
  <details>
  <summary>Explanation</summary>
   
   Checks what is the shortest path distance between given id1,id2∈V , This algorithm used Dijkstra.  
    
   Dijkstra check what is the lower weight path to get from u to v.
   
   In this program i implemented dijkstra with priority queue , which decrease the time complexity.
    
  - What is it actually does?  
    
    1. Set the "id1" node weight 0.
    2. Start to explore his neighbors.
    3. Therefore, we will see if the weight of the neighbor is greater than the weight of this vertex and the weight of the tip that connects them.
If so we will change the weight of the neighbor at the vertex weight + the weight of the edge.

    4. Once we come across a neighbour who is also our destination , we will update his weight if necessary and return the weight of the neighbor who is also the destination.
    5. If the weight isnt -1 it means that there is a path between given source and destination.
   
    ![Dijkstra](https://user-images.githubusercontent.com/92351152/145614084-391100ad-325b-4cec-951d-19c9a81dc01e.gif)
    
   This algorithm also return the shorest path between id1 to id2 - as an oredered List of nodes :id1 -> v1 -> v2 -> ... -> id2.
    
   Time complexity = O(|V|+|E|*Log|V|) -> |V| = size of vertexes , |E| = size of edges.
    
</details>
  
  ```centerPoint()```
  
 <details>
 <summary>Explanation</summary>
      
   The method basically takes vertex 'u' and checks its distance from each vertex 'v' belonging to V
      
   and saves the maximum distance from vertex 'u' to 'v' in a data format.
      
   This operation is performed on any vertex 'u' belonging to V.
      
   Finally we will select the minimum of all maximum distances and also the node id to return it.
      
    Time Complexity : O(|V|^4)   |V| - vertexes. (At the worst case if |E|=|V|^2)
      
</details>
  
  ```TSP(node_lst: list[int])```
  
  <details>
  <summary>Explanation</summary>
  
  The TSP algorithm used to look for the shortest path between all given cities and return the path and his weight.
    
  The algorithm searches all the paths between u,v ∈ node_lst .
    
  If all the nodes in node_lst contain in one of the paths and his weight is the minimized then the algorithm returns it .
    
  Else ,  all the ‘mergePaths’ go to helper algorithm that merge the good paths and returns the one with the minimized weight and.

      
      
  Time Complexity : O(|V|^4)   |V| - vertexes. (At the worst case if |E|=|V|^2)
      
  </details>
 </details> 

## Time analysis


|                        | 1,000 vertices | 10,000 vertices | 100,000 vertices | 1,000,000 vertices |
|:----------------------:|:--------------:|:---------------:|:----------------:|:------------------:|
|       Build Graph      |      36ms      |      1s 586ms   |     35s 11ms    |      61s 771ms     |
|         Center         |     11m 3ms    |     Timeout     |      Timeout     |       Timeout      |
|      Shortest Path     |      619ms     |     2s 39ms     |     35s 13ms      |    Out of memory  |
|           TSP          |      5s 595ms  |     30s 43ms   |     82s 7ms    |    Out of memory   |


## Compare times

We required to compare times between java project to this project
I made graphs that represent each algorithm with 1k,10k,100k,1m nodes:
(0 means TimeOut)</br>

![CompareRunningTimes2](https://user-images.githubusercontent.com/92351152/147502207-0d2bd310-a1a3-4442-82b2-b1f25ee36c07.jpg)


## How to run

- Open cmd in the project folder ()
