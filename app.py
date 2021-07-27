import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os
import webbrowser

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

#st.write(f'**Course chosen :** *{course_choice}*') #, **Session chosen :** *{session_choice}*')

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
xyz = xyz.sort_index(axis=1)

fig = px.line(xyz, x=xyz.index, y = xyz.columns, width = 800, height = 600)
fig.update_layout(template="plotly_dark")
fig.update_layout(
    title=f"Grade Distribution for the Course : {course_choice[:7]}",
    xaxis_title="Grades",
    yaxis_title="Number of Students",
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#7f7f7f"
    )
)
st.plotly_chart(fig)

number_of_students = st.checkbox("Show data w.r.t # of students")
if number_of_students:
    st.write("")
    st.dataframe(xyz)

#xyz.reset_index(inplace=True)
#xyz.rename(columns = {'index':'grades'}, inplace = True)
#xyz = xyz.melt('grades', var_name='academic_session',  value_name='# of students')
#sns.factorplot(data=xyz, x="grades", y="# of students", hue="academic_session")
#st.pyplot()

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


fig2 = px.line(abc, x=abc.index, y = abc.columns, width = 800, height = 600)
fig2.update_layout(template="plotly_dark")
fig2.update_layout(
    title=f"Grade Distribution for the Course : {course_choice[:7]}",
    xaxis_title="Grades",
    yaxis_title="Percentage of Students",
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#7f7f7f"
    )
)
st.plotly_chart(fig2)

perct_of_students = st.checkbox("Show data w.r.t % of students")
if perct_of_students:
    st.write("")
    st.dataframe(abc)

#abc.reset_index(inplace=True)
#abc.rename(columns = {'index':'grades'}, inplace = True)
#abc = abc.melt('grades', var_name='academic_session',  value_name='% of students')

#sns.factorplot(data=abc, x="grades", y="% of students", hue="academic_session")
#st.pyplot()

st.write("")
st.write("")

course_to_get = course_choice[:7]
url = f"https://spookbite.github.io/kronos_syllabus/{course_to_get}.pdf"

test_syll = """from bokeh.models.widgets import Div
if st.button('Get Syllabus for the Course : '):
    js = "window.open({url})"  # New tab or window
    js = "window.location.href = 'https://share.streamlit.io/spookbite/kronos2.0/main/app.py'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)"""

syllabus = """
<h3 style='text-align: left;'><b>Syllabus for the course :</b></h3>

"""
st.markdown(syllabus, unsafe_allow_html=True)
#if st.button(f'Get Syllabus for the Course : {course_choice}'):
    #webbrowser.open_new_tab(url)
st.markdown(url, unsafe_allow_html=True)


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