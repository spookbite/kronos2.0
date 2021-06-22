import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
#st.set_page_config(layout="wide")
st.set_page_config(page_title='Kronos2.0', initial_sidebar_state = 'auto')
st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache
def get_data():
    return pd.read_csv('final_data/final_grades.csv')

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
st.dataframe(xyz)
st.write("")
xyz.reset_index(inplace=True)
xyz.rename(columns = {'index':'grades'}, inplace = True)
xyz = xyz.melt('grades', var_name='academic_session',  value_name='# of students')

#c = alt.Chart(xyz).mark_line().encode(x='grades',y='# of students')
#st.altair_chart(c, use_container_width=True)

sns.factorplot(data=xyz, x="grades", y="# of students", hue="academic_session")
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

st.dataframe(abc)
st.write("")
abc.reset_index(inplace=True)
abc.rename(columns = {'index':'grades'}, inplace = True)
abc = abc.melt('grades', var_name='academic_session',  value_name='% of students')

sns.factorplot(data=abc, x="grades", y="% of students", hue="academic_session")
st.pyplot(use_container_width = False)

st.write("")
st.write("")

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
<p style='text-align: center;'>Contribute to this project on <a href="http://github.com/spookbite/kronos2.0" target="_blank"> Github</a> | Developed with ❤ by kronos2.0 </p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
#st.markdown("<h4 style='text-align: center;'><b><i>Contribute to this project on <a href = 'http://github.com/spookbite/kronos2.0'>Github</a></i></b></h4>", unsafe_allow_html=True)