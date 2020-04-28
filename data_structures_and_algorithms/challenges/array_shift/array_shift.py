from textwrap import dedent
output_text = "** Here is your output array with new value added **\n"
input_text1 = "**Enter the number of elements you want:**\n"
input_text2 = "**Enter numbers in array:**"
input_text3 = "**Please enter the value to be added to middle index of an array**\n"
input_text4 = "**Here are the array elements provide by you and value to be added to middle index of an array:**\n"
error_msg ="!!Stop accepting the user inputs here, as input is not a number."

# "//"" can be used as devide which return rounded int number though array length is odd number

def insertShiftArray(input_array,input_number):
    # Approach 1:
    # output_array = list ()  
    # if len(input_array) % 2 == 0:
    #     mid_index = int(len(input_array) / 2) 
    # else:
    #     mid_index = int((len(input_array) + 1) / 2)
    # for i in range(len(input_array)):        
    #     if mid_index == i:
    #         output_array.append(input_number)
    #     output_array.append(input_array[i])    
    # return output_array   
    #Approach 2
    mid_index = (len(input_array) + 1) // 2 
    return input_array[0:mid_index] + [input_number] + input_array[mid_index:]

def userInputs():
    number_array = list()
    number = input(input_text1)
    print(input_text2)
    for i in range(int(number)): 
        try:       
            n = int(input())                                   
            number_array.append(int(n))
        except:
            print(error_msg)  
            break    
    return number_array

if __name__ == "__main__":  
    user_array = userInputs()  
    number = int(input(input_text3))
    print (f"{input_text4} {user_array}, {number}")        
    shift_arrray = insertShiftArray(user_array,number)
    print(output_text, shift_arrray)

