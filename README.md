# UE-Calendar-Scraper
This is an automated web scraping script that will automatically log into University of Applied Sciences and download all the classes for that month. This will then write the data into a CSV file that can be exported to the desired calendar. Google calendar is recommended because not every calendar accepts csv files (apple calendar). If problems occur, feel free to notify me of the issue.

[Google's guide to adding Calendar](https://support.google.com/calendar/answer/37118?co=GENIE.Platform%3DDesktop&hl=en)

## Table of Contents
* [CSV File Example](#CSV-File-Example)
* [Requirements](#requirements)
* [Technologies](#technologies)
* [Future](#Future)

## CSV File Example:

Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private

Corporate Management # HH + B, 1/12/2020,14:00, 1/12/2020,16:15,False,Online Class,Online Class,True

Business English III: Case Studies, 1/12/2020,16:30, 1/12/2020,18:45,False,Online Class,Online Class,True

Taxes, 2/12/2020,08:30, 2/12/2020,10:45,False,Online Class,Online Class,True

Software Engineering Basics, 2/12/2020,11:00, 2/12/2020,13:15,False,B_A.01.61 (PC Pool 01),"Dessauer Street 5, 10963 Berlin",True

Case Studies, 2/12/2020,14:00, 2/12/2020,16:15,False,B_A.02.53 (Seminarraum 06),"Dessauer Street 5, 10963 Berlin",True

Digital Transformation, 3/12/2020,08:30, 3/12/2020,10:45,False,Online Class,Online Class,True

### Requirements:
The program only requires you to type in your username and password in the following box.
```
def __init__(self, username="", password=""):
  self.username = username
  self.password = password
  self.dict = {}
```

## Technologies: 
Project was created with:
* Python version: 3.7
* unicodecsv version: 0.14.1
* beautifulsoup4 version: 4.9.0
* requests version: 2.23.0

## Future:
From trial and error this is temporarily the best solution. Future changes can be made by using google calendar api. Currently, the libraries aren't working with my python version.
