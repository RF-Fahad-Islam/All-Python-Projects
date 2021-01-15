def armstrong_number_finder(n):
    sumresult = 0
    for number in str(n):
        sumresult += int(number)**len(str(n))
    if sumresult == n:
        return True
    else:
        return False

def nearest_armstrong_number_finder(n):
    n = int(n)
    sumresult = 0
    while True:
        for number in str(n):
            sumresult += int(number)**len(str(n))
        if n != sumresult:
            n += 1
            sumresult = 0
        else:
            break
    return n
        

if __name__ == "__main__":
    n = int(input("Enter the number to find armstrong : "))
    arms = armstrong_number_finder(n)
    if arms == True:
        print(f"\"{n}\" is a armstrong number of {len(str(n))} order!")
    else:
        print(f"\"{n}\" is not a armstrong number of {len(str(n))} order.")
        nn = nearest_armstrong_number_finder(n)
        print(f"-------------------The nearest armstrong number : -------------------\n\"{nn}\"")