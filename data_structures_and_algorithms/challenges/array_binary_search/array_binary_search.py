from textwrap import dedent
input_text1 = "**Enter the number of elements you want:**\n"
input_text2 = "**Enter numbers in array:**"
input_text3 = "**Please enter the search key**\n"
input_text4 = "**Here are the array elements provide by you in sort order and search key:**\n"
error_msg ="!!Stop accepting the user inputs here, as input is not a number."

# "//"" can be used as devide which return rounded int number though array length is odd number

def IdentifyIndex(input_array,input_number,start_index):
    search_key_found=""
    for start_index in range(len(input_array)):
        if input_number == input_array[start_index]:
            search_key_found = 'Y'
            return start_index
    if search_key_found == "":
        return -1

def BinarySearch(input_array,input_number):
    mid_index = (len(input_array) + 1) // 2    
    if  input_number == input_array[mid_index]:
        return mid_index
    elif input_number > input_array[mid_index]:        
        return IdentifyIndex(input_array,input_number,mid_index)             
    elif input_number < input_array[mid_index]:    
        return IdentifyIndex(input_array,input_number,0)            
    else:
        return -1 

def userInputs():
    number_array = []
    number = input(input_text1)
    print(input_text2)
    for i in range(int(number)): 
        try:       
            n = int(input())                                   
            number_array.append(int(n))
        except:
            print(error_msg)  
            break           
    number_array.sort()
    return number_array

if __name__ == "__main__":  
    user_array = userInputs()  
    search_key = int(input(input_text3))
    print (f"{input_text4} {user_array}, {search_key}")        
    index = BinarySearch(user_array,search_key)
    print(f"Index for your search key '{search_key}' is: {index}")

