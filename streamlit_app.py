# Import python packages
import streamlit as st
import pandas as pd  # Add this import for handling the data
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import sum, col
import altair as alt

st.set_page_config(layout="wide")

# Write directly to the app
st.title("Lease App in Python")
st.header("Add New Lease")
st.write(
    """Add new lease and, 
    press the button to run the month rent calculations
    """
)

# Get the current credentials
session = get_active_session()


sql = f"select * from STREAMLIT_APPS.LEASE_DB.LEASE_DETAIL"


data = session.sql(sql).collect()

# Display the data in a table
st.write("Leases:")
st.write(pd.DataFrame(data))
