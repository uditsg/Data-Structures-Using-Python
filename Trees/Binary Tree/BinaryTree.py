# Class to create a node for a Binary Tree
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Pre-Order Traversal : Root, Left, Right
def PreOrder(root):
    if root:
        print(root.data)
        PreOrder(root.left)
        PreOrder(root.right)


# In-Order Traversal : Left, Root, Right
def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.data)
        InOrder(root.right)


# Post-Order Traversal : Left, Right, Root
def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data)


# Driver Code
if __name__ == '__main__':
    Root = Node(1)
    Root.left = Node(2)
    Root.right = Node(3)
    Root.left.left = Node(4)
    Root.left.right = Node(5)

    print("Pre-Order Traversal is :")
    PreOrder(Root)

    print("In-Order Traversal is :")
    InOrder(Root)

    print("Post-Order Traversal is :")
    PostOrder(Root)
