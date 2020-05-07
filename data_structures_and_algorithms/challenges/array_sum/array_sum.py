def userInputs(matrix_size,array_size):
    multi_dimension_array = []       
    for i in range(matrix_size):
        single_dimension_array = []        
        print(f"Enter Element for Array {i+1}:")
        for j in range(array_size):                   
            try:
                input_element = input()  
                single_dimension_array.append(int(input_element))  
            except ValueError:
                single_dimension_array.append(input_element)               
        multi_dimension_array.append(single_dimension_array)
    return multi_dimension_array

def array_matrix_sum(input_array):
    output_array = []
    for single_dimension in input_array:
        sum = 0
        for i in range(len(single_dimension)):
            try:
                sum += single_dimension[i]
            except TypeError:
                print("Null or Any Test will be considered as Zero")
        output_array.append(sum)
    return output_array

if __name__ == "__main__":  
    matrix_length = int(input("Enter Matrix Length:"))
    array_length = int(input("Enter Size of The Array:"))
    user_array = userInputs(matrix_length,array_length)
    print("Here is the input array:",user_array)
    output = array_matrix_sum(user_array)
    print("Here is the output:",output)
    

