import json
import pandas as pd

def parse_json(filename=r'data\Grades\yearWiseGrades.json'):
    f = open(filename)
    data = json.load(f)

    return data

def json_to_csv():
    data = parse_json()
    count = 0
    subject = []
    subjects = []
    session = []
    ex = []
    a = []
    b = []
    c = []
    d = []
    p = []
    f = []
    for stud in data:
        subject.append(stud)

    for subj in subject:
        for i in data[subj]:
            #print(subj, i, data[subj][i]['A'])
            subjects.append(subj)
            session.append(i[4:] + i[2:4])
            ex.append(data[subj][i]['EX'])
            a.append(data[subj][i]['A'])
            b.append(data[subj][i]['B'])
            c.append(data[subj][i]['C'])
            d.append(data[subj][i]['D'])
            p.append(data[subj][i]['P'])
            f.append(data[subj][i]['F'])


    print(len(subjects))
    df = pd.DataFrame()
    df['subject'] = subjects
    df['EX'] = ex
    df['A'] = a
    df['B'] = b
    df['C'] = c
    df['D'] = d
    df['P'] = p
    df['F'] = f
    df['subject_session'] = session
    df.to_csv('oldGrades.csv', index=False, header=True)

"""df = json_to_csv()
res = df.transpose()
res.to_csv('test.csv')"""
json_to_csv()