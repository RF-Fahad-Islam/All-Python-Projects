from tkinter import *
import random
import time
def rollDice():
    for i in range(300):
        #* Range for creating a number generating view
        randomNo = random.randint(1,6)
        dice.set(str(randomNo))
        text.update()
        time.sleep(0.003)
    
if __name__ == "__main__":
    root = Tk()
    root.title("Roll the Dice")
    root.geometry("300x300")
    root.minsize(200,300)
    root.minsize(300,300)
    # root.minsize(100*300)
    dice = StringVar()
    dice.set("0")
    text = Label(root, textvariable=dice, font="comicsans 60 bold")
    text.pack(pady=12, fill=X)
    b = Button(root, text="Roll Dice", font="comicsans 30 bold",bg="#3af067", fg="white", pady=3, padx=6, command=rollDice)
    b.pack(pady=12)
    root.mainloop()
