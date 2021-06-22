import csv
import json
import os
import pandas as pd

def parse_json(filename='scripts\config.json'):
    f = open(filename)
    data = json.load(f)

    return data

def json_to_csv(roll_year):
    roll_year = roll_year
    config = parse_json()
    RAW_DATA_LOCATION = config["raw_data_location"]
    PROCESSED_DATA_LOCATION = config["processed_data_location"]
    DEPARTMENTS = config["departments"]

    for dep in DEPARTMENTS:
        f = open(os.path.join(RAW_DATA_LOCATION,
                              str(roll_year), f"{roll_year}{dep}_final.json"))

        data = json.load(f)
        subject_no = []
        subject_grades = []
        subject_session = []
        for stud in data:
            roll = list(stud.keys())[0]
            try:

                subject_data = stud[roll][0]
                #year should be roll year - 1
                year = roll_year
                prev = 0
                for sub in subject_data:
                    subject_no.append(sub["subno"] + '-' + sub["subname"])
                    #subject_name.append(sub["subname"])
                    subject_grades.append(sub["grade"])
                    if int(sub["semno"]) != prev:
                        if prev % 2 == 0:
                            prev += 1
                        else:
                            prev += 1
                            year += 1

                    if int(sub["semno"]) % 2 == 0:
                        subject_session.append("Spring" + str(year))
                    else:
                        subject_session.append("Autumn" + str(year))

                #results.append(subject_grades)
            except Exception as e:
                print(roll)
                print(e)

        df = pd.DataFrame()
        df['subject'] = subject_no
        df['subject_grades'] = subject_grades
        df['subject_session'] = subject_session

        df.to_csv(os.path.join(PROCESSED_DATA_LOCATION,
                              str(roll_year), f"{roll_year}{dep}.csv"), index = False, header=True)

        """f = open(os.path.join(PROCESSED_DATA_LOCATION,
                              str(roll_year), f"{roll_year}{dep}.csv"), "w")
        writer = csv.writer(f)

        for row in results:
            writer.writerow(row)"""

    return

def merge_csv(year):
    config = parse_json()
    PROCESSED_DATA_LOCATION = config["processed_data_location"]
    DEPARTMENTS = config["departments"]

    allResults = []

    for dep in DEPARTMENTS:
        f = open(os.path.join(PROCESSED_DATA_LOCATION,
                              str(year), f"{year}{dep}.csv"), "r")

        results = [i for i in csv.reader(f)]
        allResults.extend(results)

    f = open(os.path.join(PROCESSED_DATA_LOCATION, f"{year}.csv"), "w")
    w = csv.writer(f)

    for i in allResults:
        w.writerow(i)

def merge_year():
    config = parse_json()
    PROCESSED_DATA_LOCATION = config["processed_data_location"]
    YEARS = config["years"]

    allResults = []

    for year in YEARS:
        f = open(os.path.join(PROCESSED_DATA_LOCATION, f"{year}.csv"), "r")

        results = [i for i in csv.reader(f)]
        allResults.extend(results)

    f = open(os.path.join(PROCESSED_DATA_LOCATION, "merged.csv"), "w")
    w = csv.writer(f)

    for i in allResults:
        w.writerow(i)

#json_to_csv(17)
#merge_csv(17)
#merge_year()

