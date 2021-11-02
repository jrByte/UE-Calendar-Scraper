import UEWebsite
import csv


def checkOnline(text):
    if "B_Digitaler" in text:
        return "Online Class"
    else:
        return text


def reformatDate(text):
    finalDate = ""
    Index = text.find('.')
    day = text[:Index]
    text = text[Index + 1:]
    Index = text.find('.')
    month = text[:Index]
    text = text[Index + 1:]
    year = text

    # print("Day: ", day, "Month: ", month, "Year: ", year)
    finalDate = str(day) + "/" + str(month) + "/" + str(year)
    return finalDate
    # Needs to return "05/30/2020"


def startTime(text):
    index = text.find("-")
    text = text[:index - 1]
    # print (text)
    return str(text)


def endTime(text):
    index = text.find("-")
    text = text[index + 2:]
    # print (text)
    return str(text)


class main:
    def __init__(self):
        self.timeDuration = None
        self.timeStart = None

    print("[!]: Main class in AppleCalendar is running.")
    ue = UEWebsite.main()
    ue.loginWebsite()
    print("\n[✔]: Data collected successfully, retrieving data for AppleCalendar class.\n")

    dataDict = ue.dict

    with open('../data/Calendar.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Writing the CSV File.
        employee_writer.writerow(['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'All Day Event'
                                     , 'Description', 'Location', 'Private'])
        for key in ue.dict:
            ue.dict[key]["RoomNumber"] = checkOnline(ue.dict[key]["RoomNumber"])
            date = reformatDate(str(ue.dict[key]["Date"]))
            classStartTime = startTime(ue.dict[key]["TimeRange"])
            classEndTime = endTime(ue.dict[key]["TimeRange"])
            # print(date)

            # Writing the CSV File.
            if ue.dict[key]["RoomNumber"] == "Online Class":
                employee_writer.writerow(
                    [str(ue.dict[key]["ClassName"]), date, classStartTime, date, classEndTime, False
                        , ue.dict[key]["RoomNumber"], ue.dict[key]["RoomNumber"], True])
            else:
                employee_writer.writerow(
                    [str(ue.dict[key]["ClassName"]), date, classStartTime, date, classEndTime, False
                        , ue.dict[key]["RoomNumber"], 'Dessauer Street 5, 10963 Berlin', True])


if __name__ == "__main__":
    session = main()
    print("[✔]: Finished collecting and creating Claendar.csv ")
