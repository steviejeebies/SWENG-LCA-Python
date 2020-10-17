# 100% test coverage

from unittest import TestCase
from BST import *


class TestBST(TestCase):
    def test_add_node_string(self):
        string_bst = BST()
        string_bst.add_node("string a")
        string_bst.add_node("string b")
        string_bst.add_node("string c")
        string_bst.add_node("string c")     # adding repeat value

        self.assertEqual("string a", string_bst.find_node("string a").key)
        self.assertEqual("string b", string_bst.find_node("string b").key)
        self.assertEqual("string b", string_bst.find_node("string b").key)
        self.assertIsNone(string_bst.find_node("string d"))

    def test_add_node_int(self):
        int_bst = BST()
        int_bst.add_node(1)
        int_bst.add_node(2)
        int_bst.add_node(3)

        self.assertEqual(1, int_bst.find_node(1).key)
        self.assertEqual(2, int_bst.find_node(2).key)
        self.assertEqual(3, int_bst.find_node(3).key)
        self.assertIsNone(int_bst.find_node(4))

    def test_find_node(self):
        int_bst = BST()
        # testing trying to find a node when no nodes are on BST
        self.assertIsNone(int_bst.find_node(1))

        # adding the node of int 1 to the tree, then attempting to find this node
        int_bst.add_node(1)
        int_bst.add_node(5)
        int_bst.add_node(3)
        self.assertEqual(1, int_bst.find_node(1).key)
        self.assertEqual(5, int_bst.find_node(5).key)
        self.assertEqual(3, int_bst.find_node(3).key)
        self.assertIsNone(int_bst.find_node(2))
        self.assertIsNone(int_bst.find_node(4))

    def test_find_lca(self):
        our_tree = BST()
        input_values = [15, 14, 28, 22, 9, 12, 30, 29, 4, 7, 13]

        for x in input_values:
            our_tree.add_node(x)

        # LCA of 12 4 is 9
        self.assertEqual(9, our_tree.find_lca(12, 4), "test")
        # LCA of 7 4 is 4
        self.assertEqual(4, our_tree.find_lca(7, 4))
        # LCA of 14 22 is 15
        self.assertEqual(15, our_tree.find_lca(14, 22))
        # LCA of 15 4 is 15
        self.assertEqual(15, our_tree.find_lca(15, 4))
        # LCA of 30 29 is 30
        self.assertEqual(30, our_tree.find_lca(30, 29))
        # LCA of 7 13 is 9
        self.assertEqual(9, our_tree.find_lca(7, 13))
        # LCA of 30 99 (99 not on tree) is 30
        self.assertEqual(30, our_tree.find_lca(30, 99))
