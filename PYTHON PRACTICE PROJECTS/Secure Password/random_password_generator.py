import random
def generatePassword():
    charset = "abcdefghijklmnopqrstuvwxyz"+ "!@#$%^&*()|" + "1234567890" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    retVal = ""
    num = int(input("Enter the length of the password : "))
    for i in range(num):
        randNum = random.randint(1, len(charset))
        retVal += charset[randNum]
    return retVal

if __name__ == "__main__":
    password = generatePassword()
    print(f"The random password is {password}")