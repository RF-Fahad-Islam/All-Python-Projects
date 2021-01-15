import PIL.Image, PIL.ImageTk, PIL.ImageFilter, PIL.ImageGrab
import os
from tkinter import *
import tkinter.messagebox as tmsg
from functools import partial

def rotateImage():
    rotateDg = 45
    global photo, image  
    img = image.rotate(rotateDg)
    rotateDg += 30
    photo = PIL.ImageTk.PhotoImage(img)
    imageScreen.configure(image=photo)
    imageScreen.image = photo
    

def resizeImage():
    global photo, image
    tmsg.showinfo("Resize!", "Successfully resized!")   
    img = image.resize((255,255), PIL.Image.ANTIALIAS)
    photo = PIL.ImageTk.PhotoImage(img)
    imageScreen.configure(image=photo)
    imageScreen.image = photo
    
def filterImage(filterName):
    if filterName == "BLUR":
        photo = PIL.ImageTk.PhotoImage(image.filter(PIL.ImageFilter.BLUR))
    imageScreen.configure(image=photo)
    imageScreen.image = photo

def convertToBlackWhite():
    global photo, image
    photo = PIL.ImageTk.PhotoImage(image.convert("L"))
    imageScreen.configure(image=photo)
    imageScreen.image = photo


if __name__ == "__main__":
    root = Tk()
    # root.geometry("600x300")
    root.title("Image Editor")
    root.minsize(600, 300)
    # canvas = Canvas(root, width=600, height=300)
    image = PIL.Image.open("obj.jpg")
    image = image.filter(PIL.ImageFilter.BLUR)
    photo = PIL.ImageTk.PhotoImage(image)
    imageScreen = Label(image=photo)
    imageScreen.pack()
    img = PIL.ImageGrab.grabclipboard()
    
    # canvas.pack()
    # canvas.create_image(0,0,image=photo)
    b = Button(root, text="Resize Image", command=resizeImage)
    b.pack()
    b = Button(root, text="Blur Image", command=partial(filterImage, "BLUR"))
    b.pack()
    b = Button(root, text="Convert To Black And White", command=convertToBlackWhite)
    b.pack()
    b = Button(root, text="Rotate Image", command=rotateImage)
    b.pack()
    root.mainloop()