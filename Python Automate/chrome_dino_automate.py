import pyautogui
from PIL import Image, ImageGrab
import time
# from numpy import asarray


def hit(key):
    pyautogui.keyDown(key)


def isCollide(data):
    for i in range(250, 300):
        for j in range(250, 380):
            if data[i, j] < 100:
                hit("down")

    for i in range(250, 300):
        for j in range(380, 480):
            if data[i, j] < 100:
                hit("up")


if __name__ == "__main__":
    print("Starting in 3seconds...")
    time.sleep(3)
    print("Running....")
    hit("up")
    # pyautogui.moveRel(150, 300, duration=6)
    # while True:
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        isCollide(data)
        # isCollide(data)
    print(asarray(image))

    for i in range(250, 300):
        for j in range(250, 400):
            data[i, j] = 171
    # print(asarray(image))
    for i in range(250, 300):
        for j in range(380, 450):
            data[i, j] = 0
    image.show()
