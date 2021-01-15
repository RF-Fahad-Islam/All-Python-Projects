while True:
    op = input("Enter the operator : ")
    num1 = input("Enter the  1st Number : ")
    if num1 == "q":
        break
    num2 = input("Enter the  2nd Number : ")
    try:
        num1 = int(num1)
        num2 = int(num2)
    except Exception as e:
        print(e)
    else:
        # 45 * 3 = 555
        # 56+9 = 77
        # 56/6 = 4
 
        if op == "+":
            if num1 == 56 and num2 == 9:
                result = 77
            else: 
                result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif op == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif op == "*":
            if num1 == 45 and num2 == 3:
                result = 555
            else: 
                result = num1 * num2
            print(f"{num1} X {num2} = {result}")
        elif op == "/":
            if num1 == 56 and num2 == 6:
                result = 4
            else: 
                result = num1 / num2
            print(f"{num1} / {num2} = {result}")