import streamlit as st
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import DataTable, TableColumn
from streamlit_bokeh_events import streamlit_bokeh_events

# Create a Streamlit app
st.title("Interactive Data Visualization with Streamlit and Bokeh")

# Your app code here
# Create a Bokeh plot
p = figure(width=400, height=400)
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5])
st.bokeh_chart(p)
def on_button_click(event):
    st.write("Button Clicked!")

button = st.button("Click Me")
streamlit_bokeh_events(
    bokeh_plot=p,
    events="ButtonClick",
    key="my_event",
    on_event=on_button_click
)
