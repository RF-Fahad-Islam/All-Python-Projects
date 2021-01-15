import os
import pickle
import tkinter.messagebox as tmsg
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import (askopenfilename, asksaveasfile,
                                asksaveasfilename)
import tkinter.scrolledtext as scrolledtext
import pandas as pd
import requests
import keyboard
import time
import json
import re
import pyautogui
import PyPDF2
import pyttsx3
import wikipedia
from numpy import asarray
from functools import partial
import threading
import speech_recognition as sr

path = ""
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
        engine.setProperty("voice", voices[0].id)
        engine.save_to_file(txt, saveNameWav)
        tmsg.showinfo(
            f"Audio : {saveNameWav}", "Successfully convert text to audio file as (.wav) format!")


def speak(text):
    engine.setProperty("voice", voices[0].id)
    engine.say(text)
    if keyboard.is_pressed("esc"):
        engine.stop()
    engine.runAndWait()


def initial_speech(e="", voice="Male"):
    text = str(textArea.get(1.0, END))
    textToSpeech(text, voice)


def initial_voice(e=""):
    text = str(textArea.selection_get())
    if text != None:
        thread = threading.Thread(target=speak, args=(text,))
        thread.daemon = 1
        thread.start()
    else:
        thread = threading.Thread(target=speak, args=(textArea.get(1.0, END),))
        thread.daemon = 1
        thread.start()


def run_py_script(script):
    eval(script)


def newFile(e=""):
    global File
    root.title("Untitled - Notepad")
    File = None
    textArea.delete(1.0, END)


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
                    # os.startfile(File)
                    with open(File, "rb") as f:
                        textArea.insert(1.0, asarray(f.read()))
                    File = None
                    root.title("Untitled - Notepad")

                elif File.endswith(".xlsx"):
                    df = pd.read_excel(File)
                    textArea.insert(1.0, str(df))
                    # os.startfile(File)
                    File = None
                    root.title("Untitled - Notepad")

                elif File.endswith(".py"):
                    df = pd.read_excel(File)
                    textArea.insert(1.0, str(df))
                    # os.startfile(File)
                    File = None
                    root.title("Untitled - Notepad")

                # elif File.endswith(".csv"):
                #     df = pd.read_csv(File)
                #     textArea.insert(1.0, str(df))

                # elif File.endswith(".py"):
                #     with open(File, 'r') as f:
                #         textArea.insert(1.0, f.read())
                #         a = tmsg.askyesno("Run Python script!", "Do you want to run this python script.")
                #         if a=="yes":
                #             run_py_script(f.read())
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
        tmsg.showwarning(
            "Warning", "Please provide the save as (ctrl+shift+s) for untitled.txt option")


def saveFile(e=""):
    global File
    if File != None:
        # File = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if File == "":
            File = None
        else:
            tmsg.showinfo("Saved!", "Successfully saved the file!")
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


def undo():
    pyautogui.hotkey("ctrl", "z")


def redo():
    pyautogui.hotkey("ctrl", "y")

# Create the new window instance


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


def replace_word(e=""):
    word = pyautogui.prompt("Enter the word :")
    if word != None:
        wordRl = pyautogui.prompt("Enter the word to replace with : ")
        if wordRl != None:
            content = textArea.get(1.0, END)
            pattern = re.findall(word, content)
            if len(word) != 0:
                for word in pattern:
                    while word in content:
                        content = content.replace(word, wordRl)
                    textArea.delete(1.0, END)
                    textArea.insert(1.0, content)
                tmsg.showinfo("Replaced Successfully",
                              f"The \"{word}\" Replaced with \"{wordRl}\"")
            else:
                tmsg.showwarning(
                    f"No word like \"{word}\"", f"There is no word like \"{word}\" to replace""")


def news_writter(e=""):
    r = requests.get(
        "http://newsapi.org/v2/everything?q=bitcoin&from=2020-10-28&sortBy=publishedAt&apiKey=fcc85de3acfd4573897bb988e9cdf7b7")
    data = r.json()
    articles = data.get("articles")
    textArea.delete(1.0, END)
    for article in articles:
        source = article.get('source').get('name')
        title = article.get('title').split('-')[0]
        description = article.get("description")
        publishedAt = article.get("publishedAt")
        content = article.get("content")
        news = f"\n{title}-{publishedAt}\nDescription : {description}\nContent : {content}]\n\n-Source : {source}\n"
        textArea.insert(END, news)


def count_word(e=""):
    word = pyautogui.prompt("Enter a word to found : ")
    if word != None:
        content = textArea.get(1.0, END)
        matches = re.findall(word, content)
        if len(matches) != 0:
            tmsg.showinfo(
                "The count Result!", f"{len(matches)} matches found! 3 \"{word}\" words found.")
        else:
            tmsg.showinfo("No word found!",
                          f"There a no words like \"{word}\"")


def conversion(text):
    binary = ""
    for char in text:
        binary += format(ord(char), '08b')
    confirm = tmsg.askokcancel(f"Successfully converted to binary (Tap Enter)",
                               f"The binary format => {binary}.\n Do you want to insert to the document?")
    if confirm:
        textArea.insert(1.0, str(binary))


def str_to_binary(e=""):
    a = tmsg.askyesnocancel("Where you want to took the text file?",
                            "(Yes) => To convert the current notepad texts to binary\n(No) => To enter the desired text in a prompt\n(Cancel) => To cancel conversion")
    if a != None:
        if a:
            text = str(textArea.get(1.0, END))
        elif not a:
            text = pyautogui.prompt(
                "Enter the text that you want to convert to binary : ")
    if text != None and text != "":
        thread = threading.Thread(target=conversion, args=(text,))
        thread.daemon = 1
        thread.start()


def binary_to_str(e=""):
    # number of characters in text
    binary = pyautogui.prompt("Enter the binary code to convert to text : ")
    if binary != None:
        num = len(binary)/8
        text = ""
        for x in range(int(num)):
            start = x*8
            end = (x+1)*8
            text += chr(int(str(binary[start:end]), 2))
        textArea.insert(END, test)


def choose_font(e=""):
    global root, textArea  # I hate to use global, but for simplicity

    t = Toplevel()
    # t.geometry("300x100")
    t.wm_iconbitmap("notepad.ico")
    t.minsize(300, 100)
    t.title("Choose Font")
    font_name = Label(t, text='Font Name: ')
    font_name.grid(row=0, column=0, sticky='nsew')
    enter_font = Entry(t)
    enter_font.grid(row=0, column=1, sticky='nsew')
    font_size = Label(t, text='Font Size: ')
    font_size.grid(row=1, column=0, pady=3, sticky='nsew')
    enter_size = Entry(t)
    enter_size.grid(row=1, column=1, pady=3, padx=30, sticky='nsew')
    # * Combobox creation
    combobox = ttk.Combobox(root, width=27, textvariable=enter_size)

    def setsize():
        textArea.config(font=(enter_font.get(), int(enter_size.get())))
        tmsg.showinfo(
            "Applied!", f"Font :  {enter_font.get()}, Font Size : {enter_size.get()}")
    # associating a lambda with the call to text.config()
    # to change the font of text (a Text widget reference)
    ok_btn = Button(t, text='Apply Changes',
                    command=setsize)
    ok_btn.grid(row=2, column=1, sticky='nsew')
    done = Button(t, text='Close', bg="red", command=t.destroy)
    done.grid(row=4, column=1, sticky='nsew')


def word_wrap(e=""):
    print(var1.get())
    if var1.get() == 1:
        textArea["wrap"] = "word"
    else:
        textArea["wrap"] = "none"


def get_time(e=""):
    date = time.asctime(time.localtime(time.time()))
    textArea.insert(END, date)


def search_to_wikipedia(e=""):
    query = pyautogui.prompt("Enter the query to search in wikipedia : ")
    if query != None:
        try:
            results = wikipedia.summary(query)
            textArea.insert(1.0, f"\n{results}\n")
        except Exception as e:
            tmsg.showwarning("No Search Results found!", f"{e}")


def requestGet(e=""):
    url = pyautogui.prompt("Enter a url to get GET request : ")
    if url != None:
        try:
            r = requests.get(url)
            data = r.content
            textArea.delete(1.0, END)
            textArea.insert(1.0, data)
        except Exception as e:
            tmsg.showerror("Some Problem Ocurred!", f"{e}")


def initialize_get_request(e=""):
    thread = threading.Thread(target=requestGet)
    thread.daemon = 3
    thread.start()


def takeCommand():
    r = sr.Recognizer()
    tmsg.showinfo("Voice Typing Started!", "Voice typing has been started. Say something that you want to type to th notepad. For stopping the listening stop to speak, it will automatically stop to type.")
    with sr.Microphone() as source:
        root.title("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        root.title("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        textArea.insert(END, str(query))
    except Exception as e:
        a = tmsg.askokcancel("Can't Recognize!",
                             f"Please say that again : {e}")
        if a == True:
            convert_speech_to_text()
    root.title("Untitled - Notepad")


def convert_speech_to_text(e=""):
    try:
        thread = threading.Thread(target=takeCommand)
        thread.daemon = 3
        thread.start()
    except Exception as e:
        tmsg.showerror("Some Problem Occurred!", f"{e}")


def removePunctuations(e=""):
    punc = "`!@#$%^&*-\"':;|\\/?.,"
    selectText = textArea.selection_get()
    text = textArea.get(1.0, END)
    print(text)
    result = ""
    if selectText == None:
        for char in text:
            if char not in punc:
                result += char
    else:
        for char in selectText:
            if char not in punc:
                result += char
    textArea.delete(1.0, END)
    textArea.insert(1.0, result)


def removeExtraSpaces(e=""):
    selectText = textArea.selection_get()
    # text = textArea.get(1.0, END)
    result = ""
    if selectText == None:
        text = textArea.get(1.0, END)
    else:
        text = selectText

    for index, char in enumerate(text):
        if not(text[index] == " " and text[index+1] == " " or text[index] == "\n"):
            result += char
    textArea.delete(1.0, END)
    textArea.insert(1.0, result)


def toUpperCase(e=""):
    selectText = textArea.selection_get()
    if selectText == None:
        text = textarea.get(1.0, END)
    else:
        text = selectText

    textArea.delete(1.0, END)
    textArea.insert(1.0, text.upper())


def toLowerCase(e=""):
    selectText = textArea.selection_get()
    if selectText == None:
        text = textarea.get(1.0, END)
    else:
        text = selectText

    textArea.delete(1.0, END)
    textArea.insert(1.0, text.lower())


def window(e=""):
    root = Tk()
    root.geometry("600x400")
    # Title of Notepad (Default)
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")
    # TODO: Add a Text widget
    SVBar = Scrollbar(root)
    SVBar.pack(side=RIGHT,
               fill="y")

    SHBar = Scrollbar(root,
                      orient=HORIZONTAL)
    SHBar.pack(side=BOTTOM,
               fill="x")

    textArea = scrolledtext.ScrolledText(root, font="comicsans 12", wrap="none", undo=True, maxundo=-1,
                                         autoseparators=True, yscrollcommand=SVBar.set, xscrollcommand=SHBar.set, pady=3, padx=6)
    SVBar.config(command=textArea.yview)
    SHBar.config(command=textArea.xview)
    textArea.pack(fill=BOTH, expand=True)
    # "text" is a Tkinter Text

    # configuring a tag with a certain style (font color)
    textArea.tag_configure("red", foreground="red")
    File = None
    # TODO: Create Mainmenu with submenus
    mainmenu = Menu(root)
    # * The submenu File Menu
    filemenu = Menu(mainmenu, tearoff=0)
    # * Add the filemenu commands New, Save, Open and Exit
    filemenu.add_command(label="New Window  (Ctrl+Shift+N)", command=window)
    filemenu.add_command(label="New  (Ctrl+N)", command=newFile)
    filemenu.add_command(label="Open  (Ctrl+O)", command=openFile)
    filemenu.add_separator()
    filemenu.add_command(label="Save  (Ctrl+S)", command=saveFile)
    filemenu.add_command(label="Save As  (Ctrl+Shift+S)", command=saveAsFile)
    filemenu.add_command(label="Print", command=printdoc)
    filemenu.add_separator()
    filemenu.add_command(label="Exit (ESC)", command=root.destroy)
    mainmenu.add_cascade(label="File", menu=filemenu)
    # * Creating Edit Menu
    editmenu = Menu(mainmenu, tearoff=0)
    # * Add The Copy, Cut, Paste
    editmenu.add_command(label="Select All  (Ctrl+A)", command=selectall)
    editmenu.add_separator()
    editmenu.add_command(label="Copy  (Ctrl+C)", command=copy)
    editmenu.add_command(label="Cut  (Ctrl+X)", command=cut)
    editmenu.add_command(label="Paste  (Ctrl+P)", command=paste)
    editmenu.add_separator()
    editmenu.add_command(label="Undo  (Ctrl+Z)", command=undo)
    editmenu.add_command(label="Redo  (Ctrl+Y)", command=redo)
    editmenu.add_separator()
    editmenu.add_command(
        label="Remove Punctuations  (Ctrl+Shift+P)", command=removePunctuations)
    editmenu.add_command(
        label="Remove Extra Spaces  (Ctrl+Shift+S)", command=removeExtraSpaces)
    editmenu.add_command(
        label="To Upper Case  (Ctrl+Alt+U)", command=toUpperCase)
    editmenu.add_command(
        label="To Lower Case  (Ctrl+Alt+L)", command=toLowerCase)
    editmenu.add_separator()
    editmenu.add_command(label="Replace  (Ctrl+Shift+R)", command=replace_word)
    editmenu.add_command(label="Word Finder  (F3)", command=count_word)
    editmenu.add_command(label="Get Time  (F5)", command=get_time)

    mainmenu.add_cascade(label="Edit", menu=editmenu)
    # *Add a tool menue=""
    toolmenu = Menu(mainmenu, tearoff=0)
    # *Add tool commands
    speakmenu = Menu(toolmenu, tearoff=0)
    toolmenu.add_command(label="Speak  (Ctrl+Alt+/)", command=initial_voice)
    speakmenu.add_command(
        label="Male", command=partial(initial_speech, voice=""))
    speakmenu.add_command(
        label="Female", command=partial(initial_speech, voice=""))
    toolmenu.add_cascade(label="Convert Text to Audio file", menu=speakmenu)
    toolmenu.add_separator()
    toolmenu.add_command(
        label="Convert Text to Binary (Ctrl+`)", command=str_to_binary)
    toolmenu.add_command(label="Convert Binary to Text (Ctrl+Alt+`)")
    toolmenu.add_separator()
    toolmenu.add_command(label="News Writter  (Ctr+Atl+N)",
                         command=binary_to_str)
    toolmenu.add_separator()
    toolmenu.add_command(
        label="GET Request by URL  (Ctrl+Alt+G)", command=initialize_get_request)
    toolmenu.add_command(
        label="Get Search results from Wikipedia  (F8)", command=search_to_wikipedia)
    toolmenu.add_separator()
    toolmenu.add_command(label="Voice Typing  (F1)",
                         command=convert_speech_to_text)
    mainmenu.add_cascade(label="Tool", menu=toolmenu)

    # Advanced Tool Menu
    # adtoolmenu = Menu(mainmenu, tearoff=0)
    # mainmenu.add_cascade(label="Advanced Tools", menu=adtoolmenu)

    # *Format menu
    var1 = IntVar()
    formatmenu = Menu(mainmenu, tearoff=0)
    formatmenu.add_checkbutton(
        label="Word Wrap", onvalue=1, offvalue=0, variable=var1, command=word_wrap)
    mainmenu.add_cascade(label="Format", menu=formatmenu)

    # *Add a view menu
    viewmenu = Menu(mainmenu, tearoff=0)
    viewmenu.add_command(
        label="Switch Theme  (Ctrl+Alt+S)", command=switchTheme)
    viewmenu.add_command(
        label="Choose Font  (Ctrl+Alt+F)", command=choose_font)
    mainmenu.add_cascade(label="View", menu=viewmenu)
    # * Add Help Menu
    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="About", command=aboutApp)
    mainmenu.add_cascade(label="Help", menu=helpmenu)
    # * Status bar
    statusbar = StringVar()
    statusbar.set("Working")
    bar = Label(root, relief=SUNKEN, textvariable=statusbar,
                anchor="w", font="helvatica 12 bold")
    bar.pack(fill=X, side=BOTTOM, padx=10, pady=20)

    # * Configure the mainmenu
    root.bind("<Control-s>", saveFile)
    root.bind("<Control-n>", newFile)
    root.bind("<Control-N>", window)
    root.bind("<Control-S>", saveAsFile)
    root.bind("<Control-o>", openFile)
    # root.bind("<Control-z>", undo)
    # root.bind("<Control-y>", redo)
    root.bind("<Control-f>", count_word)
    root.bind("<Control-R>", replace_word)
    root.bind("<Control-S>", removeExtraSpaces)
    root.bind("<Control-P>", removePunctuations)
    root.bind("<Control-Alt-/>", initial_speech)
    root.bind("<Control-Alt-s>", switchTheme)
    root.bind("<Control-Alt-f>", choose_font)
    root.bind("<Control-`>", str_to_binary)
    root.bind("<Control-Alt-`>", binary_to_str)
    root.bind("<F3>", count_word)
    root.bind("<F5>", get_time)
    root.bind("<F1>", convert_speech_to_text)
    root.bind("<F8>", search_to_wikipedia)
    root.bind("<Control-Alt-g>", requestGet)
    root.bind("<Control-Alt-u>", toUpperCase)
    root.bind("<Control-Alt-l>", toLowerCase)
    root.bind("<Control-Alt-n>", news_writter)
    root.bind('<Escape>', lambda e: root.destroy())
    root.config(menu=mainmenu)
    globals().update(locals())
    root.mainloop()


window()
