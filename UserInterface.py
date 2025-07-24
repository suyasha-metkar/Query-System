import streamlit as st      #Streamlit for web interface
import requests             #Requests for HTTP requests

st.set_page_config(page_title="Query System", page_icon=":guardsman:", layout="centered")       # Set up the page configuration
st.title("Database Query System")                                                               # Title of the web app

st.markdown("Write your SQL query below:")                                                      

query = st.text_area("SQL Query", height=200, placeholder="SELECT * FROM sample;")             # Text area for SQL query input

if st.button("Run"):                                                                           # Button to run the query
    if not query.strip():                                                                      # If the query is empty
        st.error("Please write a query.")                                               
    else:
        try:                                                                                   # Send the query to the FastAPI server
            response = requests.post("http://localhost:8000/get_query", json={"query": query}) 
            result = response.json()
            if response.status_code == 200:                                                   # If the response is successful
                st.json(response.json())
                st.success(result["status"])
                st.dataframe(result["data"])
            else:
                st.error(response.json().get("detail", "Unknown Error!"))                    # If the response is not successful calls the error message
        except requests.exceptions.ConnectionError:                                          # If there is a connection error
            st.error("Could not connect to the server. Please ensure the server is running.")