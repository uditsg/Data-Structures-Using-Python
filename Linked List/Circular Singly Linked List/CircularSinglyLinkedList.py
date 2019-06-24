class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class CircularLinkedList:

    def __init__(self):
        self.last = None

    '''Method to be invoked when node has to be added to either
    front or end '''   
    def addNodeByPos(self,data,addAtStart = 0):
        
        #If there exists no nodes
        if self.last == None:
            new_node = Node(data)
            new_node.last = new_node

        else:
            new_node = Node(data)

            #Node can either be added at the start or end
            if addAtStart == 0:
                new_node.next = self.last.next
                self.last.next = new_node
                self.last = new_node
            else:
                new_node.next = self.last.next
                self.last.next = new_node
                
    '''Method to be invoked when the node needs to be added next
       to another node which has value as key''' 
    def AddNodeByKey(self,data,key):

        if self.last is None:
            new_node = Node(data)
            new_node.last = new_node

        #If key is there at the last, then invoke addNodeByPos to add it.
        #We check this as the while loop will not iterate for the last node
        if self.last.data == key:
            self.addNodeByPos(data)
            return
        
        temp = self.last.next
        while temp.next is not self.last.next:
            if temp.data == key:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            else:
                temp = temp.next
        print("Key not found")
        return

    def DelNode(self,key):
        
        if self.last is None:
            print ("List is empty cannot delete")
            return
        
        temp = self.last

        while temp.next is not self.last:
            '''Search for the match with temp.next.data as
            we need to have the previous node's info handy'''
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next
            
        #If the node to be deleted is the last one 
        if self.last.data == key:
            #if there exists only one node and that has to be deleted
            if temp.next == self.last.next:
                self.last = None
                return
            temp.next = self.last.next
            self.last = temp
            return
        else:
            print("Key not present")
            return
        
        
        
            
    def PrintList(self):
        if self.last is None :
            print("List is empty")
            return
        
        temp = self.last.next
        
        while temp.next is not self.last.next:
            print(temp.data)
            temp = temp.next
        #We print the data for the last node as the while loop
        #does not iterate for the last node
        print(self.last.data)

#Driver Code:
if __name__ == '__main__':

    Llist = CircularLinkedList()
    Node1 = Node(1)
    Node2 = Node(2)

    Node1.next = Node2
    Llist.last = Node2
    Node2.next = Node1
    
    Llist.PrintList()

    Llist.addNodeByPos(34,1)
    print("After modifying, reprinting the linked list")
    Llist.PrintList()

    Llist.AddNodeByKey(3,1)
    print("After modifying, reprinting the linked list")
    Llist.PrintList()

    Llist.DelNode(3)
    print("After deleting 3, reprinting the linked list")
    Llist.PrintList()


    Llist.DelNode(34)
    print("After deleting 34, reprinting the linked list")
    Llist.PrintList()

    Llist.DelNode(2)
    print("After deleting 2, reprinting the linked list")
    Llist.PrintList()

    Llist.DelNode(1)
    print("After deleting 1, reprinting the linked list")
    Llist.PrintList()


    Llist.DelNode(2)
    print("After deleting 2, reprinting the linked list")
    Llist.PrintList()
    
        
        
                
            
            
            
        
