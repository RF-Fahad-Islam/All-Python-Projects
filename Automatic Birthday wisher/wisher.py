import pandas as pd
import datetime
import smtplib
from binary import binary_to_str
import os

os.chdir(r"C:\Users\user\Documents\Python Codes\Automatic Birthday wisher")
os.mkdir("Testing")
GMAIL_ID = "rfautomaticmailbot@gmail.com"
GMAIL_PSWD = binary_to_str("011000010111010101110100011011110110110101100001011101000110010101100010011011110111010001101111011001100110011001100001011010000110000101100100")

def sendEmail(to, sub, msg):
    print(f"Successfully sent email to : {to}\nSubject: {sub}\nMessage: {msg}")
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject:{sub}\n\n{msg}")
    s.quit()
    
    
if __name__ == "__main__":
    df = pd.read_csv("data.csv")
    today = datetime.datetime.now().strftime("%d-%m")
    yearnow = datetime.datetime.now().strftime("%Y")
    # print(today)
    # print(yearnow)
    wishedIndex = []
    for index, item in df.iterrows():
        # print(item["Birthday"])
        bday = str(item["Birthday"])
        if bday == str(today) and yearnow not in str(item["Wished Year log"]):
            sendEmail(item["Email"], item["Subject"], item["Message"])
            wishedIndex.append(index)
            
    # print(f"The index of wished : {wishedIndex}")
    if len(wishedIndex) != 0:
        for i in wishedIndex:
            yr = df.loc[i, "Wished Year log"]
            # print(f"The year : {yr}")
            df.loc[i, "Wished Year log"] = str(yr)+ "," + str(yearnow)
            df.to_csv("data.csv", index=False)
            