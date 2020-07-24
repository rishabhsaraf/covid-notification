from plyer import notification
import requests
import time

from bs4 import BeautifulSoup

def notifyme(title,message):
     notification.notify(
         title= title,
         message = message,
         app_icon = "C:\\Users\\User\\Downloads\\virus.ico",
         timeout = 6
     )

def getdata(url):
    r = requests.get(url)
    return r.text
while True:
    # notifyme("ayaz", "let end this virus together")
    myhtml = getdata("https://www.mohfw.gov.in/")
    # print(myhtml)
    myhtmlstr = ""
    soup = BeautifulSoup(myhtml, "html.parser")
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myhtmlstr += tr.get_text()
        myhtmlstr = myhtmlstr[0:]
        a = myhtmlstr.split("\n\n")
    state = ['Madhya Pradesh', 'Uttar Pradesh', "Gujarat"]

    for item in a[0:35]:

        datalist = item.split("\n")
        if datalist[1] in state:
            print(datalist)
            title1 = 'Case of Covid19'
            text1 = f"{datalist[1]}:\nActive Case: {datalist[2]}  Cured: {datalist[3]} Death: {datalist[4]}   Total Confirm:{datalist[5]}"
            notifyme(title1, text1)
            time.sleep(10)
    time.sleep(10  )