from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import avg, sum, col, lit
import streamlit as st
import pandas as pd
import snowflake.connector

# Create Session object
conn = snowflake.connector.connect(
    user='CAMILOB',
    password='D@t@verse$$1',
    account='ABYLBQO-ZJ05545',
    warehouse='LEASE_WH',
    database='STREAMLIT_APPS',
    schema='WES_POC'
)

# Create a cursor
cursor = conn.cursor()
cursor.execute("select current_user()")
current_user = cursor.fetch_pandas_all().iloc[0]
st.info(current_user)
