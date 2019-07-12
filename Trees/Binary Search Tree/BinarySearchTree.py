'Class to create Node'
class Node:

    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

'Recursive Insertion into BST'
def Insert(root,key):

    if root is None:
        root = Node(key)

    else:
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                Insert(root.left,key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                Insert(root.right,key)

'InOrder Traversal'
def InOrder(root):
    if root is not None:
        InOrder(root.left)
        print(root.key)
        InOrder(root.right)      

'Driver Function'       
if __name__=='__main__':
    root_node = Node(40)
    Insert(root_node,30)
    Insert(root_node,50)
    Insert(root_node,80)
    Insert(root_node,560)
    Insert(root_node,34)
    Insert(root_node,5)

    InOrder(root_node)
    








