from tkinter import *
import tkinter.messagebox as tmsg
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from mutagen.mp3 import MP3
import pygame
import time
# import class_objects
pygame.init()
pygame.mixer.init()
music = pygame.mixer.music
music_length = 0
music_file = None
music_path = None
music_pos = 0
current_music = None
paused = False
mp3 = []
count = 0
i = 0
bollean = pygame.mixer.music.get_busy()
content = ""
FileLength = 0
#TODO: To show the info of the GUI
def about():
    tmsg.showinfo("About", "This music player is created by Fahad")


#TODO: To save the music list on a file
def save_mp3_list():
    with open('mp3.txt', 'w') as f:
        f.write("\n".join(mp3))
        tmsg.showinfo("Saved mp3 list",
                      "Your mp3 list saved successfully on (mp3.txt).")

#TODO: To get saved the music list on a file
def get_save_musics():
    global mp3
    global content
    global music_file
    global count
    if count == 0:
        with open('mp3.txt') as f:
            content = f.read()
            mp3 = list(content.split("\n"))
            music_file = os.path.dirname(mp3[0])
            for music in mp3:
                listbox.insert(END, os.path.basename(music))
            count += 1
            
#TODO: To let the user add liked music
def add_new():
    global mp3
    music_file = askopenfilename(defaultextension=".mp3", filetypes=[
                                 ("Mp3 Files", "*.mp3"), ("Wav Files", "*.wav")])
    if (music_file) not in mp3:
        listbox.insert(END, os.path.basename(music_file))
        mp3.append(music_file)
        print(mp3)
    else:
        tmsg.showwarning("Duplicate mp3", f"{File} is already exists")

#TODO: A Important function to to extract all the mp3 music files from a directory
def extract_music():
    global mp3
    global music_file
    music_file = askdirectory()
    # os.chdir(music_file)
    files = os.listdir(music_file)
    for File in files:
        if File.endswith(".mp3"):
            if (os.path.join(music_file, File)) not in mp3:
                listbox.insert(END, os.path.basename(File))
                mp3.append(
                    str(os.path.join(music_file, os.path.basename(File))))
            else:
                tmsg.showwarning("Duplicate mp3", f"{File} is already exists")
                print(mp3)
    if len(mp3) == 0:
        tmsg.showwarning(
            "MP3 Not Found!", f"No Mp3 Files found on this {music_file} directory to Extract. Please provide a directory for extracting mp3 files.")

#TODO: To get the value of selected item in listbox
def get_activate_value(event):
    value = listbox.curselection()
    print(value)

#TODO: To set a play loop count
def setLoop():
    global i
    i += 1
    time.sleep(2)
    initial_music_play()

#TODO: The initial music play function to initialize the music play task using controller function
def initial_music_play():
    global music_path
    global status
    global paused
    paused = False
    if music_file != None:
        value = str(listbox.get(ACTIVE))
        music_path = os.path.join(music_file, os.path.basename(listbox.get(ACTIVE)))
        controll_music(music_path, "play")

#TODO: A controller function to control the play, pause
def controll_music(music_path, command, addqueque=False):
    global music_length
    global i
    global current_music
    global paused
    global bollean
    global music_pos
    global FileLength
    music.load(music_path)
    current_music = os.path.basename(music_path)
    if command == "play":
        music.play()
        if i > 0:
            music.play(i)
        try:
            a = pygame.mixer.Sound(music_path)
            FileLength = a.get_length()
            print(f"The length of music : {music.get_pos()}")
            music_length = music.get_pos()
            TrackPlay()
        except Exception as e:
            tmsg.showerror("Some Problem Occurred!", f"{e}")
        status.set(f"Playing => {current_music} ({round(FileLength)} seconds)")
        statusbar.update()
    if command == "pause":
        music.pause()
        status

    if command == "resume":
        music.unpause()

    if command == "rewind":
        music.rewind()
    if addqueque == True:
        music.queue(os.path.join(music_file, listbox.get(ACTIVE)))
    paused = True
    i = 0
 
#TODO: Pause Function to pause the music   
def pause_music():
    global paused
    paused = True
    if music_path != None:
        controll_music(music_path, "pause")
        status.set(f"Pause => {current_music} ({round(music_length)} seconds)")

#TODO:Track the length of Music        
def TrackPlay():
    global music_pos
    if music.get_busy():
        music_pos = music.get_pos()
        current = music_pos #.get_pos() returns integer in milliseconds
        print( 'current = ', current, type(current) )
        slider_value.set( current/1000 ) #.set_pos() works in seconds
        print( 'slider_value = ', slider_value.get(), type(slider_value.get()) )
        root.after(1000, lambda:TrackPlay() ) # Loop every sec


#TODO:Set slider to mp3 file position
def ProgressBar( value ):
    print('\ndef ProgressBar( value ):')
    print('value = ', value, type(value))
    slider_value.set( value )
    # slider.update()
    print('slider_value.get() = ', slider_value.get(), type(slider_value.get()) )
    print('value = ', value, type(value) )
    # slider.configure(from_=slider_value.get())

# !Working on this function
def resume_music():
    if music_path != None:
        controll_music(music_path, "unpause")


# def rewind_music():
#     if music_path != None:
#         controll_music(music_path, "rewind")
def increase5():
    global music_pos
    global bollean
    bollean = True
    music_pos = music_pos+5000
    a = int(music_pos/1000)
    # music.load(music_path)
    pygame.mixer.music.load(music_path)
    # pygame.mixer.music.set_pos((music_pos + 5000)/1000)
    music.play(0, a)
    print(a)

def delete_music():
    global mp3
    index = listbox.curselection()
    value = str(listbox.get(ACTIVE))
    confirm = tmsg.askokcancel(
        f"Remove {value} music file!", f"Do you really want to remove the {value} Music from playlist")
    if confirm:
        listbox.delete(index)
        for i in index:
            mp3.remove(str(os.path.join(music_file, value)))
            print(mp3)


def delete_all():
    global mp3
    tmsg.showwarning(
        "Warning!", "Your all mp3 files will be deleted from the list!")
    confirm = tmsg.askokcancel(
        "Remove All mp3 files", "Do you really want to clear or remove all songs from the playlist?")
    if confirm:
        listbox.delete(1, "end")
        mp3 = []

if __name__ == "__main__":
    root = Tk()
    root.geometry("700x600")
    root.minsize(700, 600)
    root.title("Music Player")
    # root.wm_iconbitmap("Tkinter/music-player.ico")

    #!Listbox
    scrollbar = Scrollbar(root)
    scrollbar.pack(fill=Y, side=RIGHT)
    listbox = Listbox(root, yscrollcommand=scrollbar.set, font="Helvatica 12 bold")
    scrollbar.config(command=listbox.yview)
    listbox.pack(fill=X, padx=30, pady=20)
    listbox.insert(END, f"Songs_list")
    listbox.bind("<<ListboxSelect>>", get_activate_value)

    if os.path.exists("mp3.txt"):
        with open('mp3.txt') as f:
            if f.read() != "":
                get_save_musics()

    # !Buttons
    f1 = Frame(root)
    f2 = Frame(root)
    f3 = Frame(root)
    f4 = Frame(root)
    b = Button(f1, text="Add New", font="Helvatica 10 bold",
               padx=20, pady=10, command=add_new)
    b.pack(anchor="n", side=LEFT, padx=30, pady=10)
    b = Button(f1, text="Extract Mp3", font="Helvatica 10 bold",
               padx=20, pady=10, command=extract_music)
    b.pack(anchor="n", side=LEFT, padx=30, pady=10)
    b = Button(f1, text="Remove", font="Helvatica 10 bold",
               padx=20, pady=10, command=delete_music)
    b.pack(anchor="n", side=LEFT, padx=30, pady=10)

    b = Button(f2, text="Play", font="Helvatica 10 bold",padx=20, pady=10, command=initial_music_play)
    b.pack(anchor="n", side=LEFT, padx=30, pady=10)
    b = Button(f2, text="Pause", font="Helvatica 10 bold",
               padx=20, pady=10, command=pause_music)
    b.pack(anchor="n", side=LEFT, padx=30, pady=10)

    b = Button(f3, text="+5sec", font="Helvatica 10 bold", padx=20, pady=10, command=increase5)
    b.pack(anchor="n", side=LEFT, padx=30, pady=10)
    
    b = Button(f3, text="Rewind", font="Helvatica 10 bold", padx=20, pady=10, command=initial_music_play)
    b.pack(anchor="n", side=LEFT, padx=30, pady=10)

    b = Button(f3, text="Remove All", font="Helvatica 10 bold", padx=20, pady=10, command=delete_all)
    b.pack(anchor="n", side=LEFT, padx=30, pady=10)
    
    b = Button(f4, text="Loops", font="Helvatica 10 bold", padx=20, pady=10, command=setLoop)
    b.pack(anchor="n", side=LEFT, padx=30, pady=10)
    b = Button(f4, text="Save List", font="Helvatica 10 bold",padx=20, pady=10, command=save_mp3_list)
    b.pack(anchor="n", side=LEFT, padx=30, pady=10)

    f1.pack()
    f2.pack()
    f3.pack()
    f4.pack()

    # Menu
    mainmenu = Menu(root)
    filemenu = Menu(mainmenu)
    filemenu.add_command(label="Add new", command=add_new)
    filemenu.add_command(label="Extract mp3", command=extract_music)
    filemenu.add_command(label="Save", command=add_new)
    mainmenu.add_cascade(label="File", menu=filemenu)

    toolmenu = Menu(mainmenu)
    toolmenu.add_command(label="Delete Item", command=delete_music)
    toolmenu.add_command(label="Delete All", command=delete_all)
    toolmenu.add_command(label="Add to next", command=delete_all)
    mainmenu.add_cascade(label="Tools", menu=toolmenu)

    controller = Menu(mainmenu)
    controller.add_command(label="+5sec", command=delete_music)
    controller.add_command(label="-5sec", command=delete_music)
    controller.add_command(label="Rewind", command=delete_music)
    mainmenu.add_cascade(label="Controller", menu=controller)

    helpmenu = Menu(mainmenu)
    helpmenu.add_command(label="About", command=about)
    mainmenu.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=mainmenu)

    slider_value = DoubleVar()
    slider = Scale( to=FileLength, orient=HORIZONTAL, length=500, resolution=1,
                    showvalue=True, tickinterval=30, variable=slider_value,
                command=ProgressBar)
    slider.pack()
    Label(text="Created By Fahad", font="Helvatica 15 bold", bg="white", padx=3, pady=3).pack(fill=X)
    Label(text="#CodeWithHarry", font="Helvatica 15 bold", bg="grey", fg="white", padx=3, pady=3).pack(fill=X, pady=10)
    # Status bar
    status = StringVar()
    status.set("No playing..")
    statusbar = Label(root, textvariable=status, relief="groove",
                      anchor='w', padx=10, pady=15, font="comicsans 10 bold")
    statusbar.pack(fill=X, side=BOTTOM)


    root.mainloop()
