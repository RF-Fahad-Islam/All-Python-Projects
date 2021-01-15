n = input("Enter the number of rows : ")
boolean = True
try:
    n = int(n)
    if boolean:
        for i in range(n):
            print("*" * (i+1))
    else:
        for i in range(n):
            print("*" * (n-i))
except ValueError:
    print(f"Invalid Value: Please enter a number : {n}")