import pandas as pd
import json

def parse_json(filename=r'final_data\courseMapped.json'):
    f = open(filename, encoding="utf8")
    data = json.load(f)
    return data

def getGrades(filename=r'final_data\final_grades.csv'):
    f = pd.read_csv(filename)
    return f

def add_names():
    data = parse_json()
    grades = getGrades()
    codes = []
    for subj in data:
        codes.append(subj)

    count = 0
    for i in range(len(grades)):
        subj = grades.loc[i,'course']
        for code in codes:
            if subj == code:
                grades.loc[i,'course'] = grades.loc[i,'course'] + " : " + data[code]
                count += 1
        if len(grades.loc[i,'course']) == 10:
            grades.loc[i,'course'] = grades.loc[i,'course'][:7]
    grades.to_csv(r'final_data\final_grades.csv', index = False, header = True)

add_names()