from random import randrange, uniform
from unittest import TestCase

from src.DiGraph import DiGraph


class TestDiGraph(TestCase):
    def setUp(self) -> None:
        self.g = DiGraph()
        for i in range(30):
            self.g.add_node(i)
        for i in range(30):
            for j in range(1, 3):
                self.g.add_edge(i, (i + j) % 30, uniform(1.01, 2.02))

        self.g2 = DiGraph()
        for i in range(45):
            self.g2.add_node(i)
        for i in range(45):
            for j in range(1, 4):
                self.g2.add_edge(i, (i + j) % 45, uniform(1.01, 2.02))

        self.g3 = DiGraph()
        for i in range(60):
            self.g3.add_node(i)
        for i in range(60):
            for j in range(1, 5):
                self.g3.add_edge(i, (i + j) % 60, uniform(1.01, 2.02))

    def test_v_size(self):
        self.assertEqual(self.g.v_size(), 30)
        self.assertEqual(self.g2.v_size(), 45)
        self.assertEqual(self.g3.v_size(), 60)

    def test_e_size(self):
        gEdges = 30 * 2
        g2Edges = 45 * 3
        g3Edges = 60 * 4
        self.assertEqual(self.g.e_size(), gEdges)
        self.assertEqual(self.g2.e_size(), g2Edges)
        self.assertEqual(self.g3.e_size(), g3Edges)

    def test_get_all_v(self):
        self.assertTrue(type(self.g.get_all_v()), dict)
        self.assertEqual(len(self.g.get_all_v()), self.g.v_size())

    def test_get_mc(self):
        gMC = 30 + 30 * 2
        g2MC = 45 + 45 * 3
        g3MC = 60 + 60 * 4

        self.assertTrue(self.g.get_mc(), gMC)
        self.assertEqual(self.g.get_mc(), gMC)

        self.assertTrue(self.g2.get_mc(), g2MC)
        self.assertEqual(self.g2.get_mc(), g2MC)

        self.assertTrue(self.g3.get_mc(), g3MC)
        self.assertEqual(self.g3.get_mc(), g3MC)

    def test_all_in_edges_of_node(self):
        gDict = {28: self.g.edges[(28, 0)], 29: self.g.edges[(29, 0)]}
        g2Dict = {3: self.g2.edges[(3, 6)], 4: self.g2.edges[(4, 6)], 5: self.g2.edges[(5, 6)]}
        g3Dict = {6: self.g3.edges[(6, 10)], 7: self.g3.edges[(7, 10)], 8: self.g3.edges[(8, 10)],
                  9: self.g3.edges[(9, 10)]}

        self.assertEqual(self.g.all_in_edges_of_node(0), gDict)
        self.assertDictEqual(self.g.all_in_edges_of_node(0), gDict)

        self.assertEqual(self.g2.all_in_edges_of_node(6), g2Dict)
        self.assertDictEqual(self.g2.all_in_edges_of_node(6), g2Dict)

        self.assertEqual(self.g3.all_in_edges_of_node(10), g3Dict)
        self.assertDictEqual(self.g3.all_in_edges_of_node(10), g3Dict)

    def test_all_out_edges_of_node(self):
        gDict = {1: self.g.edges[(0, 1)], 2: self.g.edges[(0, 2)]}
        g2Dict = {7: self.g2.edges[(6, 7)], 8: self.g2.edges[(6, 8)], 9: self.g2.edges[(6, 9)]}
        g3Dict = {11: self.g3.edges[(10, 11)], 12: self.g3.edges[(10, 12)], 13: self.g3.edges[(10, 13)],
                  14: self.g3.edges[(10, 14)]}

        self.assertEqual(self.g.all_out_edges_of_node(0), gDict)
        self.assertDictEqual(self.g.all_out_edges_of_node(0), gDict)

        self.assertEqual(self.g2.all_out_edges_of_node(6), g2Dict)
        self.assertDictEqual(self.g2.all_out_edges_of_node(6), g2Dict)

        self.assertEqual(self.g3.all_out_edges_of_node(10), g3Dict)
        self.assertDictEqual(self.g3.all_out_edges_of_node(10), g3Dict)

    def test_add_edge(self):
        for i in range(0, 3):
            self.assertTrue(self.g.add_edge(i, i + 4, 1), True)

        for i in range(3, 6):
            self.assertTrue(self.g2.add_edge(i, i + 4, 1), True)

        for i in range(6, 9):
            self.assertTrue(self.g3.add_edge(i, i + 5, 1), True)

    def test_add_node(self):
        self.assertFalse(self.g.add_node(0), False)
        self.assertTrue(self.g.add_node(40), True)

        self.assertFalse(self.g2.add_node(0), False)
        self.assertTrue(self.g2.add_node(50), True)

        self.assertFalse(self.g3.add_node(0), False)
        self.assertTrue(self.g3.add_node(70), True)

    def test_remove_node(self):

        self.assertFalse(self.g.remove_node(500), False)
        self.assertTrue(self.g.remove_node(0), True)
        self.assertEqual(self.g.nodes.get(0), None)
        self.assertEqual(self.g.all_out_edges_of_node(0), {})
        self.assertEqual(self.g.all_in_edges_of_node(0), {})

        self.assertFalse(self.g2.remove_node(500), False)
        self.assertTrue(self.g2.remove_node(0), True)
        self.assertEqual(self.g2.nodes.get(0), None)
        self.assertEqual(self.g2.all_out_edges_of_node(0), {})
        self.assertEqual(self.g2.all_in_edges_of_node(0), {})

        self.assertFalse(self.g3.remove_node(500), False)
        self.assertTrue(self.g3.remove_node(0), True)
        self.assertEqual(self.g3.nodes.get(0), None)
        self.assertEqual(self.g3.all_out_edges_of_node(0), {})
        self.assertEqual(self.g3.all_in_edges_of_node(0), {})

    def test_remove_all_edges(self):
        self.setUp()
        self.g.removeAllEdges(0)
        self.assertEqual(self.g.all_in_edges_of_node(0), {})
        self.assertEqual(self.g.all_out_edges_of_node(0), {})

        self.g2.removeAllEdges(0)
        self.assertEqual(self.g2.all_in_edges_of_node(0), {})
        self.assertEqual(self.g2.all_out_edges_of_node(0), {})

        self.g3.removeAllEdges(0)
        self.assertEqual(self.g3.all_in_edges_of_node(0), {})
        self.assertEqual(self.g3.all_out_edges_of_node(0), {})

    def test_remove_edge(self):
        self.assertTrue(self.g.remove_edge(0, 1), True)
        self.assertTrue(self.g.remove_edge(0, 2), True)
        self.assertFalse(self.g.remove_edge(0, 50), True)

        self.assertTrue(self.g2.remove_edge(0, 1), True)
        self.assertTrue(self.g2.remove_edge(0, 2), True)
        self.assertTrue(self.g2.remove_edge(0, 3), True)
        self.assertFalse(self.g2.remove_edge(0, 50), True)

        self.assertTrue(self.g3.remove_edge(0, 1), True)
        self.assertTrue(self.g3.remove_edge(0, 2), True)
        self.assertTrue(self.g3.remove_edge(0, 3), True)
        self.assertTrue(self.g3.remove_edge(0, 4), True)
        self.assertFalse(self.g3.remove_edge(0, 50), True)

    # ===============BUILD GRAPHS===================
    def build1000(self) -> DiGraph:
        g = DiGraph()
        for i in range(1000):
            g.add_node(i)
        for i in g.nodes.keys():
            for j in range(20):
                g.add_edge(i, randrange(0, 1000), uniform(1.055, 2.971))
        return g

    def build10000(self) -> DiGraph:
        g = DiGraph()
        for i in range(10000):
            g.add_node(i)
        for i in g.nodes.keys():
            for j in range(20):
                g.add_edge(i, randrange(0, 10000), uniform(1.055, 2.971))
        return g

    def build100000(self) -> DiGraph:
        g = DiGraph()
        for i in range(100000):
            g.add_node(i)
        for i in g.nodes.keys():
            for j in range(20):
                g.add_edge(i, randrange(0, 100000), uniform(1.055, 2.971))
        return g
