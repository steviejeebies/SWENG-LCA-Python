from BST import *

# BST will look like this: https://i.ibb.co/1dQdqDD/Untitled.png
our_tree = BST()
input_values = [15, 14, 28, 22, 9, 12, 30, 29, 4, 7, 13]

for x in input_values:
    our_tree.add_node(x)

print("LCA of 12 4:", our_tree.find_lca(12, 4))
print("LCA of 7 4: ", our_tree.find_lca(7, 4))
print("LCA of 14 22: ", our_tree.find_lca(14, 22))
print("LCA of 15 4: ", our_tree.find_lca(15, 4))
print("LCA of 30 29: ", our_tree.find_lca(30, 29))
print("LCA of 7 13: ", our_tree.find_lca(7, 13))
