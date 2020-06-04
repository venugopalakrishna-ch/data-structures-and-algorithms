# Challenge Summary 1
Print the array elements in reverse order
## Challenge Description
Prompts the user to enter the number of elements to be part of an array, User will be prompted again to enter the array elements.
array_reverse.py will display the array in reverse order.
File Location: data_structures_and_algorithms\challenges\array_reverse\array_reverse.py
## Approach & Efficiency
userInputs method will be called to gather user entred inputs and put into an array using append method
reverseArray method will be called to read the user entered array elements in reverse order using pop method and each element will be added to a new array using append method. Finally print the array in reverse order on the console 
## Solution 
Refer the white board image in the followiing location data_structures_and_algorithms\challenges\array_reverse\assets\array-reverse.jpg

# Challenge Summary 1 a
 Print the entered numbers in reverse order 
## Challenge Description
Prompts the user to enter the numbers in a comma separated format
array_reverse.py will display the entered elements in reverse order
## Approach & Efficiency
Split the user entered string on the cosole into an array using split method.
reverseArray method will be called to read the array in reverse order using pop method and add them into an new array using append method.
## Solution
Refer the white board image in the followiing location 
data_structures_and_algorithms\challenges\array_reverse_2\assets\array-reverse2.jpg

# Challenge Summary 2
Insert an element into middle index of an array 
## Challenge Description
Prompts the user to enter the number of elements to be part of an array, User will be prompted again to enter the array elements. Also prompt the user to enter element which needs to be added in middle index
array_shift.py will display an array after inserting user entered element to middle index of an array.
File Location:
data_structures_and_algorithms\challenges\array_shift\array_shift.py 
## Approach & Efficiency
userInputs method will be called to gather user entred inputs and put into an array using append method and user also will be prompted to enter the element which needs to be added in middle index
insertShiftArray function takes in an array and the value to be added to middle index of an array. Find out the middle index to identify left side array and right side array, and insert user entered element into middle.
 Return an array with the new value added at the middle index.
## Solution
Refer the white board image in the followiing location 
data_structures_and_algorithms\challenges\array_shift\assets\array-shift.jpg 

# Challenge Summary 3
Find out the index of a search key from an array 
## Challenge Description
Prompts the user to enter the number of elements to be part of an array, User will be prompted again to enter the array elements.Also prompt the user to enter the element for which index needs to be identified
array_binary_search.py will return the index of the array’s element that is equal to the search key, or -1 if the element does not exist. 
File Location
data_structures_and_algorithms\challenges\array_binary_search\array_binary_search.py
## Approach & Efficiency
userInputs method will be called to gather user entred inputs and put into an array using append method and user also will be prompted to enter the element for which index needs to be identified 
BinarySearch method will be called to identify the middle index, compares the value of middle index of an array against search key. If values are same return middle index, if the search key is greater than the value of middle index of an array then search in right side of an array, if the search key is less than the value of middle index of an array then search in left side of an array. If search key found either in left side or right side of an array then return the respective index else return -1
## Solution
Refer the white board image in the followiing location 
data_structures_and_algorithms\challenges\array_binary_search\assets\array-binary-search.jpg 

# Challenge Summary 4
Find out the sum of each row in a matrix of arbitary size 
## Challenge Description
User will be asked to enter the size of multi dimensional array and individual array. Based on these inputs, user will be prompted to enter values into an individual array. The formated multi dimensional array will be passed as input to array_matrix_sum function. This function sum up the elements in each individual array and return the output
## Approach & Efficiency
Prompts user to enter the matrix size
Promots user to enter array size
Promots user to enter elements into an individual array
Formate the user inputs into an multi dimensional array
Loop through each individual array from an multi dimensional array and sum up the elements
Add the sum of each individual array to a new array
Repeat the process for all individual array and print the final output.
## Solution
Refer the white board image in the followiing location 
data_structures_and_algorithms\challenges\array_sum\assets\array-sum.jpg 

# Challenge Summary 5 A
Singly Linked List Implementation
## Challenge Description
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created. 
- Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
- Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
- Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
## Approach & Efficiency
User can successfully instantiate an empty linked list
User can properly insert into the linked list
The head property will properly point to the first node in the linked list
User can properly insert multiple nodes into the linked list
True should be return when finding a value within the linked list that exists
False should be return when searching for a value in the linked list that does not exist
Program should return a collection of all the values that exist in the linked list
## Solution
Refer the code here
data_structures_and_algorithms\data_structures\linked_list\linked_list.py

# Challenge Summary 5 B
Doubly Linked List Implementation
## Challenge Description
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node and previous node
Within your LinkedList class, include a head property and set the value to previous and next pointers Upon instantiation, an empty Linked List should be created. 
- Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance and set the pointer to previous and next nodes.
- Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
- Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
        "{ a } <-> { b } <-> { c } <-> NULL"
## Approach & Efficiency
User can successfully instantiate an empty linked list
User can properly insert into the linked list
The head property will properly point to the first node in the linked list
User can properly insert multiple nodes into the linked list
True should be return when finding a value within the linked list that exists
False should be return when searching for a value in the linked list that does not exist
Program should return a collection of all the values that exist in the linked list
## Solution
Refer the code here 
data_structures_and_algorithms\data_structures\doubly_linked_list\doubly_linked_list.py

# Challenge Summary 6
Extenstion of Linked List class with additinal methods.
## Challenge Description
- append(value) which adds a new node with the given value to the end of the list
- insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
- insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node
- deleteNode(value) which deletes a node with the given value from the linked list.
## Approach & Efficiency
Can successfully add a node to the end of the linked list
Can successfully add multiple nodes to the end of a linked list
Can successfully insert a node before a node located i the middle of a linked list
Can successfully insert a node before the first node of a linked list
Can successfully insert after a node in the middle of the linked list
Can successfully insert a node after the last node of the linked list
Can successfully delete a node
## Solution
Refer the code and white boarding here 
data_structures_and_algorithms\data_structures\linked_list\linked_list.py
data_structures_and_algorithms\data_structures\linked_list\assets\append and insertBefore.jpg
data_structures_and_algorithms\data_structures\linked_list\assets\insertAfter and DeleteNode.jpg

# Challenge Summary 7
Extenstion of Linked List class with additinal methods.
## Challenge Description
A. Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

B. implement a method that finds the node at the middle of the Linked List.
## Approach & Efficiency
A.
Where k is greater than the length of the linked list
Where k and the length of the list are the same
Where k is not a positive integer
Where the linked list is of a size 1
“Happy Path” where k is not at the end, but somewhere in the middle of the linked list
B.
Where linked list is empty
Where linked list size is 1
Where linked list size is 2
Where linked list size is 3
Where linked list size is 4
Where linked list size is 5

## Solution
Refer the code and white boarding here 
data_structures_and_algorithms\data_structures\linked_list\linked_list.py
data_structures_and_algorithms\data_structures\linked_list\assets\ll-kth-from-end.jpg

# Challenge Summary 8
Extenstion of Linked List class with additinal methods.
## Challenge Description
Write a function called mergeLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Solution
Refer the code here 
data_structures_and_algorithms\data_structures\linked_list\linked_list.py