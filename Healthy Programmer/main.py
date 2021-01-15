import os
from datetime import datetime
from time import time

from plyer import notification
from pygame import mixer

path = r"C:\Users\user\Documents\Python Codes\Healthy Programmer"
if path != os.getcwd():
    os.chdir(os.path.join(os.getcwd(), "Healthy Programmer"))
log_file_name = "mylog.log"

def mainsongloop(musicpath, stopper):
    mixer.init()
    mixer.music.load(musicpath)
    mixer.music.play(100)
    while True:
        print(f"Enter \"{stopper}\" to stop. Don't forget to do the task.")
        a = input("Enter the stopper code : ")
        if a == stopper:
            mixer.music.stop()
            break
def log_file(msg):
    print(msg)
    with open(log_file_name, "a") as f:
        f.write(f"{msg} [{datetime.now()}]\n")

def show_notification(tle, msg):
    notification.notify(
        title=tle,
        message=msg,
        timeout=12
    )
   
if __name__ == "__main__":
    print("\n\t\t\tWelcome to Healthy Programmer Software")
    initial_water = time()
    initial_eyes = time()
    initial_exercise = time()
    waterTime = 60*60
    water_level = 0     
    eyesTime = 40*60
    exerciseTime = 100*60
    print(f"\nThis software will remind you to :-\nDrink water in every {waterTime/60} minutes,\nRelax eyes in every {eyesTime/60} minutes,\nDo some physical exercise in every {exerciseTime//60} minutes")
    print(f"Note : Your activities will be logged in {log_file_name}")
    while True:
        if time() - initial_water > waterTime and water_level != 3500:
            mainsongloop("water.wav", "drank")
            log_file("Drink Water")
            water_level += 250
            show_notification("***Drink Water***", "It's time to drink water. Please drink water and notify the program that you drink water.")
            initial_water = time()
            
        if time() - initial_eyes > eyesTime:
            mainsongloop("eyes.wav", "eydone")
            log_file("Relax eyes")
            show_notification("***Relax Eyes***", "It's time to relax your eyes. Please remove your eyes from screen for few minutes.")
            initial_eyes = time()
            
        if time() - initial_exercise > exerciseTime:
            mainsongloop("exercise.wav", "phydone")
            show_notification("***Physical Exercise***", "It's time to do some physical exercise. Take away your sit and stand up and do some exercises to keep your health healthy")
            log_file("Physical exercise")
            initial_exercise = time()
        
        if water_level == 3500:
            print("Your today's goal is completed of drinking 3.5 liters of water. Continue to 3.5 liters to drink water everyday to be healthy")
            log_file("Total Drink 3.5 liters")
