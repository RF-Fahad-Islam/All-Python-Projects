
def str_to_binary(text):
    for char in text:
        return format(ord(char), '08b')
        
def binary_to_str(binary):
    #number of characters in text
    num = len(binary)/8 
    bit = ""
    for x in range(int(num)):
        start = x*8
        end = (x+1)*8
        bit += chr(int(str(binary[start:end]),2))
    return bit