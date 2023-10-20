import streamlit as st
import snowflake.snowpark as snowpark
import pandas as pd  # Import pandas for creating the DataFrame
from snowflake.snowpark.functions import current_user
from datetime import date


conn = connect(
    user='CAMILOB',
    password='D@t@verse$$1',
    account='ABYLBQO.ZJ05545.snowflakecomputing.com',
    warehouse='LEASE_WH',
    database='STREAMLIT_APPS',
    schema='WES_POC',
    role='ACCOUNTADMIN',
    cursor_class=DictCursor
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM NEW_TRANSACTIONS)
data = cursor.fetchall()

st.write(pd.DataFrame(data))
