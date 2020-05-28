class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,value):
        self.head = Node(value,self.head)

    def includes(self,key):
        current = self.head
        while current:
            if current.value == key:
                return True
            current = current.next
        return False

    def append(self,value):
        new_node = Node(value,None)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next        
        last.next = new_node

    def insertBefore(self, value, new_value):                 
        current = self.head 
        if current.value == value:
            self.head = Node(new_value,self.head)
        else:          
            match_found = ""  
            while current:                
                if current.value == value:  
                    match_found ="X"              
                    break
                prev_node = current
                current = current.next   

            if match_found == "X":      
                new_node = Node(new_value)
                prev_node.next = new_node
                new_node.next = current
            else:
                return f"Node {value} does not exists in Linked List"                
    
    def insertAfter(self, value, new_value):
        current = self.head 
        match_found = ""  
        while current:                
            if current.value == value:  
                match_found ="X"              
                break                
            current = current.next   

        if match_found == "X":      
            new_node = Node(new_value)
            store_next = current.next
            current.next = new_node
            new_node.next = store_next  
        else:
            return f"Node {value} does not exists in Linked List"

    def deleteNode(self, value):                 
        current = self.head 
        if current.value == value:
            self.head = current.next
        else:          
            match_found = ""  
            while current:                
                if current.value == value:  
                    match_found ="X"              
                    break
                prev_node = current
                current = current.next   

            if match_found == "X":                      
                prev_node.next = current.next                
            else:
                return f"Node {value} does not exists in Linked List"  

    def nthNodeValueFromEnd(self, index):
        if index < 0:
            return "Negative index is not allowed to search"
        length = 0
        current = self.head
        while current is not None:
            current = current.next
            length += 1
        if index >= length:
            return "Index is out of range"
        
        current = self.head
        for i in range(1, length - index):
            current = current.next
        return current.value

    def fidnMiddleNodeValue(self):
        if self.head is None:
            return "Linked list is empty"
        length = 0
        current = self.head
        while current is not None:
            current = current.next
            length += 1
        mid_index =  (length+1) // 2
        current = self.head
        for i in range(1, mid_index):
            current = current.next
        return current.value



    def __str__(self):
        current = self.head  
        linked_list_string=""      
        while current:
            try:
                linked_list_string += "{" + current.value + "}->"
                current = current.next
            except AttributeError:
                return linked_list_string + "None"
        return linked_list_string + "None"

class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next  = next

