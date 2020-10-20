import streamlit as st
import tzlocal
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if st.checkbox('checkbox'):
    st.image("foo.jpg")
    st.write("Welcome to the Quantum Physics 1 app")
#st.write(st.__version__)
    
#df = pd.DataFrame()
df = pd.read_csv("exam1stats.csv")
#st.write(df)
#st.write('exam scores actually')
#st.write(tzlocal.get_localzone())

st.title("Quantum Physics 1")

st.write("Exam 1 scores")

#file_obj = st.sidebar.file_uploader('Choose an image:', ('jpg', 'jpeg'))

num_bins = st.slider("Pick a number of bins", 5, 35, 20)

#st.write(value)
#input = st.text_input("Tell me something", "Cantami o Diva")
#with open("temp_file.txt", "r") as f:
#  st.write(f.read())
#st.write("Streamlit is fabulous")
#st.bar_chart(df['total'])

df['total'].hist(bins=num_bins)
plt.xlabel("score [%]")
plt.ylabel("count")
plt.show()
st.pyplot()
mean = np.mean(df['total'])
std = np.std(df['total'])

st.write('Mean score is', mean)
st.write("Standard deviation is", std)
#st.balloons()
#print("this is a log line")
