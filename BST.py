def myFunction():
    print("sucess")

# JAVA CODE FOR BST BELOW
# public class BST {
#     class Node {
#         int key;
#         Node leftChild, rightChild;
#
#         public Node(int value) {
#             key = value;
#             leftChild = null;
#             rightChild = null;
#         }
#     }
#
#     // root of our tree
#     Node root;
#
#     public BST() {
#         root = null;
#     }
#
#     // call recursive function, then return the key of the LCA found
#     public int findLCA(int key1, int key2) { return findLCA(root, key1, key2).key; }
#
#     // recursive function
#     private Node findLCA(Node searchNode, int key1, int key2) {
#         if (searchNode == null) return null;        // if no root node, return null
#         if (searchNode.key == key1 || searchNode.key == key2) return searchNode;    // if key matches search node,
#                                                                                     // return search node
#         Node leftSearch = findLCA(searchNode.leftChild, key1, key2);    // call recursively on left branch
#         Node rightSearch = findLCA(searchNode.rightChild, key1, key2);  // call recursively on right branch
#
#         if (leftSearch != null && rightSearch != null) return searchNode;
#         return (leftSearch != null) ? leftSearch : rightSearch;
#     }
#
#     public void addNode(int value) {
#         if (root == null) root = new Node(value);
#         Node searchNode = root;
#         while (true) {  // if the same number is entered twice, it will not create a new node for the repetition
#             if (value == searchNode.key) break;     // break if current node has the same value
#             if (value < searchNode.key) {
#                 if (searchNode.leftChild == null) {
#                     searchNode.leftChild = new Node(value);  // create new left node if no left node, and breaks
#                     break;
#                 } else searchNode = searchNode.leftChild;    // if left child present and not equal, search left branch
#             } else {    // if (value > searchNode.key)
#                 if (searchNode.rightChild == null) {
#                     searchNode.rightChild = new Node(value); // create new right node if no left node, and breaks
#                     break;
#                 } else searchNode = searchNode.rightChild;   // if left child present and not equal, search left branch
#             }
#         }
#     }
# }
