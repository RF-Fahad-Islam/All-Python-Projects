from tkinter import *
root = Tk()
root.geometry("400x500")
root.minsize(400,500)
root.maxsize(400,500)

root.title("Calculator GUI")
# root.wm_iconbitmap("Tkinter/calculator.ico")
def click(event):
    global screenvalue
    global status
    text = event.widget.cget('text')
    # print(text)
    if text == "=":
        try:
            if screenvalue.get().isdigit():
                value = int(screenvalue.get())
            else:
                value = eval(screenvalue.get())
        except Exception as e:
            print(e)
            screenvalue.set(f"Error : {screenvalue.get()}")
        screenvalue.set(value)
        screen.update()
    elif text == "C":
        screenvalue.set("")
        screen.update()
    else:
        screenvalue.set(screenvalue.get() + text)
        screen.update()
    try:
        statusmsg = eval(screenvalue.get())
    except Exception as e:
        statusmsg = screenvalue.get()
    status.set(f"Status : {statusmsg}")
    statusbar.update()

screenvalue = StringVar()
screenvalue.set("")
screen = Entry(root, textvar=screenvalue, font="comicsans 30 bold",
               bg="lightGrey", fg="black", borderwidth=3, relief="groove")
screen.pack(fill=X, pady=20, padx=20, ipadx=10)
button_texts = ["(", ")", "%", "C","7", "8", "9","*","4","5","6","/","3","2","1","-","0",".","=","+"]
for i in range(1):
    f1 = Frame(root)
    f2 = Frame(root)
    f3 = Frame(root)
    f4 = Frame(root)
    f5 = Frame(root)
    for i in range(len(button_texts)):
        if i < 4:
            frame = f1
        elif i < 8:
            frame = f2
        elif i < 12:
            frame = f3
        elif i < 16:
            frame = f4
        else:
            frame = f5
        if button_texts[i] == "C":
            color = "red"
        elif button_texts[i] == "=":
            color = "slateblue"
        else:
            color = "white"
        b = Button(frame, text=button_texts[i], pady=3, padx=20, font="Helvetica 20 bold", bg=color)
        b.pack(side=LEFT, padx=3, pady=6)
        b.bind("<Button-1>",click)
        frame.pack()
        
status = StringVar()
status.set("Status : 0")
statusbar = Label(root, textvariable=status, relief="groove", anchor="w", padx=6, pady=3, font="helvetica 10 bold")
statusbar.pack(fill=X, side=BOTTOM)
root.mainloop()
