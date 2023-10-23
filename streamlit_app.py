from snowflake.snowpark import Session
import streamlit as st

# Create Session object
connection_parameters = {
    'user': 'CAMILOB',
    'password': 'D@t@verse$$1',
    'account': 'ABYLBQO-ZJ05545',
    'warehouse': 'LEASE_WH',
    'database': 'STREAMLIT_APPS',
    'schema': 'WES_POC'
}

test_session = Session.builder.configs(connection_parameters).create()

# Execute the SQL query
ev_sales = test_session.execute("SELECT current_user()")

# Convert the result to a Pandas DataFrame
ev_sales_df = ev_sales.to_pandas()

# Display the DataFrame using Streamlit
st.dataframe(ev_sales_df)
