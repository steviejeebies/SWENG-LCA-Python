class BST:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.key = value
            self.left_child = None
            self.right_child = None

    def add_node(self, value):
        if self.root is None:
            self.root = self.Node(value)
            return

        search_node = self.root
        while True:
            if search_node.key is value:
                break
            elif value < search_node.key:
                if search_node.left_child is None:
                    search_node.left_child = self.Node(value)
                    break
                else:
                    search_node = search_node.left_child
            else:  # if value > search_node.key
                if search_node.right_child is None:
                    search_node.right_child = self.Node(value)
                    break
                else:
                    search_node = search_node.right_child
        return

    def find_lca(self, key1, key2):
        return self.findLCA(self, self.root, key1, key2).key

    def find_lca(self, search_node, key1, key2):
        if search_node is None:
            return None
        if search_node.key is key1 or search_node.key is key2:
            return search_node

        left_search = self.find_lca(self, search_node.left_child, key1, key2)
        right_search = self.find_lca(self, search_node.right_child, key1, key2)

        if left_search is None and right_search is None:
            return search_node
        return left_search if left_search is not None else right_search
