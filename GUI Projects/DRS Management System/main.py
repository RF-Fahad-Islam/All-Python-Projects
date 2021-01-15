import threading
import time
from functools import partial
from tkinter import *
from tkinter.filedialog import askopenfilename

import cv2
import imutils
from PIL import Image, ImageTk

File = None
stream = None
def chooseVideo():
    '''Ask the path of the video'''
    global File
    global stream
    File = askopenfilename(defaultextension=".mp4", filetypes=[("Videos", "*.mp4")])
    stream = cv2.VideoCapture(File)
    play(0)
    
def play(speed):
    if stream != None:
        frame = stream.get(cv2.CAP_PROP_POS_FRAMES)
        stream.set(cv2.CAP_PROP_POS_FRAMES, frame + speed)
        grabbed, frame = stream.read()
        if not grabbed:
            stream.set(0,0)
        frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
        frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(-0,0,anchor=NW, image=frame)

    print(f"The speed is {speed}")
    
    
def showDecision(decisionType):
    print("Taking Decision")
    '''Make the decision depends on the out or not out'''
    frame = cv2.cvtColor(cv2.imread("decision.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH,height=SET_HEIGHT)
    photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=photo, anchor=NW)
    
    time.sleep(1)
    frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH,height=SET_HEIGHT)
    photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=photo, anchor=NW)
    time.sleep(1.5)
    
    if decisionType == "out":
        img = "out.png"    
    else:
        img = "not_out.png"
        
    frame = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH,height=SET_HEIGHT)
    photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=photo, anchor=NW)
    time.sleep(2)
    
def out():
    thread = threading.Thread(target=showDecision, args=("out",))
    thread.daemon = 1
    thread.start()

def not_out():
    thread = threading.Thread(target=showDecision, args=("not out",))
    thread.daemon = 1
    thread.start()

#Set width and height of screen
SET_WIDTH = 600
SET_HEIGHT = 380
#Create the Tkinter GUI Window
root = Tk()
#TODO: Create the canvas and show the image ground.png
root.title("DRS Decision Review Management System")
root.minsize(SET_WIDTH, SET_HEIGHT)
canvas = Canvas(root,width=SET_WIDTH, height=SET_HEIGHT)
cv_img = cv2.cvtColor(cv2.imread("ground.png"), cv2.COLOR_BGR2RGB)
cv_img = imutils.resize(cv_img, width=SET_WIDTH, height=SET_HEIGHT)
photo = ImageTk.PhotoImage(image=Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,anchor=NW, image=photo)
canvas.pack()
#TODO: Creating controll buttons
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

b1 = Button(f1, text="Choose Video", font="comicsans 12 bold",width=60, pady=3, padx=3, command=chooseVideo)
b1.pack(anchor=NE,side=LEFT, pady=6)

b1 = Button(f2, text="Next (fast) >>", font="comicsans 12 bold",width=30, pady=3, padx=3, command=partial(play, 25))
b1.pack(anchor=NE,side=LEFT, pady=6, padx=6)

b1 = Button(f2, text="<< Previous (fast)", font="comicsans 12 bold",width=30, pady=3, padx=3, command=partial(play, -25))
b1.pack(anchor=NE,side=LEFT, pady=6, padx=6)

b1 = Button(f3, text="Next (slow) >>", font="comicsans 12 bold",width=30, pady=3, padx=3, command=partial(play, 2))
b1.pack(side=LEFT, anchor=N, pady=6, padx=6)

b1 = Button(f3, text="<< Previous (slow)", font="comicsans 12 bold",width=30, pady=3, padx=3, command=partial(play, -2))
b1.pack(side=LEFT, anchor=N, pady=6, padx=6)

b1 = Button(f4, text="Give OUT", font="comicsans 12 bold",width=30, pady=3, padx=3, command=out)
b1.pack(side=LEFT, anchor=N, pady=6, padx=6)

b1 = Button(f4, text="Give NOT OUT", font="comicsans 12 bold",width=30, pady=3, padx=3, command=not_out)
b1.pack(side=LEFT, anchor=N, pady=6, padx=6)

f1.pack()
f2.pack()
f3.pack()
f4.pack()
root.mainloop()
