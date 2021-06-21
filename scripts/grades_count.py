import pandas as pd

#csv generated from json
df = pd.read_csv('data\merged.csv')

df.dropna(axis = 0, inplace = True)
df.reset_index(inplace = True)
df.drop(columns=['index'], axis=1, inplace=True)
df.rename(columns = {'subject':'course', 'subject_grades':'grade', 'subject_session':'session'}, inplace = True)

for i in range(len(df['course'])):
  df.loc[i,'course'] = df.loc[i,'course'] + ' ' +df.loc[i,'session']

courses = {new_list: [] for new_list in df['course']}

courses_list = []
for i in df['course']:
  if i not in courses_list:
    courses_list.append(i)

grades_list = []
for i in df['grade']:
  if i not in grades_list:
    grades_list.append(i)

grades_list.sort()

for item, row in df.iterrows():
  courses[row.course].append(row.grade)

temp = {new_list: {} for new_list in df['course']}

for j in courses_list:
  test = {x: 0 for x in grades_list}
  for i in courses[j]:
    test[i]+=1
  temp[j] = test

new = pd.DataFrame.from_dict(temp, orient='index')
new.reset_index(inplace = True)

session_list = []
for i in range(len(new['index'])):
  session = new.loc[i,'index'][-8:]
  session_list.append(session)
  new.loc[i,'index'] = new.loc[i,'index'][:-9]

big_oof = pd.DataFrame()
big_oof['course'] = new['index']
big_oof['EX'] = new['EX']
big_oof['A'] = new['A']
big_oof['B'] = new['B']
big_oof['C'] = new['C']
big_oof['D'] = new['D']
big_oof['P'] = new['P']
big_oof['F'] = new['F']
big_oof['session'] = session_list

big_oof.to_csv(r'final_data\final_grades.csv', header = True, index = False)