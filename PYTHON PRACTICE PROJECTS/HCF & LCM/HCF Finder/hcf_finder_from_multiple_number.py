def hcf_finder(numlist):
    mn = min(numlist)
    for i in range(1, mn+1):
        for n in numlist:
            if n%i == 0:
                hcf = i
    return hcf

if __name__ == "__main__":
    try:
        i = 1
        numlist = []
        while True:
            print("Enter \"q\" to exit")
            num1 = input(f"{i}. Enter the number : ")
            if num1 == "q":
                break
            else:
                numlist.append(int(num1))
            i += 1
        hcf = hcf_finder(numlist)
        print(f"The HCF of {numlist} is \"{hcf}\"")
    except ValueError:
        print(f"Please Enter a number not a intiger.")