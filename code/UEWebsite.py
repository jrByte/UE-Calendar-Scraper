import requests
import json
from bs4 import BeautifulSoup as bs
import os


class main:
    # Enter your username and password in the empty field bellow.
    def __init__(self, username="", password=""):
        with open(f"{os.path.dirname(os.getcwd())}/data/credentials.json", "r") as cred_file:
            cred = (json.load(cred_file))["ue"]
            if cred["username"] == "" and cred["password"] == "":
                raise Exception("username and password are empty, edit credentials file")
            cred_file.close()
        self.username = cred["username"]
        self.password = cred["password"]
        self.dict = {}

    def checkStatusCode(self, requestCode, url):
        if requestCode == 200:
            print("[✔]: Successfully connected to: " + url)
        else:
            print("[X]: Failed to connect, code response was [" + requestCode + "] with URL: " + url)

    print("[!]: Main class in UEWebsite is running.")

    def loginWebsite(self):
        # This is for the website to know what kind of browser we are using. This mitigates potential problems if the
        # website checks if this is a bot.
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 '
                          'Safari/537.36 '
        }

        with requests.Session() as request:
            # Connecting to the login page specified in the URL bellow.
            url = 'https://onlinecampus.bits-hochschule.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME' \
                  '=EXTERNALPAGES&ARGUMENTS=-N000000000000001,-N000299,-AHomedeWelcome '
            print("[!]: POST, Attempting to login.")
            print(
                "[!]: Note that if the KeyError is 'refresh'. Your username and password are either not entered or "
                "are incorrect.")
            login_data = {"usrname": self.username, "pass": self.password, "APPNAME": "CampusNet",
                          "PRGNAME": "LOGINCHECK",
                          "ARGUMENTS": "clino,usrname,pass,menuno,menu_type,browser,platform",
                          "clino": "000000000000001", "menuno": "000299", "menu_type": "Classic", "browser": "",
                          "platform": ""}
            # Making a post request to the website.
            site = request.post(url, login_data)

            # Below the code fetches the login token that the site gives us in the header response. This token is
            # basically our credentials and how the site knows it's us.
            loginToken = site.headers["REFRESH"]
            # TODO: This could potentially go cause problems with the size of the token. Currently it's fine.
            loginToken = str(loginToken[84:101])
            self.checkStatusCode(site.status_code, url)

            # The website operates by keeping your session token in the url itself. This is insecure, but is the only
            # way for me to access data for now.
            print("[✔]: Login token received." + loginToken)
            loginLocationURL = "/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=MONTH&ARGUMENTS=" + loginToken

            # This is now connecting to the calendar of the school for scheduled classes in the month view. Month is
            # specified via date. The for loop is iterating through months 10-12, this was just for the current
            # semester. Classes aren't posted any later than this range.
            for i in range(10, 13):
                dateCalendar = "01." + str(i) + ".2020"
                url = 'https://onlinecampus.bits-hochschule.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=MONTH' \
                      '&ARGUMENTS=' + loginToken + ",-N000354,-A" + dateCalendar + ",-A,-N000000000000000"

                # Sending a get request to the server for the month of classes.
                print("[✔]: Getting the month of:" + dateCalendar)
                site = request.get(url, headers=headers, )
                self.checkStatusCode(site.status_code, url)

                try:
                    # For windows computer
                    soup = bs(site.content, 'html5lib')
                    print("\n[✔]: Running html5lib parsing.\n")
                except Exception as e:
                    # For mac computer
                    soup = bs(site.content, 'lxml')
                    print("\n[X]: Exception:", e)
                    print("\n[✔]: Running lxml parsing.\n")

                number = 0
                specificMonth = soup.findAll("tr", class_="")
                for allDays in specificMonth:
                    daySchedule = allDays.findAll("td", class_="tbMonthDayCell")

                    for getDate in daySchedule:
                        daySpecific = getDate.findAll("div", class_="appMonth")
                        # print(daySpecific)
                        date = str(getDate.find("div", class_="tbMonthDay").get("title")) + dateCalendar[2:]

                        for classes in daySpecific:
                            link = classes.findAll("a", class_="apmntLink")

                            for linkParsed in link:
                                number = number + 1
                                linkParsed = str(linkParsed.get("title"))
                                print("[✔]: This link is being parsed: ", str(linkParsed))
                                Index = linkParsed.find('/')
                                timeRange = linkParsed[:Index - 1]
                                linkParsed = linkParsed[Index + 2:]

                                Index = linkParsed.find('/')
                                roomNumber = linkParsed[:Index - 1]
                                linkParsed = linkParsed[Index + 2:]

                                Index = linkParsed.find('/')
                                className = linkParsed
                                linkParsed = linkParsed[Index + 2:]

                                numberDict = str(number)
                                self.dict[numberDict] = {}
                                self.dict[numberDict]['ClassName'] = className
                                self.dict[numberDict]['RoomNumber'] = roomNumber
                                self.dict[numberDict]['TimeRange'] = timeRange
                                self.dict[numberDict]['Date'] = date


if __name__ == "__main__":
    session = main()
    session.loginWebsite()
