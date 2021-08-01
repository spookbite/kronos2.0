import csv
import requests
import os

from tqdm import tqdm
from joblib import Parallel, delayed


# Get your cookies after logging in, and add the string to the Cookie key
HEADERS = {
    'Connection': 'keep-alive',
    'Cookie': "HAHAHAHAHA You thought I'd give you my session ID"
}

SYLLABUS_PATH = "./SYLLABUS"
os.makedirs(SYLLABUS_PATH, exist_ok=True)


def get_subject_codes(path):
    with open(path, "r") as f:
        reader = csv.reader(f)
        data = [i for i in reader]

        subject_codes = [i[0][:7] for i in data]

    subject_codes = set(subject_codes[1:])
    return subject_codes


def get_syllabus(subject_code):
    try:
        url = f"https://erp.iitkgp.ac.in/Acad/subject/get_syllabus_pdf.jsp?subno={subject_code}"
        r = requests.get(url, headers=HEADERS)

        # print(r.headers)
        # print(r.status_code)

        if r.headers['Content-Type'] != 'application/pdf;charset=UTF-8':
            return True

        path = os.path.join(SYLLABUS_PATH, f"{subject_code}.pdf")
        with open(path, "wb") as f:
            f.write(r.content)

        return True

    except Exception as e:
        print(e)
        return False


def get_syllabus_retry(subject_code):
    i = 0
    while i <= 2:
        if get_syllabus(subject_code):
            break
        i += 1


if __name__ == "__main__":
    subject_codes = get_subject_codes(r"final_data\final_grades.csv")
    Parallel(n_jobs=8)(delayed(get_syllabus_retry)(code)
                       for code in tqdm(subject_codes))
