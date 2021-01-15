import time

def fibIter(n):
    currentNum = 1
    previousNum = 0
    for i in range(1,n):
        prevPreviousNum = previousNum
        previousNum = currentNum
        currentNum = prevPreviousNum + previousNum
    return currentNum

def fibrec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibrec(n-1) + fibrec(n-2)

if __name__ == "__main__":
    n = int(input("Enter the number : "))
    initial = time.time()
    print(f"The Iterative Approach result : fib({n}) = {fibIter(n)}")
    print(f"The Iter result took => {time.time() - initial} seconds")
    initial2 = time.time()
    print(f"The Recursive Approach result : fib({n}) = {fibrec(n)}")
    print(f"The Iter result took => {time.time() - initial2} seconds")