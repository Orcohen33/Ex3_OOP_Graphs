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
  
  
   - In this class I decided to store the vertex data in dict :
     - Key - Contain vertex id
     - Value - Contain a list of 2 variables: 
        - Tuple - Position in space (x,y,z)
        - Int - A variable to to use in algorithms (tag)
  
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
