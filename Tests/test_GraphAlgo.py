from unittest import TestCase

from src.GraphAlgo import GraphAlgo
from src.GraphAlgoInterface import GraphAlgoInterface


class TestGraphAlgo(TestCase):

    def setUp(self) -> None:
        """
        for each check unmark the # of each graph.
        :return:
        """
        # gCheck - "A5.json"
        self.gCheck = GraphAlgo()
        self.gCheck.load_from_json("A5")

        # G1 - 1k nodes
        # self.g1 = GraphAlgo()
        # self.g1.load_from_json("1000nodes")

        # G2 - 10k nodes
        # self.g2 = GraphAlgo()
        # self.g2.load_from_json("10000nodes")

        # G3- 100k nodes - too much time
        # self.g3 = GraphAlgo()
        # self.g3.load_from_json("100000nodes")


    def test_get_graph(self):
        # gCheck - "A5.json"
        # self.assertTrue(type(self.gCheck.get_graph), GraphAlgoInterface)

        # G1 - 1k nodes
        # self.assertTrue(type(self.g1.get_graph()), GraphAlgoInterface)

        # G2 - 10k nodes
        # self.assertTrue(type(self.g2.get_graph), GraphAlgoInterface)

        # G3- 100k nodes - too much time
        # self.assertTrue(type(self.g3.get_graph()),GraphAlgoInterface)
        pass

    def test_load_from_json(self):
        # gCheck - "A5.json"
        self.assertTrue(self.gCheck.load_from_json("A5"), True)
        self.assertFalse(self.gCheck.load_from_json("asdfasf"), False)

        # G1 - 1k nodes
        # self.assertTrue(self.g1.load_from_json("1000nodes"), True)
        # self.assertFalse(self.g1.load_from_json("asdfasf"), False)

        # G2 - 10k nodes
        # self.assertTrue(self.g2.load_from_json("10000nodes"), True)
        # self.assertFalse(self.g2.load_from_json("asdfasf"), False)

        # G3- 100k nodes - too much time
        # self.assertTrue(self.g3.load_from_json("1000nodes"), True)
        # self.assertFalse(self.g3.load_from_json("asdfasf"), False)
        pass

    def test_save_to_json(self):
        # gCheck - "A5.json"
        self.gCheck.save_to_json("unittest")
        self.assertTrue(self.gCheck.save_to_json("unittest"), True)

        # G1 - 1k nodes
        # self.assertTrue(self.g1.save_to_json("unittest"))

        # G2 - 10k nodes
        # self.assertTrue(self.g2.save_to_json("unittest"), True)

        # G3- 100k nodes - too much time
        # self.assertTrue(self.g3.save_to_json("unittest"))
        pass

    def test_shortest_path(self):
        # gCheck - "A5.json"
        self.assertEqual(self.gCheck.shortest_path(2, 30),(6.149857110780779, [2, 3, 13, 14, 29, 30]))
        self.assertEqual(self.gCheck.shortest_path(32, 7), (9.609195174664903, [32, 31, 30, 29, 14, 13, 11, 7]))
        self.assertNotEqual(self.gCheck.shortest_path(10, 30), (5.074337685433037, [10, 3, 57, 245, 30]))

        # G1 - 1k nodes
        # self.assertEqual(self.g1.shortest_path(10, 30), (5.074337685433037, [10, 57, 245, 30]))
        # self.assertEqual(self.g1.shortest_path(2, 9), (5.6054543816853935, [2, 147, 210, 9]))
        # self.assertNotEqual(self.g1.shortest_path(10, 30), (5.074337685433037, [10, 3, 57, 245, 30]))

        # G2 - 10k nodes
        # self.assertEqual(self.g2.shortest_path(2, 6521), (float('inf'), []))
        # self.assertEqual(self.g2.shortest_path(2, 983), (3.2094839848443097, [2, 141, 983]))
        # self.assertNotEqual(self.g2.shortest_path(10, 30), (5.074337685433037, [10, 3, 57, 245, 30]))

        # G3- 100k nodes - too much time
        # self.assertEqual(self.g1.shortest_path(10, 30), (5.074337685433037, [10, 57, 245, 30]))
        # self.assertEqual(self.g1.shortest_path(2, 9), (5.6054543816853935, [2, 147, 210, 9]))
        # self.assertNotEqual(self.g1.shortest_path(10, 30), (5.074337685433037, [10, 3, 57, 245, 30]))
        pass

    def test_tsp(self):
        # gChack - "A5.json"
        self.assertEqual(self.gCheck.TSP([0, 7, 8, 9, 15]),([15, 14, 13, 11, 9, 0, 8, 7], 8.320944616970902))
        # G1 - 1k nodes
        # self.assertEqual(self.g1.TSP([0, 300, 200]),([200, 241, 62, 0, 61, 248, 201, 300], 11.338276699688258))
        # G2 - 10k nodes
        # self.assertEqual(self.g2.TSP([400,123,8]), ([123, 230, 185, 194, 27, 8, 400], 8.526415008352034))
        # G3- 100k nodes - too much time
        pass


        """1:2.057259971168178
            2:1.1641514363400272"""
    def test_center_point(self):
        # gChack - "A5.json"
        self.assertEqual(self.gCheck.centerPoint(),(40, 9.291743173960954))

        # G1 - 1k nodes
        # self.assertEqual(self.g1.centerPoint(),0)

        # G2 - 10k nodes
        # self.assertTrue(self.g2.centerPoint())

        # G3- 100k nodes - too much time
        # self.assertEqual(self.g3.centerPoint(),0)
        pass




