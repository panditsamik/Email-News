import requests
import streamlit as st

API_KEY = "cEC9PeTgwwBnhyoeLsARN3qXhvIK5Cidm97ykxZi"
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

request = requests.get(url)
dict = request.json()

st.title(dict["title"])
st.image(dict["url"])
st.write(dict["explanation"])
st.write(f"[Link]({dict['hdurl']})")


