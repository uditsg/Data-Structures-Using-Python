#Class to initialize a Singly Linked List and other methods to perform various operations
class LinkedList:
    
    def __init__(self):
        self.head = None
 
    def PrintList(self):
        temp = self.head
        while(temp is not None):
            print (temp.data)
            temp = temp.next

    def InsertNodeAtHead(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def InsertNodeAtEnd(self,data):
        new_node = Node(data)
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        temp.next = new_node
        new_node.next = None

    #Method will insert node next to the match i.e. on the right side    
    def InsertNodeAtMatch(self,data,key):
        temp = self.head
        while(temp is not None):
            if(temp.data == key):
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            else:
                temp = temp.next
                
        #Two possibilities : Either no node matches key or Linked List is empty.        
        if(self.head is not None):
            print("Node cannot be inserted as Key is not present")
            
        #If Linked List is empty, create a new one with the data passed.
        else:
            print("No nodes present. Creating a new list with the key hence")
            self.InsertNodeAtHead(data)


    def DeleteNode(self,key):
        temp = self.head
        while(temp is not None):
            #If key is the first node
            if (temp.data == key):
                self.head = temp.next
                return
            
            #If key is any other node including the last one
            elif (temp.next.data == key ):
                temp.next = temp.next.next
                return
            
            else:
                temp = temp.next
        print("Node to be deleted is not present")
            

#Class to initialize a node with the given data
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None



#Driver Code to test the above    
if __name__=='__main__':

    #Methods can be invoked in any order
    Llist = LinkedList()
    Llist.InsertNodeAtMatch(24,90)
    print("after process")
    Llist.PrintList()
    print("begin")
    Llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    Llist.head.next = second
    second.next = third
    Llist.InsertNodeAtHead(34)
    Llist.InsertNodeAtEnd(90)
    Llist.PrintList()
    Llist.InsertNodeAtMatch(24,90)
    print("after process")
    Llist.PrintList()
    Llist.InsertNodeAtMatch('yoyo',2)
    print("after process")
    Llist.PrintList()
    print("After deleting 90")
    Llist.DeleteNode(90)
    Llist.PrintList()
    print("After deleting 34")
    Llist.DeleteNode(34)
    Llist.PrintList()
    print("After deleting yoyo")
    Llist.DeleteNode('yoyo')
    Llist.PrintList()
   
        
