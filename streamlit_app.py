from snowflake.snowpark import Session

# Create Session object
connection_parameters = {
    user='CAMILOB',
    password='D@t@verse$$1',
    account='ABYLBQO-ZJ05545',
    warehouse='LEASE_WH',
    database='STREAMLIT_APPS',
    schema='WES_POC'
}

test_session = Session.builder.configs(connection_parameters).create()

ev_sales = test_session.sql(("select current_user()").collect()
ev_sales_df = ev_sales.to_pandas()
st.dataframe(ev_sales_df)
