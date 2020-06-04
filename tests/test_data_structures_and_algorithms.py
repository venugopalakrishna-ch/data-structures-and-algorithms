# import pytest
from data_structures_and_algorithms import __version__
from data_structures_and_algorithms.challenges.array_reverse.array_reverse import reverseArray
from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray
from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import BinarySearch
from data_structures_and_algorithms.challenges.array_sum.array_sum import array_matrix_sum
from data_structures_and_algorithms.data_structures.linked_list.linked_list import Node, LinkedList, mergeLists
from data_structures_and_algorithms.data_structures.doubly_linked_list.doubly_linked_list import Node, DoublyLinkedList

#@pytest.mark.parametrize("test_input1","test_input2","expected",[([1,2,3,4],4,3),([1,2,3,4],3,2)])

# def test_array_binary_search_test(test_input1,test_input2,expected):
#     assert BinarySearch(test_input1,test_input2) == expected


def test_version():
    assert __version__ == '0.1.0'

def test_array_shift_one():
    assert insertShiftArray([2,4,6,8],5) == [2,4,5,6,8]

def test_array_shift_two():
    assert insertShiftArray([2,4,6,8,10],99) == [2,4,6,99,8,10]

def test_array_shift_three():
    assert insertShiftArray([2,4,6,8,10,14],99) == [2,4,6,99,8,10,14]

def test_array_shift_four():
    assert insertShiftArray([2,4,6,8,10,14,16],99) == [2,4,6,8,99,10,14,16]

def test_array_reverse_one():
    assert reverseArray([1,2,3,4]) == [4,3,2,1]

def test_array_reverse_two():
    assert reverseArray([5,6,7,8]) == [8,7,6,5]

def test_array_reverse_three():
    assert reverseArray([100,135,80,200]) == [200,80,135,100]

def test_array_reverse_four():
    assert reverseArray([-987,9877,-843343,400]) == [400,-843343,9877,-987]

def test_array_binary_search_one():
    assert BinarySearch([1,2,3,4],4) == 3

def test_array_binary_search_two():
    assert BinarySearch([1,2,3,4],3) == 2

def test_array_binary_search_three():
    assert BinarySearch([1,2,3,4],2) == 1

def test_array_binary_search_four():
    assert BinarySearch([1,2,3,4],1) == 0

def test_array_binary_search_five():
    assert BinarySearch([1,2,3,4],99) == -1

def test_array_binary_search_six():
    assert BinarySearch([1,2,3,4],-33) == -1

def test_array_binary_search_seven():
    assert BinarySearch([1,2,3,4,5],4) == 3

def test_array_binary_search_eight():
    assert BinarySearch([1,2,3,4,5],5) == 4

def test_array_binary_search_nine():
    assert BinarySearch([1,2,3,4,5],3) == 2

def test_array_binary_search_ten():
    assert BinarySearch([1,2,3,4,5],2) == 1

def test_array_binary_search_11():
    assert BinarySearch([1,2,3,4,5],1) == 0

def test_array_binary_search_12():
    assert BinarySearch([1,2,3,4,5],99) == -1

def test_array_binary_search_13():
    assert BinarySearch([1,2,3,4,5],-12) == -1

def test_array_matrix_sum():
    assert array_matrix_sum([[1,2,3],[4,'Test',6],[7,-8,9]]) == [6,10,8]

def test_array_matrix_sum_one():
    assert array_matrix_sum([[1,2,-3],[4,'Test',-6],[7,-8,9]]) == [0,-2,8]

def test_node_apples():
    node = Node("apples")
    assert node.value == "apples"
    assert node.next  == None

def test_linked_list_creation():
    ll = LinkedList()
    assert ll.head == None

def test_insert_one():
    ll = LinkedList()
    ll.insert("apples")
    assert ll.head.value == "apples"
    assert ll.head.next == None

def test_insert_two():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    assert ll.head.value == "bananas"
    assert ll.head.next.value  == "apples"

def test_insert_more():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    ll.insert("cherries")
    assert ll.head.value == "cherries"
    assert ll.head.next.value == "bananas"        
    assert ll.head.next.next.value == "apples"     

def test_includes():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    ll.insert("cherries")
    assert ll.includes("bananas")
    assert ll.includes("oranges") == False

def test_tostring():
    ll = LinkedList()    
    assert ll.__str__() == "None"
    ll.insert("apples")    
    assert ll.__str__() == "{apples}->None"
    ll.insert("bananas")
    assert ll.__str__() == "{bananas}->{apples}->None"
    ll.insert("cherries")
    assert ll.__str__() == "{cherries}->{bananas}->{apples}->None"

def test_doubly_node_apples():
    node = Node("apples")
    assert node.value == "apples"
    assert node.next  == None
    assert node.prev  == None

def test_doubly_linked_list_creation():
    ll = DoublyLinkedList()
    assert ll.head == None

def test_doubly_insert_one():
    ll = DoublyLinkedList()
    ll.insert("apples")
    assert ll.head.value == "apples"
    assert ll.head.next == None
    assert ll.head.prev == None

def test_doubly_insert_two():
    ll = DoublyLinkedList()
    ll.insert("apples")
    ll.insert("bananas")    
    assert ll.head.value == "apples"
    assert ll.head.next.value == "bananas"    
    assert ll.head.prev == None
    assert (ll.head.next).prev.value == "apples"


def test_doubly_insert_more():
    ll = DoublyLinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    ll.insert("cherries")
    assert ll.head.value == "apples"
    assert ll.head.next.value == "bananas"
    assert ll.head.next.next.value == "cherries"
    assert ll.head.prev == None
    assert (ll.head.next).prev.value == "apples"
    assert (ll.head.next.next).prev.value == "bananas"
    
def test_doubly_includes():
    ll = DoublyLinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    ll.insert("cherries")
    assert ll.includes("bananas")
    assert ll.includes("oranges") == False

def test_doubly_tostring():
    ll = DoublyLinkedList()    
    assert ll.__str__() == "None"
    ll.insert("apples")    
    assert ll.__str__() == "{apples}->None"
    ll.insert("bananas")
    assert ll.__str__() == "{apples}->{bananas}->None"
    ll.insert("cherries")
    assert ll.__str__() == "{apples}->{bananas}->{cherries}->None"

def test_append():
    ll = LinkedList()   
    assert ll.__str__() == "None"     
    ll.append("5")    
    assert ll.__str__() == "{5}->None"

def test_append1():
    ll = LinkedList()   
    assert ll.__str__() == "None"     
    ll.append("1")    
    assert ll.__str__() == "{1}->None"
    ll.append("3")
    assert ll.__str__() == "{1}->{3}->None"
    ll.append("2")
    assert ll.__str__() == "{1}->{3}->{2}->None"
    ll.append("5")
    assert ll.__str__() == "{1}->{3}->{2}->{5}->None"

def test_insertBefore():
    ll = LinkedList()   
    ll.append("1")    
    ll.append("3")    
    ll.append("2")   
    ll.insertBefore("3","5")
    assert ll.insertBefore("4","5") == "Node 4 does not exists in Linked List"
    assert ll.insertBefore("8","10") == "Node 8 does not exists in Linked List"
    assert ll.__str__() == "{1}->{5}->{3}->{2}->None"
    
def test_insertBefore1():
    ll = LinkedList()   
    ll.append("1")    
    ll.append("3")    
    ll.append("2")   
    ll.insertBefore("1","5")
    assert ll.insertBefore("4","5") == "Node 4 does not exists in Linked List"
    assert ll.insertBefore("8","10") == "Node 8 does not exists in Linked List"
    assert ll.__str__() == "{5}->{1}->{3}->{2}->None"

def test_insertBefore2():
    ll = LinkedList()   
    ll.append("1")    
    ll.append("3")    
    ll.append("2")   
    ll.insertBefore("2","5")
    assert ll.insertBefore("4","5") == "Node 4 does not exists in Linked List"
    assert ll.insertBefore("8","10") == "Node 8 does not exists in Linked List"
    assert ll.__str__() == "{1}->{3}->{5}->{2}->None"

def test_insertAfter():
    ll = LinkedList()   
    ll.append("1")    
    ll.append("3")    
    ll.append("2")   
    ll.insertAfter("3","5")
    assert ll.insertAfter("4","5") == "Node 4 does not exists in Linked List"
    assert ll.insertAfter("8","10") == "Node 8 does not exists in Linked List"
    assert ll.__str__() == "{1}->{3}->{5}->{2}->None"
    
def test_insertAfter1():
    ll = LinkedList()   
    ll.append("1")    
    ll.append("3")    
    ll.append("2")   
    ll.insertAfter("2","5")
    assert ll.insertAfter("4","5") == "Node 4 does not exists in Linked List"
    assert ll.insertAfter("8","10") == "Node 8 does not exists in Linked List"
    assert ll.__str__() == "{1}->{3}->{2}->{5}->None"

def test_insertAfter2():
    ll = LinkedList()   
    ll.append("1")    
    ll.append("2")    
    ll.append("2")   
    ll.insertAfter("2","5")
    assert ll.insertAfter("4","5") == "Node 4 does not exists in Linked List"
    assert ll.insertAfter("8","10") == "Node 8 does not exists in Linked List"
    assert ll.__str__() == "{1}->{2}->{5}->{2}->None"

def test_insertAfter3():
    ll = LinkedList()   
    ll.append("1")    
    ll.append("2")    
    ll.append("2")   
    ll.insertAfter("1","5")
    assert ll.insertAfter("4","5") == "Node 4 does not exists in Linked List"
    assert ll.insertAfter("8","10") == "Node 8 does not exists in Linked List"
    assert ll.__str__() == "{1}->{5}->{2}->{2}->None"

def test_deleteNode():
    ll = LinkedList()   
    ll.append("1")    
    ll.append("3")    
    ll.append("2")   
    ll.deleteNode("3")
    assert ll.deleteNode("5") == "Node 5 does not exists in Linked List"
    assert ll.deleteNode("10") == "Node 10 does not exists in Linked List"
    assert ll.__str__() == "{1}->{2}->None"

def test_deleteNode1():
    ll = LinkedList()   
    ll.append("1")    
    ll.append("3")    
    ll.append("2")   
    ll.deleteNode("2")
    assert ll.deleteNode("4") == "Node 4 does not exists in Linked List"
    assert ll.deleteNode("8") == "Node 8 does not exists in Linked List"
    assert ll.__str__() == "{1}->{3}->None"

def test_deleteNode2():
    ll = LinkedList()   
    ll.append("1")    
    ll.append("3")    
    ll.append("2")   
    ll.deleteNode("1")
    assert ll.deleteNode("4") == "Node 4 does not exists in Linked List"
    assert ll.deleteNode("8") == "Node 8 does not exists in Linked List"
    assert ll.__str__() == "{3}->{2}->None"

def test_nthNodeValueFromEnd():
    ll = LinkedList()
    ll.append("1")
    ll.append("3")
    ll.append("8")
    ll.append("2")
    assert ll.nthNodeValueFromEnd(0) == "2"
    assert ll.nthNodeValueFromEnd(1) == "8"
    assert ll.nthNodeValueFromEnd(2) == "3"
    assert ll.nthNodeValueFromEnd(3) == "1"
    assert ll.nthNodeValueFromEnd(4) == "Index is out of range"
    assert ll.nthNodeValueFromEnd(5) == "Index is out of range"
    assert ll.nthNodeValueFromEnd(-1) == "Negative index is not allowed to search"
    assert ll.nthNodeValueFromEnd(-99) == "Negative index is not allowed to search"

def test_nthNodeValueFromEnd1():
    ll = LinkedList()    
    assert ll.nthNodeValueFromEnd(0) == "Index is out of range"
    assert ll.nthNodeValueFromEnd(1) == "Index is out of range"
    ll.append("1")
    assert ll.nthNodeValueFromEnd(0) == "1"

def test_fidnMiddleNodeValue():
    ll = LinkedList()
    assert ll.fidnMiddleNodeValue() == "Linked list is empty"
    ll.append("1")
    assert ll.fidnMiddleNodeValue() == "1"
    ll.append("3")
    assert ll.fidnMiddleNodeValue() == "1"
    ll.append("8")
    assert ll.fidnMiddleNodeValue() == "3"
    ll.append("2")
    assert ll.fidnMiddleNodeValue() == "3"
    ll.append("5")
    assert ll.fidnMiddleNodeValue() == "8"

def test_mergeLinkedListOne():    
    ll1 = LinkedList()
    ll1.append("10")
    ll1.append("20")
    ll1.append("30")    
    ll2 = LinkedList()
    ll2.append("5")
    ll2.append("15")
    ll2.append("25")
    ll = LinkedList()
    ll.head = mergeLists(ll1.head,ll2.head) 
    assert ll.__str__() == "{10}->{5}->{20}->{15}->{30}->{25}->None"


def test_mergeLinkedListTwo():    
    ll1 = LinkedList()
    ll1.append("1")
    ll1.append("3")
    ll1.append("2")    
    ll2 = LinkedList()
    ll2.append("5")
    ll2.append("9")
    ll2.append("4")
    ll = LinkedList()
    ll.head = mergeLists(ll1.head,ll2.head) 
    assert ll.__str__() == "{1}->{5}->{3}->{9}->{2}->{4}->None"

def test_mergeLinkedListThree():    
    ll1 = LinkedList()
    ll1.append("1")
    ll1.append("3")      
    ll2 = LinkedList()
    ll2.append("5")
    ll2.append("9")
    ll2.append("4")
    ll = LinkedList()
    ll.head = mergeLists(ll1.head,ll2.head) 
    assert ll.__str__() == "{1}->{5}->{3}->{9}->{4}->None"

def test_mergeLinkedListFour():    
    ll1 = LinkedList()
    ll1.append("1")
    ll1.append("3")
    ll1.append("2")    
    ll2 = LinkedList()
    ll2.append("5")
    ll2.append("9")    
    ll = LinkedList()
    ll.head = mergeLists(ll1.head,ll2.head) 
    assert ll.__str__() == "{1}->{5}->{3}->{9}->{2}->None"