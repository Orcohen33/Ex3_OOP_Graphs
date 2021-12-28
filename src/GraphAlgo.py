import json
import sys
from queue import *
from random import uniform

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
import matplotlib.pyplot as plt
import numpy as np


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=DiGraph()):
        self.g = graph

    def get_graph(self) -> GraphInterface:
        return self.g

    """
    :return: the directed graph on which the algorithm works on.
    """

    def load_from_json(self, file_name: str) -> bool:
        if ".json" not in file_name:
            file_name += '.json'
        try:
            with open("../data/" + file_name) as f:
                a = json.load(f)

            if "pos" in a['Nodes'][0]:
                for node in a['Nodes']:
                    self.g.nodes[node['id']] = [tuple(float(n) for n in node['pos'].split(',')), 0]
            else:
                for node in a['Nodes']:
                    self.g.nodes[node['id']] = [None, 0]

            for edge in a['Edges']:
                key = (edge['src'], edge['dest'])
                self.g.edges[key] = edge['w']
            return True
        except IOError as e:
            print(e)
            return False

    """
    This function loads a JSON file into my graph and cells the vertices and edges.
    """

    def save_to_json(self, file_name: str) -> bool:
        if ".json" not in file_name:
            file_name += '.json'
        try:
            with open("../data/" + file_name, "w") as f:

                # set dict to use for json format and iterate on all vertex and edges
                details = {"Edges": [], "Nodes": []}
                for key in self.g.edges.keys():
                    edgeDetail = {'src': key[0], 'w': self.g.edges[key], 'dest': key[1]}
                    details["Edges"].append(edgeDetail)

                for key in self.g.nodes.keys():
                    if self.g.nodes[key][0] is None:
                        nodeDetail = {'id': key}
                    else:
                        nodeDetail = {
                            'pos': f"{self.g.nodes[key][0][0]},{self.g.nodes[key][0][1]},{self.g.nodes[key][0][2]}",
                            'id': key}
                    details["Nodes"].append(nodeDetail)

                json.dump(details, indent=2, fp=f)
                return True

        except IOError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.g is None: return float('inf'), []
        if id1 not in self.g.nodes or id2 not in self.g.nodes:
            return float('inf'), []
        if id1 == id2: return 0, [id1]

        self.resetTags()
        ans = (self.Dijkstra(id1, id2))

        return ans[0], ans[1]

    """ Shortest path :
    Returns distance and shorest path between src to dest - as an oredered List of nodes :
    src -> v1 -> v2 -> ... -> dest.
    If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
    This function use Dijkstra algorithm , implemented by priority queue
    Time Complexity : O(|V|+|E|*Log|V|) ->|V| - Vertices , |E| - Edges
    """

    def Dijkstra(self, id1: int, id2: int) -> (float, list, dict):
        dists = {x: float('inf') for x in self.g.nodes}
        dists[id1] = 0

        pq = PriorityQueue()
        pq.put((0, id1))

        parent = dict()
        parent[id1] = None
        path_found = False

        while not pq.empty():
            (dist, curr) = pq.get()

            self.g.nodes[curr][1] = 1

            if self.g.all_out_edges_of_node(curr) is not None:
                for adj in self.g.all_out_edges_of_node(curr):
                    key = (curr, adj)
                    dist = self.g.edges[key]
                    if self.g.nodes[adj][1] != 1:
                        old_weight = dists[adj]
                        new_weight = dists[curr] + dist
                        if new_weight < old_weight:
                            pq.put((new_weight, adj))
                            dists[adj] = new_weight
                            parent[adj] = curr
            if curr == id2:
                path_found = True
                break

        path = []
        dest = id2
        if path_found is True:
            path.append(dest)
            while True:
                parent_node = parent[dest]
                if parent_node is None:
                    break
                path.append(parent_node)
                dest = parent_node
            path.reverse()
            ans = (dists[id2], path, dists)
            return ans
        ans = (float('inf'), [], dists)
        return ans

    def resetTags(self):
        for node in self.g.nodes.values():
            node[1] = 0
        pass

    """
    helper algorithms to shortest path :
    - Dijkstra algorithm to find the shortest path dist between two vertexes
    - resetTags to reset all tags if changed while the program run
    """

    def TSP(self, node_lst: list[int]) -> (list[int], float):

        goodPaths = {}
        mergePaths = {}
        for src in node_lst:
            for dest in node_lst:
                if src == dest: continue
                temp = self.shortest_path(src, dest)
                # (float, list)
                dist = temp[0]
                path = temp[1]
                if dist == float('inf'):
                    continue
                if all(elem in path for elem in node_lst):
                    goodPaths[dist] = path
                else:
                    mergePaths[(src, dest)] = [temp[0], temp[1]]

        if goodPaths.__len__() != 0:
            ans = min(goodPaths.keys())
            return goodPaths[ans], ans
        else:
            return self.mergeCities(node_lst, mergePaths)

    @staticmethod
    def mergeCities(node_lst: list[int], mergePaths: dict):
        i = 0
        dict_ans = {}
        for path1 in mergePaths.keys():
            for path2 in mergePaths.keys():
                if path1 is path2: continue
                if path1[1] == path2[0] and path1[0] != path2[1]:
                    pathWeight = mergePaths[path1][0] + mergePaths[path2][0]
                    key = mergePaths[path1][1] + mergePaths[path2][1][1:]
                    if all(elem in key for elem in node_lst):
                        dict_ans[pathWeight] = key
                    i += 1

        ans = min(dict_ans.keys())

        return dict_ans[ans], ans

    """  TSP:
    This method find the shortest path to travel on a given list of cities
    Each time, the algorithm searches for a route between two vertexes and checks whether the entire list of cities is 
    contained in the path.
    If not, use the helper function to consolidate routes and find the shortest route that passes through all cities.
    
    Time complexity: 
    At the worst case if the number of edges is |V|^2 -> O(V^4)
    """

    def centerPoint(self) -> (int, float):
        maxdists = {x: float('inf') for x in self.g.nodes}

        for u in maxdists:
            self.resetTags()
            temp = self.Dijkstra(u, sys.maxsize)
            dists = temp[2]
            maxdists[u] = max(dists.values())
        if float('inf') in maxdists.values():
            return -1, float('inf')

        value = min(maxdists.values())
        node_id = min(maxdists, key=maxdists.get)
        if value == float('inf'):
            node_id = -1
        return node_id, value

    """
    The method basically use dijkstra on each vertex 'u' belonging to V and take the maximum distance to dict,
    the key represent node_id and the value represent the max distance .
    This operation is performed on any vertex 'u' belonging to V.
    Finally we will select the minimum of all maximum distances and also the node id to return it.
    
    This algorithm do Dijkstra on each vertex that means :
    Time Complexity : O(|V|^2 + |V|*|E|*Log|V|)   |V| - vertexes    |E| - edges.
    """

    def plot_graph(self) -> None:
        nodes = self.g.nodes
        edges = self.g.edges
        ids, x, y = [], [], []
        if nodes[0][0] is None:
            for pos in nodes.values():
                position = (uniform(35.1901, 35.2103), uniform(32.0980, 32.1091), 0)
                pos[0] = position

        for k, v in nodes.items():
            ids.append(k)
            x.append(v[0][0])
            y.append(v[0][1])

        fig, ax = plt.subplots()

        # paint points
        ax.scatter(x, y, c='red')
        # paint edges
        for i, txt in enumerate(ids):
            ax.annotate(txt, (x[i], y[i]), c='black')

        for src, dest in edges.keys():
            x, y, _ = nodes[src][0]
            dx, dy, _ = np.array(nodes[dest][0]) - np.array(nodes[src][0])

            width = 5e-5
            plt.arrow(x, y, dx, dy, width=width, length_includes_head=True, head_width=4 * width, ec='black')

        plt.show()
