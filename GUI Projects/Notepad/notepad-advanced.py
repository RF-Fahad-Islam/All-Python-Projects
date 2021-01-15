import os
import pickle
import tkinter.messagebox as tmsg
from tkinter import *
from tkinter.filedialog import (askopenfilename, asksaveasfile,
                                asksaveasfilename, askdirectory)
import keyboard
import pandas as pd
import pyautogui
import PyPDF2
import pyttsx3
from numpy import asarray
from functools import partial
import threading

path = None
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# def textToSpeech(txt):
#     txt = str(txt)
#     language = "en"
#     obj = gTTS(text=txt, lang=language, slow=False)
#     obj.save("speak.mp3")
def textToSpeech(txt, voice="Male"):
    saveNameWav = asksaveasfilename(initialfile="Untitled.wav",
                                 defaultextension=".wav",
                                 filetypes=[("Wav Files", "*.wav")])
    if saveNameWav == "":
        saveNameWav = None
    else:
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        if voice=="Male":
            engine.setProperty("voice", voices[0].id)
        elif voice == "Female":
            engine.setProperty("voice", voices[1].id)
        engine.save_to_file(txt, saveNameWav)
        tmsg.showinfo(f"Audio : {saveNameWav}", "Successfully convert text to audio file as (.wav) format!")
        
def speak(text):
    engine.setProperty("voice", voices[0].id)
    engine.say(text)
    if keyboard.is_pressed("esc"):
        engine.stop()
    engine.runAndWait()

def initial_speech(e="", speak=False, voice="Male"):
    text = str(textArea.get(1.0, END))
    thread = threading.Thread(target=textToSpeech, args=(text,voice))
    thread.daemon = 1
    thread.start()

def initial_voice(e=""):
    text = str(textArea.get(1.0, END))
    thread = threading.Thread(target=speak, args=(text,))
    thread.daemon = 1
    thread.start()
    

def newFile(e=""):
    global File
    root.title("Untitled - Notepad")
    File = None
    textArea.delete(1.0, END)

def openFolder(e=""):
    global path 
    directory = askdirectory()
    if directory == "":
        path = None
    else:  
        files = os.listdir(directory)
        path = directory
        for File in files:
            listbox.delete(0, END)
            listbox.insert(0, os.path.basename(directory))
            listbox.insert(END, File)

def get_activate_value(e):
    value = listbox.get(ACTIVE)
    if value == "Untitled Folder":
        openFolder()
    if path != None:
        File = os.path.join(path, value)
        if os.path.basename(File) == os.path.basename(path):
            openFolder()
        else:
            textArea.delete(1.0, END)
            with open(File) as f:
                textArea.insert(1.0, f.read())
        
def openFile(e=""):
    try:
        global File
        global path
        File = askopenfilename(defaultextension=".txt", filetypes=[
                            ("All Files", "*.*"), ("Text Documents", "*.txt")])
        path = File
        if File == "":
            File = None
        else:
            Imgext = [".jpg", ".png", ".jpeg", ".img"]
            root.title(os.path.basename(File)+" - Notepad")
            root.update()
            textArea.delete(1.0, END)
            for ext in Imgext:
                if File.endswith(".pkl"):
                    with open(File, "rb") as f:
                        read = pickle.load(f)
                        textArea.insert(1.0, read)
                        
                elif File.endswith(ext):
                    with open(File, "rb") as f:
                        textArea.insert(1.0, asarray(f.read()))
                    File = None
                    
                elif File.endswith(".xlsx"):
                    df = pd.read_excel(File)
                    textArea.insert(1.0, str(df))
                    File = None    
                    
                # elif File.endswith(".csv"):
                #     df = pd.read_csv(File)
                #     textArea.insert(1.0, str(df))
                    
                elif File.endswith(".pdf"):
                    a = PyPDF2.PdfFileReader(File)
                    print(a)
                    for i in range(int(a.getNumPages())):
                        data = a.getDocumentInfo()
                        textArea.insert(1.0, data)
                        print(data)
                    File = None        
                else:  
                    with open(File, 'r') as f:
                        textArea.insert(1.0, f.read())
    except Exception as e:
        tmsg.showerror("Encoded File", f"{e}")

def saveAsFile(e=""):
    global File
    if File == None:
        File = asksaveasfilename(initialfile="Untitled.txt",
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if File == "":
            File = None
        else:
            with open(File, 'w') as f:
                f.write(textArea.get(1.0, END))
    else:
        tmsg.showwarning("Warning", "Please provide the save as (ctrl+shift+s) for untitled.txt option")


def saveFile(e=""):
    global File
    if File != None:
        # File = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if File == "":
            File = None
        else:
            tmsg.showinfo("Saved!","Successfully saved the file!")
            if File.endswith(".pkl"):
                with open(path, 'wb') as f:
                    pickle.dump(textArea.get(1.0, END), f)
            else:
                with open(path, 'w') as f:
                    f.write(textArea.get(1.0, END))
    else:
        tmsg.showwarning("Error(X)", "There is a error to save this file")


def printdoc():
    pyautogui.hotkey("ctrl", "p")
    # textArea.event_generate("<Print>")


def selectall():
    pyautogui.hotkey("ctrl", "a")


def copy():
    textArea.event_generate("<<Copy>>")


def cut():
    textArea.event_generate("<<Cut>>")


def paste():
    textArea.event_generate("<<Paste>>")

#Create the new window instance
def create_window():
    window = Toplevel(root)

def aboutApp():
    tmsg.showinfo("Notepad", "This Notepad GUI is created by Fahad")

def keydown(e):
    print(e.char)

def switchTheme(e=""):
    if textArea["bg"] != "black":
        textArea["fg"] = "white"
        textArea["bg"] = "black"
        textArea["insertbackground"] = "white"
    else:
        textArea["fg"] = "black"
        textArea["bg"] = "white"
        textArea["insertbackground"] = "black"
        
    
def window(e=""):
    root = Tk()
    root.geometry("600x400")
    # Title of Notepad (Default)
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("Tkinter/notepad.ico")
    frame = Frame(root)
    frame.pack(side=RIGHT, anchor=NE)
    sideMenu = Menu(frame)
    sideMenu.add_command(label="Hide")
    root.config(menu=sideMenu)
    # TODO: Add a Text widget
    ScrollBar = Scrollbar(root)
    ScrollBar2 = Scrollbar(root)
    ScrollBar2.pack(fill=Y, side=LEFT)
    ScrollBar.pack(fill=Y, side=RIGHT)
    # root.configure(bg="black")
    listbox = Listbox(root, font="comicsans 12 bold", yscrollcommand=ScrollBar2.set)
    listbox.pack(side=LEFT, anchor=NW, fill=Y, padx=12)
    listbox.insert(END, "Untitled Folder")
    listbox.bind("<<ListboxSelect>>", get_activate_value)

    
    textArea = Text(root, font="comicsans 12", yscrollcommand=ScrollBar.set, xscrollcommand=ScrollBar2.set, pady=3, padx=6)
    ScrollBar.config(command=textArea.yview)
    ScrollBar2.config(command=listbox.yview)
    textArea.pack(fill=BOTH, expand=True)
    File = None
    # TODO: Create Mainmenu with submenus
    mainmenu = Menu(root)
    # The submenu File Menu
    filemenu = Menu(mainmenu, tearoff=0)
    # Add the filemenu commands New, Save, Open and Exit
    filemenu.add_command(label="New Window  (Ctrl+Shift+N)", command=window)
    filemenu.add_command(label="New  (Ctrl+N)", command=newFile)
    filemenu.add_command(label="Open File  (Ctrl+O)", command=openFile)
    filemenu.add_command(label="Open Folder  (Ctrl+Shift+O)", command=openFolder)
    filemenu.add_separator()
    filemenu.add_command(label="Save  (Ctrl+S)", command=saveFile)
    filemenu.add_command(label="Save As  (Ctrl+Shift+S)", command=saveAsFile)
    filemenu.add_command(label="Print", command=printdoc)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.destroy)
    mainmenu.add_cascade(label="File", menu=filemenu)
    # Creating Edit Menu
    editmenu = Menu(mainmenu, tearoff=0)
    # Add The Copy, Cut, Paste
    editmenu.add_command(label="Select All  (Ctrl+A)", command=selectall)
    editmenu.add_separator()
    editmenu.add_command(label="Copy  (Ctrl+C)", command=copy)
    editmenu.add_command(label="Cut  (Ctrl+X)", command=cut)
    editmenu.add_command(label="Paste  (Ctrl+P)", command=paste)
    mainmenu.add_cascade(label="Edit", menu=editmenu)
    #Add a tool menue=""
    toolmenu = Menu(mainmenu, tearoff=0)
    #Add tool commands
    speakmenu = Menu(toolmenu, tearoff=0)
    toolmenu.add_command(label="Speak  (Ctrl+Alt+/)", command=initial_voice)
    speakmenu.add_command(label="Male", command=partial(initial_speech, "", False, "Male"))
    speakmenu.add_command(label="Female", command=partial(initial_speech, "", False, "Female"))
    toolmenu.add_cascade(label="Convert Text to Audio file", menu=speakmenu)
    mainmenu.add_cascade(label="Tool", menu=toolmenu)
    #Add a view menu
    viewmenu = Menu(mainmenu, tearoff=0)
    viewmenu.add_command(label="Switch Theme  (Ctrl+Alt+S)", command=switchTheme)
    mainmenu.add_cascade(label="View", menu=viewmenu)
    # Add Help Menu
    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="About", command=aboutApp)
    mainmenu.add_cascade(label="Help", menu=helpmenu)
    # Configure the mainmenu
    root.bind("<Control-s>", saveFile)
    root.bind("<Control-n>", newFile)
    root.bind("<Control-N>", window)
    root.bind("<Control-S>", saveAsFile)
    root.bind("<Control-o>", openFile)
    root.bind("<Control-Alt-/>", initial_speech)
    root.bind("<Control-Alt-s>", switchTheme)
    root.config(menu=mainmenu)
    globals().update(locals())
    root.mainloop()
window()
