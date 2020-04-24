from textwrap import dedent
output_text = "** Here is your output in reverse order **\n"

def reverseArray(input_array):
    output_array = list ()     
    while len(input_array) !=  0:
        output_array.append(input_array.pop())
    return output_array

def userInputs():
    number_array = list()
    number = input("**Enter the number of elements you want:**\n")
    print ('**Enter numbers in array:**')
    for i in range(int(number)): 
        try:       
            n = int(input())                                   
            number_array.append(int(n))
        except:
            print("!!Stop accepting the user inputs here, as input is not a number.")  
            break                  
    print ("**Here are the array elements provide by you:**\n",number_array) 
    return number_array

if __name__ == "__main__":  
    user_arry = userInputs()         
    reverse_arrray = reverseArray(user_arry)
    print(output_text, reverse_arrray)

