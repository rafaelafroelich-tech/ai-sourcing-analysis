
import streamlit as st, pandas as pd
df=pd.read_excel('data/mock_sourcing_dataset.xlsx')
st.title('AI-Powered Human-Centered Sourcing Analytics')
st.metric('Candidates',len(df))
st.metric('Hire Rate',f"{df['hired'].mean()*100:.2f}%")
st.write(df.groupby('source_channel')['hired'].mean().sort_values(ascending=False)*100)
