import csv
import json
import os
import pandas as pd

def parse_json(filename="config.json"):
    f = open(filename)
    data = json.load(f)

    return data

def json_to_csv(roll_year):
    config = parse_json()
    RAW_DATA_LOCATION = config["raw_results_location"]
    PROCESSED_DATA_LOCATION = config["processed_data_location"]
    DEPARTMENTS = config["departments"]

    for dep in DEPARTMENTS:
        f = open(os.path.join(RAW_DATA_LOCATION,
                              str(year), f"{year}{dep}_final.json"))

        data = json.load(f)
        results = []
        for stud in data:
            roll = list(stud.keys())[0]
            try:

                subject_data = stud[roll][0]
                subject_grades = []
                #year should be roll year - 1
                year = roll_year-1
                prev = 0
                for sub in subject_data:
                    subject_grades.append(sub["subno"] + '-' + sub["subname"])
                    #subject_name.append(sub["subname"])
                    subject_grades.append(sub["grade"])
                    if int(sub["semno"]) != prev:
                        if prev % 2 == 0:
                            prev += 1
                            year += 1
                        else:
                            prev += 1

                    if int(sub["semno"]) % 2 == 0:
                        subject_grades.append("Spring" + str(year))
                    else:
                        subject_grades.append("Autumn" + str(year))

                results.append(subject_grades)
            except Exception as e:
                print(roll)
                print(e)

        

        f = open(os.path.join(PROCESSED_DATA_LOCATION,
                              str(year), f"{year}{dep}.csv"), "w")
        writer = csv.writer(f)

        for row in results:
            writer.writerow(row)

    return

json_to_csv(17)
#json_to_csv(18)
#json_to_csv(19)

"""f = open('18AE_final.json',)

data = json.load(f)

subject_no = []
subject_name = []
subject_grades = []
subject_session = []

for stud in data:
    roll = list(stud.keys())[0]
    try:

        subject_data = stud[roll][0]

        #year should be roll year - 1
        year = 17
        prev = 0
        for sub in subject_data:
            subject_no.append(sub["subno"] + '-' + sub["subname"])
            #subject_name.append(sub["subname"])
            subject_grades.append(sub["grade"])
            if int(sub["semno"]) != prev:
                if prev % 2 == 0:
                    prev += 1
                    year += 1
                else:
                    prev += 1

            if int(sub["semno"]) % 2 == 0:
                subject_session.append("Spring" + str(year))
            else:
                subject_session.append("Autumn" + str(year))

        #row = subject_grades
        #results.append(subject_grades)
    except Exception as e:
        print(roll)
        print(e)

print(len(subject_no), len(subject_grades), len(subject_session))

df = pd.DataFrame()
df['subject'] = subject_no
df['subject_grades'] = subject_grades
df['subject_session'] = subject_session

df.to_csv('aefinal.csv', index = False, header=True)"""