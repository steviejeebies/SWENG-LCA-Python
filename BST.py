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
        while search_node.key is not value:
            if value < search_node.key:
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

    def find_node(self, value):
        if self.root is None:
            return None

        search_node = self.root

        while value is not search_node.key:    # if the same number is entered twice, it will not create a new node for the repetition
            if value < search_node.key:
                if search_node.left_child is None:
                    return None
                else:
                    search_node = search_node.left_child  # if left child present and not equal, search left branch
            else:   # if (value > search_node.key)
                if search_node.right_child is None:
                    return None
                else:
                    search_node = search_node.right_child   # if left child present and not equal, search left branch

        return search_node  # return if current node has the same value

    def find_lca(self, key1, key2):
        found_node = self.find_lca_recursive(self.root, key1, key2)
        return found_node.key if found_node is not None else found_node.key

    def find_lca_recursive(self, search_node, key1, key2):
        if search_node is None:
            return None
        if search_node.key is key1 or search_node.key is key2:
            return search_node

        left_search = self.find_lca_recursive(search_node.left_child, key1, key2)
        right_search = self.find_lca_recursive(search_node.right_child, key1, key2)

        if left_search is not None and right_search is not None:
            return search_node
        return left_search if left_search is not None else right_search
