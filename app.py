import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
import altair as alt
st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache
def get_data():
    return pd.read_csv('au20_new.csv')

df = get_data()
st.title("Kronos v2.0 - the gradekeeper")

st.write("")

#st.dataframe(df)
st.write("")
st.write("")

st.sidebar.title("Enter Course Code here:")

course = df['course']
course_choice = st.sidebar.selectbox('', course)
df_new = df[df['course'] == course_choice].copy()
df_new.reset_index(inplace=True)
df_new.drop(['index'], axis = 1, inplace=True)
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


number_of_students = st.checkbox("Show Graph w.r.t the Number of Students")
if number_of_students:
    xyz = df_num.transpose()
    xyz.rename(columns = {'Autumn20':'autumn20'}, inplace = True)
    #st.write(xyz.dtypes)
    st.dataframe(xyz)
    #st.line_chart(xyz)
    xyz.plot.line()
    st.pyplot()

pct_of_students = st.checkbox("Show Graph w.r.t the Percentage of Students")
if pct_of_students:
    xyz = df_num.transpose()
    #st.dataframe(xyz)
    #st.line_chart(xyz)
    xyz.plot.line()
    st.pyplot()

#df_plot = pd.DataFrame(df_new, columns = ['Ex', 'A', 'B', 'C', 'D', 'P', 'F'])
#st.bar_chart(df_new['Ex','A','B','C','D','F','P'])