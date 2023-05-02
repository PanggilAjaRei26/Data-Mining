import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open('tokobuka.sav', 'rb'))

df = pd.read_excel("dataset.xlsx")
df['YEAR'] = pd.to_datetime(df['YEAR'], format='%Y')
df.set_index(['YEAR'], inplace=True)

st.title('Prediksi Jumlah Toko')
year = st.slider("Tentukan Tahun",1,5, step=1)

pred = model.forecast(year)
pred = pd.DataFrame(pred, index=pd.date_range(start=df.index[-1], periods=year, freq='Y'), columns=['VALUE'])

if st.button("Prediksi"):
    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots()
        df['VALUE'].plot(style="--", color='gray', legend=True, label='known')
        pred['VALUE'].plot(color='b', legend=True, label='Prediction')
        st.pyplot(fig)