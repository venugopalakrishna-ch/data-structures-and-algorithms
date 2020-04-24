from textwrap import dedent
user_prompt = "** Enter any numbers separated by comma **\n"
output_text = "** Here is your array output in reverse order **\n"

def reverseArray(input_list): 
    output_list = list ()        
    while len(input_list) !=  0:
        output_list.append(input_list.pop())
    return output_list
    
if __name__ == "__main__":    
    input_numbers = input(dedent(user_prompt))
    input_array = input_numbers.split(",")  
    print("**Here are the array elements provide by you:**\n",input_array)
    output_array = reverseArray(input_array)
    print(output_text, output_array)

