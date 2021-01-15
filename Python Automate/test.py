import pyautogui
import time
# time.sleep(3)
# distance = 200
# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.5)   # move right
#     distance -= 5
#     pyautogui.drag(0, distance, duration=0.5)   # move down
#     pyautogui.drag(-distance, 0, duration=0.5)  # move left
#     distance -= 5
#     pyautogui.drag(0, -distance, duration=0.5)  # move up
while True:
    a = pyautogui.locateOnScreen('obj.jpg')  # returns (left, top, width, height) of first place it is found
    if a != None:
        pyautogui.keyDown("up")