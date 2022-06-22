import streamlit as st
from introduction import aforo_introduction
from derivatives_and_gradients import aforo_derivatives_and_gradients

st.set_page_config(layout="wide")

_, center, _ = st.columns([2, 2, 2])
with center:
    st.title("Algorithms for Optimization - Python Notes")

_, _, _, right = st.columns([2, 2, 1, 1])
with right:
    chapter = st.selectbox("Chapter", [f"Chapter - {i}" for i in range(1, 22)])

table_of_contents = {
    "Chapter - 1": aforo_introduction,
    "Chapter - 2": aforo_derivatives_and_gradients,
}

table_of_contents.get(chapter, aforo_introduction).run()
