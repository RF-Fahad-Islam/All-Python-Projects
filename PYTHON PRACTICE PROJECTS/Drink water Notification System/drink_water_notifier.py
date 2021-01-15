import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="**It's time to drink water.**",
            message="An adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            # app_icon="C:\\Users\\user\\Documents\\Python Codes\\Drink water Notification System\\water.png",
            timeout=12
        )
        time.sleep(6)
