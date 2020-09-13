import streamlit as st
import tzlocal
import pandas as pd

if st.checkbox('checkbox'):
    st.image("foo.jpg")

st.write(st.__version__)
    
df = pd.DataFrame({'ts': ['2020-04-14 01:00:00']})
df['ts2'] = pd.to_datetime(df['ts'])
st.write(df)
st.write('ts2 is actually:', df.loc[0, 'ts2'])
st.write(tzlocal.get_localzone())

st.title("Test App!!!")

st.write("don't mess with the best")

file_obj = st.sidebar.file_uploader('Choose an image:', ('jpg', 'jpeg'))

value = st.slider("Pick a number", 0, 10, 3)

st.write(value)

input = st.text_input("Tell me something", "Cantami o Diva")

with open("temp_file.txt", "a") as f:
  f.write(f"{input}\n")
  
with open("temp_file.txt", "r") as f:
  st.write(f.read())

st.write("Streamlit is fabulous")

st.write("Hello Corey, this is the demo!")
st.balloons()
print("this is a log line")
