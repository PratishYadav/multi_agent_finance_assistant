import streamlit as st
import requests
from voice.tts import speak

st.title("📈 Morning Market Brief")

if st.button("Get Brief"):
    result = requests.get("http://localhost:8000/brief").json()
    summary = result["summary"]
    st.write(summary)
    speak(summary)
