class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):        
        new_item = Node(value)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item               
            
    def includes(self,key):       
        current = self.head
        while current:
            if current.value == key:   
                return True       
            current = current.next 
        return False    
    
    def __str__(self):
        current = self.head  
        linked_list_string=""      
        while current:
            linked_list_string += "{" + current.value + "}->"
            current = current.next
        return linked_list_string + "None"

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value        
        self.next = next
        self.prev = prev
                        
