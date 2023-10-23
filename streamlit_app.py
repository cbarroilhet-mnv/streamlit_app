from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import avg, sum, col, lit
import streamlit as st
import pandas as pd

# Create Session object
def create_session_object():
   connection_parameters = {
      "account": "ABYLBQO-ZJ05545",
      "user": "CAMILOB",
      "password": "D@t@verse$$1",
      "role": "ACCOUNTADMIN",
      "warehouse": "LEASE_WH",
      "database": "STREAMLIT_APPS",
      "schema": "WES_POC"
   }
   session = Session.builder.configs(connection_parameters).create()
   user = session.sql('select current_user()').collect()

   # Use Streamlit to display the current user
   st.write("Current User:", user[0][0])

    # Call the function to create the Snowflake session and display the current user
create_session_object()
