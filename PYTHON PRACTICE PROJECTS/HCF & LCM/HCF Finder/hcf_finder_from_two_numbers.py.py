def hcf_finder(num1, num2):
    if num2 > num1:
        mn = num1
    else:
        mn = num2
        
    for i in range(1, mn+1):
        if num1%i == 0 and num2%i == 0:
            hcf = i
    return hcf

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
    except ValueError:
        print(f"Please Enter a number not a intiger.")
    else:
        hcf = hcf_finder(num1, num2)
        print(f"The HCF of {num1} & {num2} is \"{hcf}\"")