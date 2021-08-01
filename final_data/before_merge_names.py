import json
import pandas as pd

def parse_json(filename):
    f = open(filename, encoding="utf8")
    data = json.load(f)
    return data

def getGrades(filename=r'final_data\final_grades.csv'):
    f = pd.read_csv(filename)
    return f

def code_to_name():
    data = getGrades()
    names = {}
    count = 0
    for i in data["course"].unique():
        names[i[:7]] = i[9:]
        count += 1

    print(count)
    with open(r"final_data\newCourseMapped.json", 'wt') as f:
        f.write(str(names))

def merge_jsons():
    old = parse_json(r"final_data\oldCourseMapped.json")
    new = parse_json(r"final_data\newCourseMapped.json")
    old_ls = []
    new_ls = []
    temp = []

    for key in old:
        old_ls.append(key)

    print("old : ", len(old), " ", "old_ls : ", len(old_ls))

    for key in new:
        new_ls.append(key)

    for i in new_ls:
        if i not in old_ls:
            temp.append(i)

    for i in temp:
        old[i] = new[i]

    print("old : ", len(old), " ", "temp : ", len(temp))

    with open(r"final_data\courseMapped.json", 'wt') as f:
        f.write(str(old))


merge_jsons()