from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title, text):
    ''''
    For giving notification
    '''
    notification.notify(
        title=title,
        message=text,
        app_icon=r"C:\Users\rashedul\Documents\Python Codes\Coronavirus Notification System\icon.ico",
        timeout=12
    )


def getData(url):
    ''''
    Get the data by requests module
    '''
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        url = "https://www.worldometers.info/coronavirus/"
        htmlContent = getData(url)
        soup = BeautifulSoup(htmlContent, "html.parser")
        # Get the desired data
        datas = soup.find_all("div", class_="maincounter-number")
        dataStr = ""
        # TODO: Split get text of the html elements then split to list with removing ("") from the list
        for data in datas:
            dataTxt = data.get_text()
            dataStr += dataTxt
        dataList = dataStr.split("\n")

        # TODO: Remove the none elements from the list
        while "" in dataList:
            dataList.remove("")
        # TODO: Initialize the notification title and message
        nTitle = "Cases of CoronaVirus world wide"
        nText = f"Total Cases : {dataList[0]}\nDeaths : {dataList[1]}\nRecovered : {dataList[2]}"
        notifyme(nTitle, nText)
        time.sleep(3600)
