import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="My first page",
    layout="wide",
    initial_sidebar_state="expanded")
st.write("HELLOOOOOOOOO")
st.markdown("items")
data = {
    "name":["amma","nanna","nenu","puppy"],
    "age":[20,34,13,2],
    "hobbies":["watching tv","phone","coding","eating"],
    "born":[1982,1972,2007,2020]
}
df=pd.DataFrame(data)
st.table(df)
