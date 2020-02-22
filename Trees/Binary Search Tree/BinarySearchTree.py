'Class to create Node'


class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


'Recursive Insertion into BST'


def Insert(root, key):
    if root is None:
        root = Node(key)
        return root

    else:
        if key < root.key:
            root.left = Insert(root.left, key)

        else:
            root.right = Insert(root.right, key)
        return root


'InOrder Traversal'


def InOrder(root):
    if root is not None:
        InOrder(root.left)
        print(root.key)
        InOrder(root.right)


def Search(root, key):
    if root is None:
        print("Key Not Found")
    elif root.key == key:
        print("Key Found")

    else:
        if key < root.key:
            Search(root.left, key)
        else:
            Search(root.right, key)


'Used to find the next inorder successor to replace the deleted key in the Delete method'


def NextSuccessor(root):
    while root.left is not None:
        root = root.left
    return root


'Deletes the matched node with the key supplied'


def Delete(root, key):
    # Base Case
    if root is None:
        return root
    # Iterate recursively over left child of the node if key < current node value
    if key < root.key:
        root.left = Delete(root.left, key)
        return root

    # Iterate recursively over right child of the node if key > current node value
    elif key > root.key:
        root.right = Delete(root.right, key)
        return root

    # Delete logic :
    else:
        # The following if elif takes care when node either has one child or no child
        if root.right is None:
            temp = root.left
            root = None
            return temp
        elif root.left is None:
            temp = root.right
            root = None
            return temp

        # This logic takes care where node to be deleted will be replaced by the immediate inorder successor
        else:
            temp = NextSuccessor(root.right)
            root.key = temp.key
            root.right = Delete(root.right, temp.key)
            return root


'Driver Function'
if __name__ == '__main__':
    root = Node(40)
    root = Insert(root, 30)
    root = Insert(root, 50)
    root = Insert(root, 80)
    root = Insert(root, 560)
    root = Insert(root, 34)
    root = Insert(root, 5)

    Search(root, 5)
    Search(root, 560)
    Search(root, 80)
    Search(root, 9985)
    InOrder(root)
    root = Delete(root, 34)
    print("After deleting")

    InOrder(root)
