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
df2 = pd.read_csv("exam2stats.csv")
#st.write(df)

st.title("Quantum Physics 1")

st.write("Exam 1 scores")
#file_obj = st.sidebar.file_uploader('Choose an image:', ('jpg', 'jpeg'))
num_bins = st.slider("Pick a number of bins", 5, 35, 20,key='exam1')

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
st.pyplot(fig)
mean = np.mean(df['total'])
std = np.std(df['total'])

st.write('Mean score is', mean)
st.write("Standard deviation is", std)
st.write("==================================================")


st.write("Exam 2 scores")
num_bins2 = st.slider("Pick a number of bins", 5, 35, 20, key='exam2')

fig2 = plt.figure()
exam2_total = np.sum(df2, axis=1)

#st.write("total cal",exam2_total.shape)
#st.write(exam2_total)
df2['total'] = exam2_total

df2['total'].hist(bins=num_bins2)
plt.xlabel("score [%]")
plt.ylabel("count")
plt.show()
st.pyplot(fig2)
mean2 = np.mean(df2['total'])
std2 = np.std(df2['total'])

st.write('Mean score is', mean2)
st.write("Standard deviation is", std2)

#plt.subplot(4,2,1)
import plotly.graph_objects as go
from plotly.subplots import make_subplots


fig = make_subplots(
    rows=2, cols=2,
    #shared_xaxes=True,
    #vertical_spacing=0.03,
    #specs=[[{"type": "histogram"}],
    #       [{"type": "histogram"}],
    #       [{"type": "histogram"}],
    #       [{"type": "histogram"}]]
)

fig.add_trace(
    go.Histogram(
        x=df2["Q1"],
        nbinsx=num_bins2,
        name="Exam2_Q1"
    ),
    row=1, col=1
)

fig.add_trace(
    go.Histogram(
        x=df2["Q2"],
        nbinsx=num_bins2,
        name="Exam2_Q2"
    ),
    row=1, col=2
)

fig.add_trace(
    go.Histogram(
        x=df2["Q3"],
        nbinsx=num_bins2,
        name="Exam2_Q3"
    ),
    row=2, col=1
)

fig.add_trace(
    go.Histogram(
        x=df2["Q4"],
        nbinsx=num_bins2,
        name="Exam2_Q4"
    ),
    row=2, col=2
)



#fig.show()
#st.pyplot(fig)
st.plotly_chart(fig)

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
st.pyplot(fig)

