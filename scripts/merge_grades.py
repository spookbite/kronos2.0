import json
import pandas as pd

def parse_json(filename):
    f = open(filename, encoding="utf8")
    data = json.load(f)
    return data

def getGrades(filename=r'data\final_grades.csv'):
    f = pd.read_csv(filename)
    return f

def code_to_name():
    data = getGrades()
    names = {}
    count = 0
    for i in data["course"].unique():
        names[i[:7]] = i[8:]
        count += 1

    print(count)
    with open(r"data\newCourseMapped.json", 'wt') as f:
        f.write(str(names))

def merge_jsons():
    old = parse_json(r"kronosv1\oldCourseMapped.json")
    new = parse_json(r"data\newCourseMapped.json")
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

    with open(r"data\courseMapped.json", 'wt') as f:
        f.write(str(old))

def add_names():
    data = parse_json(r"data\courseMapped.json")
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
    grades.to_csv(r'data\final_grades.csv', index = False, header = True)

def merge_grades():

    old = pd.read_csv(r'data\oldGrades.csv')
    new = pd.read_csv(r'data\final_grades.csv')

    for i in range(len(new)):
        new.loc[i,"course"] = new.loc[i,"course"][:7]
        
    new["tbc"] = new["course"].astype(str) + " " + new["session"].astype(str)
    old["tbc"] = old["subject"].astype(str) + " " + old["subject_session"].astype(str)

    df = pd.merge(new, old, on='tbc', how='inner')
    a = df["tbc"].tolist()
    new = new[~new['tbc'].isin(a)]
    old.rename(columns = {'subject':'course', 'subject_session':'session'}, inplace = True)
    print(len(old) + len(new))
    final_data = new.append(old, ignore_index = True)
    print(len(final_data), len(final_data.columns))
    final_data.drop(['tbc'], axis = 1, inplace=True)
    final_data.to_csv(r'data\final_grades.csv', index=False, header=True)

#code_to_name()
#merge_jsons()
#add_names()
merge_grades()