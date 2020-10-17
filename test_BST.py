from unittest import TestCase
from BST import *


class TestBST(TestCase):
    def test_add_node_string(self):
        string_bst = BST()
        string_bst.add_node("string a")
        string_bst.add_node("string b")
        string_bst.add_node("string c")

        self.assertEqual("string a", string_bst.find_node("string a").key)
        self.assertEqual("string b", string_bst.find_node("string b").key)
        self.assertEqual("string b", string_bst.find_node("string b").key)
        self.assertIsNone(string_bst.find_node("string d"))

    def test_add_node_int(self):
        string_bst = BST()
        string_bst.add_node(1)
        string_bst.add_node(2)
        string_bst.add_node(3)

        self.assertEqual(1, string_bst.find_node(1).key)
        self.assertEqual(2, string_bst.find_node(2).key)
        self.assertEqual(3, string_bst.find_node(3).key)
        self.assertIsNone(string_bst.find_node(4))

    def test_find_lca(self):
        our_tree = BST()
        input_values = [15, 14, 28, 22, 9, 12, 30, 29, 4, 7, 13]

        for x in input_values:
            our_tree.add_node(x)

        # LCA of 12 4 is 9
        self.assertEqual(9, our_tree.find_lca(12, 4))
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

