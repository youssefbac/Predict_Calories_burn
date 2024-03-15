import streamlit as st
import pickle as pk
import numpy as np
import pandas as pd

pipe=pk.load(open('pipeline.pkl','rb'))

st.image("icon.png", width=64)
#col1, col2 = st.columns([1,2])
#with col1:
#    st.image("icon.png", width=64)
#with col2:
st.title("Calories Burned Calculator")

gender=st.selectbox('Gender',['male','female'])
age= st.number_input('Age')
height=st.number_input('height')
weight=st.number_input('weight')
duration=st.number_input('Exercice Duration')
heart_rate=st.number_input('Heart Rate')
body_temp=st.number_input('Body temperature')

if st.button('Predict'):
    sample = pd.DataFrame({
        'Gender': [gender],
        'Age': [age],
        'Height': [height],
        'Weight':[weight],
        'Duration': [duration],
        'Heart_Rate': [heart_rate],
        'Body_Temp': [body_temp],
    }, index=[0])

    st.title("the predicted calories burnt is:"+ str( pipe.predict(sample)[0]))