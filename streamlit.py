from scraper import bridges
import streamlit as st

st.title('Severn Bridges checker')
st.write(f'M4: {bridges.m4}')
st.write(f'M48: {bridges.m48}')
st.write(f'Time of check: {bridges.timestamp}')