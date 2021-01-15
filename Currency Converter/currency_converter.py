import requests
import json
import os
def fetchData(url):
    data = requests.get(url)
    with open("currency_data.json", "w") as f:
        f.write(data.text)
    return data.json()

def currencyData():
    if os.path.exists("currency_data.json"):
        with open("currency_data.json") as f:
            return f.read()
    else:
        return ""
    
if __name__ == "__main__":
    currencyDict = {}
    url = "https://api.currencyfreaks.com/latest?apikey=6f6441fc4a7744c8b8e92edc578fa422"
    fileData = currencyData()
    if fileData == "":
        print("Fetching...")
        data = fetchData(url)
    else:
        print("Reading...")
        data = json.loads(fileData)
        
    rates = data.get("rates")
    # print(rates)
    for rate in rates.keys():
        currencyDict[rate] = rates.get(rate)
        # print(rates.get(rate))
        # print(key)
def getInput():
    while True:
        a = input("Enter a currency form to USD conversions : ")
        perUSDRate = currencyDict.get(a.upper())
        if perUSDRate == None:
            print("Invalid Value!")
            getInput()
        print(f"OverView : {perUSDRate} {a} in 1$ (USD)")
        if a == "q":
            break
        value = input(f"Enter the {a} Amount : ")
        currencyvalue = 1 / float(perUSDRate)
        print(f"{float(currencyvalue)*int(value)}$ (USD)")
getInput()