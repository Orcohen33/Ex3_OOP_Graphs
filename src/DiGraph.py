from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self, nodes=[], edges=[]):
        self.nodes = {}
        for node in nodes:
            if 'pos' in node:
                self.nodes[node['id']] = [tuple([float(n) for n in (node['pos'].split(','))]), 0, 0]
            else:
                self.nodes[node['id']] = [None, 0, 0]

        self.edges = {}
        for edge in edges:
            self.edges[(edge['src'], edge['dest'])] = edge['w']

        self.mc = 0

    def v_size(self) -> int:
        return len(self.nodes)

    """
    Returns the number of vertices in this graph
    @return: The number of vertices in this graph
    """

    def e_size(self) -> int:
        return len(self.edges)

    """
    Returns the number of edges in this graph
    @return: The number of edges in this graph
    """

    def get_all_v(self) -> dict:
        all_v = {x: None for x in self.nodes}

        for node in self.nodes:
            outE = len(self.all_out_edges_of_node(node))
            inE = len(self.all_in_edges_of_node(node))
            all_v[node] = {node: f"|edges out| {outE} |edges in| {inE}"}
        return all_v

    """
    return a dictionary of all the nodes in the Graph, each node is represented using a pair
    (node_id, node_data)
    """

    def get_mc(self) -> int:
        return self.mc

    """
    Returns the current version of this graph,
    on every change in the graph state - the MC should be increased
    @return: The current version of this graph.
    """

    def all_in_edges_of_node(self, id1: int) -> dict:
        ans = {}
        for x in self.edges.keys():
            if x[1] is id1:
                ans[x[0]] = self.edges[x]
        return ans

    """return a dictionary of all the nodes connected to (into) node_id ,
    each node is represented using a pair (other_node_id, weight)
     """

    def all_out_edges_of_node(self, id1: int) -> dict:
        ans = {}
        for x in self.edges.keys():
            if x[0] is id1:
                ans[x[1]] = self.edges[x]
        return ans

    """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
    (other_node_id, weight)
    """

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        key = (id1, id2)
        if key in self.edges.keys():
            self.edges[key] = weight
            self.mc += 1
            return True
        self.edges[key] = weight
        self.mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes.keys(): return False
        if pos is None:
            self.nodes[node_id] = [None, 0, 0]
        else:
            self.nodes[node_id] = [pos, 0, 0]
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes.keys(): return False
        self.removeAllEdges(node_id)
        self.nodes.pop(node_id)
        self.mc += 1
        return True

    def removeAllEdges(self, node_id: int):
        tempEdges = self.edges.copy()
        if len(self.all_out_edges_of_node(node_id)) != 0:
            for key in tempEdges:
                if key[0] is node_id:
                    self.edges.pop(key)
                elif key[1] is node_id:
                    self.edges.pop(key)

    """help function to remove node"""

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        key = (node_id1, node_id2)
        if key not in self.edges.keys(): return False
        self.edges.pop(key)
        self.mc += 1
        return True

    def __repr__(self):
        return f"Graph: |V|={len(self.nodes)} , |E|={len(self.edges)}"
