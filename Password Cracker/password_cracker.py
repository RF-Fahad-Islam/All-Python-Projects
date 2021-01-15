import random
password = input("Enter the password : ")
charset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
cracked_password = ""
while True:
    for i in range(len(password)):
        cracked_password += charset[random.randint(0, (len(charset)-1))]
    print(cracked_password)
    if cracked_password == password:
        break
    else:
        cracked_password = ""
    