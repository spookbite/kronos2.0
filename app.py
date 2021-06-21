import pandas as pd
import streamlit as st
#st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache
def get_data():
    return pd.read_csv('../final_data/final_grades.csv')

df = get_data()
st.title("Kronos v2.0 - The Gradekeeper")

st.write("")

#st.dataframe(df)
st.write("")
st.write("")

st.sidebar.title("Enter Course Code here:")

course = df['course'].unique()
course_choice = st.sidebar.selectbox('', course)
df_new = df[df['course'] == course_choice].copy()
df_new.reset_index(inplace=True)
df_new.drop(['index'], axis = 1, inplace=True)
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write(f'**Course chosen :**')
st.sidebar.write(f'*{course_choice}*')
#session = df["session"].unique()
#session_choice = st.sidebar.selectbox('Select the Session: ', session)
#grades = df_new[df_new['session'] == session]
#symbol = symbol_df['Symbol'].unique()
st.write(f'**Course chosen :** *{course_choice}*') #, **Session chosen :** *{session_choice}*')

st.write("")
st.dataframe(df_new)

st.write("")
st.write("")


df_new.set_index('session', inplace = True)
df_num = df_new.copy()
df_num.drop(['course'], axis = 1, inplace=True)


#number_of_students = st.checkbox("Show Graph w.r.t the Number of Students")
#if number_of_students:
st.markdown("<h2 style='text-align: center;'><b>Plot w.r.t the Number of Students</b></h2>", unsafe_allow_html=True)
st.write("")
st.write("")
xyz = df_num.transpose()
#xyz.reset_index(inplace=True)
#xyz.rename(columns = {'index':'grades'}, inplace = True)
#sns.lineplot(data=xyz, x="Grades", y="# of students", hue="session")
#st.write(xyz.dtypes)
st.dataframe(xyz)
st.write("")
#st.line_chart(xyz)
xyz.plot.line(figsize=(10,8))
st.pyplot(use_container_width = False)
st.write("")
st.write("")

#pct_of_students = st.checkbox("Show Graph w.r.t the Percentage of Students")
#if pct_of_students:
st.markdown("<h2 style='text-align: center;'><b>Plot w.r.t the Percentage of Students</b></h2>", unsafe_allow_html=True)
st.write("")
st.write("")
abc = df_num.transpose()
colNames = []
for (columnName, columnData) in abc.iteritems():
    colNames.append(columnName)
    abc[columnName] = (abc[columnName] / abc[columnName].sum()) * 100
#abc.drop(colNames, axis = 1, inplace=True)
st.dataframe(abc)
st.write("")
#st.line_chart(abc)
abc.plot.line()
st.pyplot()

#df_plot = pd.DataFrame(df_new, columns = ['Ex', 'A', 'B', 'C', 'D', 'P', 'F'])
#st.bar_chart(df_new['Ex','A','B','C','D','F','P'])

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Contribute to this project on <a href="http://github.com/spookbite/kronos2.0" target="_blank"> Github</a> | Developed with ❤ by kronos2.0 </p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
#st.markdown("<h4 style='text-align: center;'><b><i>Contribute to this project on <a href = 'http://github.com/spookbite/kronos2.0'>Github</a></i></b></h4>", unsafe_allow_html=True)