import json
import pandas as pd

def parse_json(filename=r'data\courses.json'):
    f = open(filename, encoding="utf8")
    data = json.load(f)
    return data

def code_to_name():
    data = parse_json()
    names = {}
    count = 0
    
    for stud in data:
        #subject.append(stud)
        data[stud]["name"] = data[stud]["name"].upper()
        names[stud] = data[stud]["name"]
        print(stud, data[stud]["name"])

    with open(r"data\oldCourseMapped.json", 'wt') as f:
        f.write(str(names))

code_to_name()