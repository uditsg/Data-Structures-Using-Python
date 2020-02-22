class LinkedListException(Exception):
    pass


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def AddNodeAtEnd(self, data):

        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            new_node.prev = None
            new_node.next = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def PrintList(self):

        if self.head is None:
            try:
                raise LinkedListException("List is empty")
            except LinkedListException as msg:
                print(msg)
                return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next

    def AddNodeAfterKey(self, data, key):

        if self.head == None:
            try:
                raise LinkedListException("List is empty")
            except LinkedListException as msg:
                print(msg)
        else:
            temp = self.head
            new_node = Node(data)
            # Check for all nodes except last one
            while temp.next is not None:
                if temp.data == key:
                    new_node.next = temp.next
                    temp.next = new_node
                    new_node.prev = temp
                    new_node.next.prev = new_node
                    return
                temp = temp.next
            # Check the last node for a match
            if temp.data == key:
                temp.next = new_node
                new_node.prev = temp
            else:
                try:
                    raise LinkedListException("List does not have key")
                except LinkedListException as msg:
                    print(msg)

    def DeleteNode(self, key):
        if self.head == None:
            try:
                raise LinkedListException("List is empty. Nothing to delete")
            except LinkedListException as msg:
                print(msg)
                return
        else:
            temp = self.head
            # If the node to be deleted is first node
            while temp.next is not None:
                if temp.data == key:
                    print("Deleting the key:", key)
                    temp1 = temp.prev
                    temp1.next = temp.next
                    temp.next.prev = temp1
                    temp.next = temp.prev = None
                    return
                temp = temp.next

            # Check for the last node:
            if temp.data == key:
                temp.prev.next = None
                temp.prev = temp.next = None
                print("Deleted the value :", temp.data, "from the end")
                return
            print("Key not found")


if __name__ == '__main__':
    DLL = DoublyLinkedList()
    DLL.AddNodeAtEnd(10)
    DLL.AddNodeAtEnd(20)
    DLL.AddNodeAtEnd(30)
    DLL.AddNodeAtEnd(40)
    DLL.AddNodeAtEnd(50)
    DLL.AddNodeAtEnd(60)

    DLL.PrintList()

    DLL.AddNodeAfterKey(345, 10)
    DLL.PrintList()
