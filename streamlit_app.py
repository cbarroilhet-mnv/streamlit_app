import streamlit as st
import bokeh.models
from bokeh.models import ColumnDataSource
from bokeh.models import CustomJS
from bokeh.models import DataTable
from bokeh.models import TableColumn
from bokeh.models import HTMLTemplateFormatter
from streamlit_bokeh_events import streamlit_bokeh_events
import pandas as pd

# Sample data
data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [30, 25, 35],
    "Action": ["Click", "Click", "Click"]
}

df = pd.DataFrame(data)

# Create a Bokeh DataTable
source = ColumnDataSource(df)
template = """
<a href="#" onclick="bokeh_streamlit_events.emit({event_name: 'cell_click', data: {index: source['index']}});">Click</a>
"""

formatter = HTMLTemplateFormatter(template=template)
columns = [
    TableColumn(field="Name", title="Name"),
    TableColumn(field="Age", title="Age"),
    TableColumn(field="Action", title="Action", formatter=formatter)
]

table = DataTable(source=source, columns=columns, width=400, height=150)

# Streamlit app
st.title("Clickable DataTable with Bokeh")

# Display the DataTable
st.bokeh_chart(table)

# Handle the click event using streamlit_bokeh_events
click_event = streamlit_bokeh_events(table, events="cell_click")

if click_event:
    st.write(f"Clicked row {click_event['index']}")
