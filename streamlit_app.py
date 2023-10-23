import snowflake.connector
import pandas as pd
import streamlit as st

# Set up the connection to Snowflake
conn = snowflake.connector.connect(
    user='CAMILOB',
    password='D@t@verse$$1',
    account='qo61633.ap-southeast-2',
    warehouse='LEASE_WH',
    database='STREAMLIT_APPS',
    schema='WES_POC'
)

# # Create a cursor
# cursor = conn.cursor()

# def create_editable_income_df(selected_farm):
    # try:
    #     cursor.execute(f"""select T.ID, T.operation, D.INCOME_EXPENSE_CATEGORY, T.year, T.month, T.description, T.quantity, T.TYPE, T.cost, T.costunit, T.unitprice, T.priceunit, T.total from STREAMLIT_APPS.WES_POC.NEW_TRANSACTIONS AS T
    #                    inner join INCOME_EXPENSE_CATEGORY AS D ON T.EXPENSECATEGORY = D.YARDI_CODE
    #                     WHERE T.FARM = '{selected_farm}' AND D.COST_CATEGORY = 'Income'""")
    #     income_data = cursor.fetch_pandas_all()
    #     if income_data is not None:
    #         income_df = pd.DataFrame(income_data, columns=["Row id", "Operation", "Category", "Year", "Month", "Description", "Quantity", "Type", "Cost", "Cost Unit", "Unit Price", "Price Unit", "Total"])
    #         editable_income_df = income_df.copy()
    #     else:
    #         st.error("No data found for the selected farm.")
    #         editable_income_df = pd.DataFrame()  # Create an empty DataFrame
    # except Exception as e:
    #     st.error(f"An error occurred: {str(e)}")
    #     editable_income_df = pd.DataFrame()  # Create an empty DataFrame
    # return editable_income_df


# Call the function and store the result in a variable
# editable_income_df = create_editable_income_df("selected_farm")

# # Close the cursor and connection
# cursor.close()

cursor_2 = conn.cursor()
cursor_2.execute("select FARM from STREAMLIT_APPS.WES_POC.FARM")
distinct_farms_data = cursor_2.fetch_pandas_all()
existing_farms = [row[0] for row in distinct_farms_data]
cursor_2.close()

col1, col2, col3, col4 = st.columns([2.5,1.5,1.5,2.5])


# LEFT ONE: CROP PRODUCTION BY FARM# Add content to the first column ("Crop Production")
with col1:
    st.subheader("Crop Production")
    # Create four columns within this column
    crop_column, area_column, yield_column, tonnes_column = st.columns(4)
    # Create a DataFrame from the FARM table and filter based on selected farm
    selected_farm = "Farm 1"
    farm_df = conn.cursor()
    farm_df.execute("SELECT * FROM WES_POC.FARM")
    farm_df = farm_df.fetch_pandas_all()
    
    # Check if data is retrieved
if not farm_data.empty:
    crop = str(farm_data['CROP'][0])
    area = str(farm_data['HA'][0])
    yield_ = str(farm_data['YIELD'][0])
    tonnes = str(farm_data['TONNES'][0])

    with crop_column:
        st.markdown("Crop")
        st.info(crop)

    with area_column:
        st.write("Crop Area (Ha)")
        formatted_area = "{:,.0f}".format(float(area))
        st.info(formatted_area)

    with yield_column:
        st.write("Yield / Ha")
        formatted_yield = "{:,.0f}".format(float(yield_))
        st.info(formatted_yield)

    with tonnes_column:
        st.write("Tonnes|Bales")
        formatted_tonnes = "{:,.0f}".format(float(tonnes))
        st.info(formatted_tonnes)
else:
    st.warning("No data found for the selected farm.")
