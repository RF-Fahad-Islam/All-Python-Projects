from test import getData, notifyme
import time
from bs4 import BeautifulSoup
url = "https://www.worldometers.info/coronavirus/"
htmlContent = getData(url)
soup = BeautifulSoup(htmlContent, "html.parser")
table = soup.find("table")
headings = table.find("thead").find_all("th")
contents = table.find_all("td")
contentText = ""
for content in contents:
    contentText += content.get_text()
    print(contentText)
    # print(contentText)
for heading in headings:
    headingText = heading.get_text()
    # print(headingText)
contentList = contentText.split("\n\n\n")
print(contentList)