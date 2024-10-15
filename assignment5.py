import streamlit as st
import pandas as pd

# Title of the app
st.title('Store Performance Data Visualization App')

# New dataset for store sales and profit information
data = {
    'City GDP': ['Manila', 'Hong Kong','Tokyo','Uganda','Vientiene'],
    'Monthly Sales (Thousands USD)': [500, 600, 450, 700, 550],
    'Monthly Profit (Thousands USD)': [200, 250, 150, 300, 220],
    'Number of Employees': [50, 60, 45, 65, 55]
}

df = pd.DataFrame(data)

# Display the dataset
st.write("Store Performance Data:")
st.write(df)

# Let the user select columns for the chart
columns = df.columns.tolist()

# Dropdowns for X and Y axes selection
x_axis = st.selectbox('Select column for X-axis', columns)
y_axis = st.selectbox('Select column for Y-axis', columns)

# Choose chart type: Bar Chart or Line Chart
chart_type = st.selectbox('Select chart type', ['Bar Chart', 'Line Chart'])

# Display chart based on user selections
if chart_type == 'Bar Chart':
    st.bar_chart(df[[x_axis, y_axis]].set_index(x_axis))
elif chart_type == 'Line Chart':
    st.line_chart(df[[x_axis, y_axis]].set_index(x_axis))
