# Twenty random cards are placed in a row all face down. A turn consists of taking two adjacent cards where the left one is face up and the right one can be face up or face down and flipping them both. Show that this process must terminate. (with all the cards facing up).
def transfrom(b):
    for i in range(len(b)-1):
        if b[i] == "1":
            b[i] = "0"
            if b[i+1] == "0":
                b[i+1] = "1"
            else:
                b[i+1] = "0"
    return b

if __name__ == "__main__":
    a = list("10101010101010001001001010")
    n = 0
    while a != transfrom(a.copy()):
        a = transfrom(a.copy())
    print(a)