# Ex3_OOP_Graphs
* *Made by Or Cohen and Shlomi Lantser*

## Introduction

  In this project, we implement :
   - Directed weighted graph.
   - Algorithms on the graph,
   - Plot graph.
   - Comparing a time measurement between the graph realized here and the graph from the     previous project realized in Java.


# Implementaion

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

  
</details>

## Time analysis


|                        | 1,000 vertices | 10,000 vertices | 100,000 vertices | 1,000,000 vertices |
|:----------------------:|:--------------:|:---------------:|:----------------:|:------------------:|
|       Build Graph      |      36ms      |      1s 586ms   |     35s 11ms    |      61s 771ms     |
|         Center         |     11m 3ms    |     Timeout     |      Timeout     |       Timeout      |
|      Shortest Path     |      619ms     |     2s 39ms     |     35s 13ms      |    Out of memory  |
|           TSP          |      5s 595ms  |     30s 43ms   |     82s 7ms    |    Out of memory   |


