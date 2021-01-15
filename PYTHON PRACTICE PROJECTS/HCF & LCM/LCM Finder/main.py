def lcm_finder(num1, num2):
    if num2 > num1:
        mx = num2
    else:
        mx = num1
        
    while True:
        if mx%num1 == 0 and mx%num2 == 0:
            lcm = mx
            break
        mx += 1
    return lcm
if __name__ == "__main__":
    try:
        num1 = int(input("Enter the 1st number : "))
        num2 = int(input("Enter the 2nd number : "))
    except ValueError:
        print("Please enter a intiger not a string.")
    else:
        lcm = lcm_finder(num1, num2)
        print(f"The LCM of {num1} & {num2} is \"{lcm}\"")