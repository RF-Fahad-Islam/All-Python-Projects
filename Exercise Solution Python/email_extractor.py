import re #For searching the email pattern
import requests #For get the content of a URL
import pandas as pd #For saving the data to excel file
def fetchData(url):
    data = requests.get(url)
    return data.text

# url = "https://jsonplaceholder.typicode.com/users"
url = input("Enter the url : ")
data = fetchData(url)
mystr = data
# patt = re.compile(r"[0-9a-zA-Z._-%]+@[0-9a-zA-Z_-%]+[.][a-zA-Z.]+")
matches = re.findall(r"[0-9a-zA-Z(.)(_)(-)(%)&]+@[0-9a-zA-Z(_)(-)(%)]+[.][a-zA-Z.]+",mystr)
# matches = re.findall(r"\b[A-Za-z][a-zA-Z0-9]+\.\w+\b",mystr)
# matches = re.findall(r"\d{5}-\d{4}",mystr)
if len(matches) == 0:
    print("No matches found!")
else:
    df = pd.DataFrame(matches, columns=["Emails"])
    print(df)
    df.to_excel("emails.xlsx", index=False)
    with open("email-extract.txt", "w") as f:
        f.write("The E-mail extracted list here : ")
        for match in matches:
            # print(match)
            f.write(match+ "\n")