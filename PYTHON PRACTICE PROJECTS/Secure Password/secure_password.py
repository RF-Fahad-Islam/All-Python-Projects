# from tkinter import *
Secure = (('s', "$"), ('a', '@'), ('I', "|"),
          ("And", "&"), ('i', 'T'), ('1', "!"), ('o', "0"),("b", "A"), ("C", "��D�"), ("c", "??"), ("e", ":"), (" "))
password = ""
# for tuples in Secure:
#     for char in tuples:
#         password = password.replace(tuples[0], tuples[1])
def decode():
    # password = input("Enter the password : ")
    global password
    password = str(password)
    for tuples in Secure:
        for char in tuples:
            password = password.replace(tuples[0], tuples[1])
    print(f"Your secure password is {password}")
    
def encode():
    # password = input("Enter the password : ")
    global password
    password = str(password)
    for tuples in Secure:
        for char in tuples:
            password = password.replace(tuples[1], tuples[0])
    print(f"Your secure password is {password}")
        
if __name__ == "__main__":
    password = input("Enter the password : ")
    typeDE = input("1.Decode\n2.Encode\nChoose your option : ")
    if typeDE == "1":
        decode()
    else:
        encode()
