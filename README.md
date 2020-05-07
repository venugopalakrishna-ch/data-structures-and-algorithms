# Challenge Summary 1
<!--Print the array elements in reverse order -->
## Challenge Description
<!--
Prompts the user to enter the number of elements to be part of an array, User will be prompted again to enter the array elements.
array_reverse.py will display the array in reverse order.
File Location: data_structures_and_algorithms\challenges\array_reverse\array_reverse.py-->
## Approach & Efficiency
<!--
userInputs method will be called to gather user entred inputs and put into an array using append method
reverseArray method will be called to read the user entered array elements in reverse order using pop method and each element will be added to a new array using append method. Finally print the array in reverse order on the console -->
## Solution
<!-- 
Refer the white board image in the followiing location data_structures_and_algorithms\challenges\array_reverse\assets\array-reverse.jpg-->

# Challenge Summary 1
<!-- Print the entered numbers in reverse order -->
## Challenge Description
<!--Prompts the user to enter the numbers in a comma separated format
array_reverse.py will display the entered elements in reverse order-->
## Approach & Efficiency
<!--
Split the user entered string on the cosole into an array using split method.
reverseArray method will be called to read the array in reverse order using pop method and add them into an new array using append method.-->
## Solution
<!--Refer the white board image in the followiing location 
data_structures_and_algorithms\challenges\array_reverse_2\assets\array-reverse2.jpg-->

# Challenge Summary 2
<!--Insert an element into middle index of an array -->
## Challenge Description
<!--Prompts the user to enter the number of elements to be part of an array, User will be prompted again to enter the array elements. Also prompt the user to enter element which needs to be added in middle index
array_shift.py will display an array after inserting user entered element to middle index of an array.
File Location:
data_structures_and_algorithms\challenges\array_shift\array_shift.py -->
## Approach & Efficiency
<!--userInputs method will be called to gather user entred inputs and put into an array using append method and user also will be prompted to enter the element which needs to be added in middle index
insertShiftArray function takes in an array and the value to be added to middle index of an array. Find out the middle index to identify left side array and right side array, and insert user entered element into middle.
 Return an array with the new value added at the middle index.
-->
## Solution
<!--Refer the white board image in the followiing location 
data_structures_and_algorithms\challenges\array_shift\assets\array-shift.jpg -->

# Challenge Summary 3
<!--Find out the index of a search key from an array -->
## Challenge Description
<!--Prompts the user to enter the number of elements to be part of an array, User will be prompted again to enter the array elements.Also prompt the user to enter the element for which index needs to be identified
array_binary_search.py will return the index of the array’s element that is equal to the search key, or -1 if the element does not exist. 
File Location
data_structures_and_algorithms\challenges\array_binary_search\array_binary_search.py-->
## Approach & Efficiency
<!--userInputs method will be called to gather user entred inputs and put into an array using append method and user also will be prompted to enter the element for which index needs to be identified 
BinarySearch method will be called to identify the middle index, compares the value of middle index of an array against search key. If values are same return middle index, if the search key is greater than the value of middle index of an array then search in right side of an array, if the search key is less than the value of middle index of an array then search in left side of an array. If search key found either in left side or right side of an array then return the respective index else return -1-->
## Solution
<!--Refer the white board image in the followiing location 
data_structures_and_algorithms\challenges\array_binary_search\assets\array-binary-search.jpg -->

# Challenge Summary 4
<!-- Find out the sum of each row in a matrix of arbitary size -->
## Challenge Description
<!-- User will be asked to enter the size of multi dimensional array and individual array. Based on these inputs, user will be prompted to enter values into an individual array. The formated multi dimensional array will be passed as input to array_matrix_sum function. This function sum up the elements in each individual array and return the output
-->
## Approach & Efficiency
<!-- Prompts user to enter the matrix size
Promots user to enter array size
Promots user to enter elements into an individual array
Formate the user inputs into an multi dimensional array
Loop through each individual array from an multi dimensional array and sum up the elements
Add the sum of each individual array to a new array
Repeat the process for all individual array and print the final output.
-->
## Solution
<!--Refer the white board image in the followiing location 
data_structures_and_algorithms\challenges\array_sum\assets\array-sum.jpg -->


