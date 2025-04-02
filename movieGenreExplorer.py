import streamlit as st
import pandas as pd

st.title("Movie Genre Explorer")

df = pd.read_csv("cleaned_movies.csv")

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.dataframe(df, use_container_width=True)

st.write("You selected:", option)