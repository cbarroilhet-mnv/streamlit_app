# Import python packages
import streamlit as st
import pandas as pd  # Add this import for handling the data
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import sum, col
import altair as alt
import snowflake.connector

st.set_page_config(layout="wide")

# Write directly to the app
st.title("Lease App in Python")
st.header("Add New Lease")
st.write(
    """Add new lease and, 
    press the button to run the month rent calculations
    """
)

# Create input fields for the columns in the LEASE_DETAIL table
LEASE_ID = st.text_input("Lease ID")
LEASE_NAME = st.text_input("Lease Name")
START_DATE = st.date_input("Start Date")
END_DATE = st.date_input("End Date")
INCREASE_DATE = st.date_input("Increase Date")
BASE_RENT = st.number_input("Base Rent")
BASE_PROMOTIONAL_FUND = st.number_input("Base Promotional Fund")
BASE_OTHER = st.number_input("Base Other")
BASE_OUTGOINGS = st.number_input("Base Outgoings")
MONTHLY_RENTAL_GROSS = st.number_input("Monthly Rental Gross")
REFERENCE_RATE = st.number_input("Reference Rate")
FINANCIAL_SPREAD_ADJ = st.number_input("Financial Spread Adj")
LEASE_SPECIFIC_ADJ = st.number_input("Lease Specific Adj")
ANNUAL_DISCOUNT_RATE = st.number_input("Annual Discount Rate")
MONTHLY_DISCOUNT_RATE = st.number_input("Monthly Discount Rate")
ROUA_LIFE = st.number_input("ROUA Life")
CPI_CHECK = st.checkbox("CPI Check")
ANNUAL_RENT_INCREASE = st.number_input("Annual Rent Increase")
STATUS = st.text_input("Status")
CPI = st.number_input("CPI")
CPI_SENSITIVE_ADJ = st.number_input("CPI Sensitive Adj")

 # Get the active Snowflake session
session = get_active_session()

# Initialize data
data = session.sql("SELECT * FROM STREAMLIT_APPS.LEASE_DB.LEASE_DETAIL").collect()

# Add a button to submit the form data
if st.button("Add Lease"):
    # Get the active Snowflake session
    session = get_active_session()   

    # Insert the entered data into the LEASE_DETAIL table
    sql = f"""
    INSERT INTO STREAMLIT_APPS.LEASE_DB.LEASE_DETAIL (
        LEASE_ID, 
        LEASE_NAME, 
        START_DATE, 
        END_DATE, 
        INCREASE_DATE, 
        BASE_RENT, 
        BASE_PROMOTIONAL_FUND, 
        BASE_OTHER, 
        BASE_OUTGOINGS, 
        MONTHLY_RENTAL_GROSS, 
        REFERENCE_RATE, 
        FINANCIAL_SPREAD_ADJ, 
        LEASE_SPECIFIC_ADJ, 
        ANNUAL_DISCOUNT_RATE, 
        MONTHLY_DISCOUNT_RATE, 
        ROUA_LIFE, 
        CPI_CHECK, 
        ANNUAL_RENT_INCREASE, 
        STATUS, 
        CPI, 
        CPI_SENSITIVE_ADJ
    ) 
    VALUES (
        '{LEASE_ID}',
        '{LEASE_NAME}',
        '{START_DATE}',
        '{END_DATE}',
        '{INCREASE_DATE}',
        {BASE_RENT},
        {BASE_PROMOTIONAL_FUND},
        {BASE_OTHER},
        {BASE_OUTGOINGS},
        {MONTHLY_RENTAL_GROSS},
        {REFERENCE_RATE},
        {FINANCIAL_SPREAD_ADJ},
        {LEASE_SPECIFIC_ADJ},
        {ANNUAL_DISCOUNT_RATE},
        {MONTHLY_DISCOUNT_RATE},
        {ROUA_LIFE},
        {CPI_CHECK},
        {ANNUAL_RENT_INCREASE},
        '{STATUS}',
        {CPI},
        {CPI_SENSITIVE_ADJ}
    )
    """

    try:
        
        _= session.sql(sql).collect()
        
        # Clear the input fields after successful insertion
        
        LEASE_ID = ""
        LEASE_NAME = ""
        START_DATE = None
        END_DATE = None
        INCREASE_DATE = None
        BASE_RENT = None
        BASE_PROMOTIONAL_FUND = None
        BASE_OTHER = None
        BASE_OUTGOINGS = None
        MONTHLY_RENTAL_GROSS = None
        REFERENCE_RATE = None
        FINANCIAL_SPREAD_ADJ = None
        LEASE_SPECIFIC_ADJ = None
        ANNUAL_DISCOUNT_RATE = None
        MONTHLY_DISCOUNT_RATE = None
        ROUA_LIFE = None
        CPI_CHECK = False
        ANNUAL_RENT_INCREASE = None
        STATUS = ""
        CPI = None
        CPI_SENSITIVE_ADJ = None
        # ... Clear other input fields ...
        
        st.success("Lease added successfully.")
        
        # Refresh the table by rerunning the query
        data = session.sql("SELECT * FROM STREAMLIT_APPS.LEASE_DB.LEASE_DETAIL").collect()
    except Exception as e:
        st.error(f"Error adding lease: {str(e)}")

# Display existing leases
st.write("Existing Leases:")
st.write(pd.DataFrame(data))



