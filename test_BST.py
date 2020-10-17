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

    def test_find_node(self):
        self.fail()

    def test_find_lca(self):
        self.fail()

    def test_find_lca_recursive(self):
        self.fail()

