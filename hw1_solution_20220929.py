# -*- coding: utf-8 -*-
"""HW1_solution_20220929.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Joy02vjqcyf_1z0xZ0qSJrNBUG2fvprg
"""

# https://docs.streamlit.io/library/cheatsheet
# streamlit run app.py
!pip install streamlit
import streamlit as st
import numpy as np
import joblib

# load model
clf2 = joblib.load('penguins.joblib')
scaler = joblib.load('scaler.joblib')

y_dict = {0:'Adelie', 1:'Chinstrap', 2:'Gentoo'}
island_dict = {'Torgersen':0, 'Biscoe':1, 'Dream':2}
sex_dict = {'Female':0, 'Male':1}

# 畫面設計
st.markdown('# 企鵝品種預測系統')
col1, col2 = st.columns(2)

with col1:
    island = st.selectbox('島嶼', island_dict.keys())
    bill_length = st.slider('嘴巴長度', 30, 60, 40)
    bill_depth = st.slider('嘴巴寬度', 10, 25, 15)
with col2:
    flipper_length = st.slider('翅膀長度', 170, 230, 200)
    body_mass = st.slider('體重', 2500, 6500, 4000)
    sex = st.radio('性別', sex_dict.keys())
    
if st.button('預測'):
    # predict
    X=np.array([[island_dict[island], bill_length, bill_depth, flipper_length,
                 body_mass, sex_dict[sex]]])
    X=scaler.transform(X)
    st.markdown(f'預測結果： **{y_dict[int(clf2.predict(X))]}**')

#網頁上傳到local web
!streamlit run classsification.py & npx localtunnel --port 8501