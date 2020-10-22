import streamlit as st
import tzlocal
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
#matplotlib.use('TKAgg',warn=False, force=True)
#import tkinter

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

fig = plt.figure()
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


st.write("==================================================")
st.write("Finite square well")

V0 = st.slider("Choose your well potential:", 0, 100, 30)

fig = plt.figure()
x = np.arange(0,np.pi*3,0.01)
x = list(x) #plt.plot() DOES NOT like np.arange for some reason
#V0 = 1
x0 = np.sqrt(V0)
y = np.tan(x); y=list(y)
y2 = np.sqrt(np.power(x0,2) - np.power(x,2))/x
y2 = list(y2)
plt.plot(x,y,c='blue',linewidth=2,linestyle='dashed')
plt.plot(x,y2,c='orange')
plt.ylim(0,50)
plt.xlabel("$xi$")
plt.ylabel("tan($xi$),($xi_0^2$-$xi^2$)$^{0.5}$/$xi$")
plt.show()
st.pyplot()

