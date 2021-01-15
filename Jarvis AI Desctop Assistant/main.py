import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# Set Volume
# getting to know current volume level (min=0 and max=1)
volume = engine.getProperty('volume')
# print(volume)  # printing current volume level
engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1

rate = engine.getProperty('rate')   # getting details of current speaking rate
# print(rate)
engine.setProperty('rate', 180)     # setting up new voice rate")


def speak(audio):
    engine.say(audio)
    print("JARVIS : ", audio)
    engine.runAndWait()


def wishUser():
    hour = int(datetime.datetime.now().hour)
    if hour > 3 and hour < 12:
        speak("Good morining!")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon!")
    elif hour > 18 and hour < 22:
        speak("Good evening!")
    else:
        speak("Good night!")
    speak("This is Jarvis. May I help you?")


def info():
    # getting details of current speaking rate
    rate = engine.getProperty('rate')
    # volume = engine.getProperty('volume')
    voices = engine.getProperty('voices')
    return f"Speak rate : {rate} w/s Voice id : {voices[0]}"


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishUser()
    # query = takeCommand().lower()
    # takeCommand()
    if True:
        while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak("Searching...")
                query = query.replace('wikipedia', '')
                results = wikipedia.summary(query, sentences=2)
                speak(f"According to wikipedia: \n{results}")
            elif "open youtube" in query:
                webbrowser.open('youtube.com')
            elif "open google" in query:
                webbrowser.open('google.com')
            elif "open facebook" in query:
                webbrowser.open('facebook.com')
            elif "open stackoverflow" in query:
                webbrowser.open('stackoverflow.com')
            elif "open website" in query:
                speak("Which website do you want to open?")
                website = takeCommand().lower()
                webbrowser.open(website)
            elif "search" in query:
                speak("Which Content do you want to search?")
                website = takeCommand()
                webbrowser.open(website)
            elif "the time" in query:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {time}")
            elif "vs code" in query:
                codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            elif "perfect guise game" in query:
                path = "C:\\Users\\user\\Documents\\Python Codes\\Game Project\\perfect_guise_game.py"
                os.startfile(path)
            elif 'play music' in query:
                music_dir = 'C:\\Users\\user\\Music\\musics'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
                speak(f"playing {songs[0]}")
                            
            elif "exit" in query:
                speak("Exiting.....")
                exit()
