import pandas as pd

old = pd.read_csv(r'final_data\oldGrades.csv')
new = pd.read_csv(r'final_data\final_grades.csv')

for i in range(len(new)):
    new.loc[i,"course"] = new.loc[i,"course"][:7]
    #print(new.loc[i,"course"])
new["tbc"] = new["course"].astype(str) + " " + new["session"].astype(str)
old["tbc"] = old["subject"].astype(str) + " " + old["subject_session"].astype(str)
#print(old["tbc"])

df = pd.merge(new, old, on='tbc', how='inner')
a = df["tbc"].tolist()
new = new[~new['tbc'].isin(a)]
old.rename(columns = {'subject':'course', 'subject_session':'session'}, inplace = True)
print(len(old) + len(new))
final_data = new.append(old, ignore_index = True)
print(len(final_data), len(final_data.columns))
final_data.drop(['tbc'], axis = 1, inplace=True)
final_data.to_csv(r'final_data\final_grades.csv', index=False, header=True)
#print(df)