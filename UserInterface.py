import streamlit as st
import requests

st.set_page_config(page_title="Query System", page_icon=":guardsman:", layout="centered")
st.title("Database Query System")

st.markdown("Write your SQL query below:")

query = st.text_area("SQL Query", height=200, placeholder="SELECT * FROM sample;")

if st.button("Run"):
    if not query.strip():
        st.error("Please write a query.")
    else:
        try:
            response = requests.post("http://localhost:8000/get_query", json={"query": query})
            result = response.json()
            if response.status_code == 200:
                st.json(response.json())
                st.success(result["status"])
                st.dataframe(result["data"])
            else:
                st.error(response.json().get("detail", "Unknown Error!"))
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the server. Please ensure the server is running.")