# Import required libraries
import pandas as pd
import plotly.express as px
import streamlit as st

# Title for the Streamlit app
st.title('OSHA Inspection Data Visualization')

# Hardcoded values for company names and number of inspections
data = {
    'Company Name': ["Company 1", "Company 2", "Company 3", "Company 4"],
    'Number of Inspections': [310, 240, 160, 90]
}

# Create a DataFrame from the hardcoded values
top_companies = pd.DataFrame(data)

# Plot the results using Plotly
fig = px.bar(top_companies, x='Company Name', y='Number of Inspections',
             title='Companies with Most "Inspection Type = Accident"',
             labels={'Company Name': 'Company Name', 'Number of Inspections': 'Number of Inspections of Type "Accident"'},
             hover_data={'Number of Inspections': True})

# Customize the layout
fig.update_layout(
    xaxis_tickangle=-90,
    yaxis_title='Number of Inspections of Type "Accident"',
    xaxis_title='Company Name',
    yaxis=dict(range=[0, 500], tickvals=[0, 100, 200, 300, 400, 500]),
    height=600  # Adjust height to fit the data
)

# Display the plot in the Streamlit app
st.plotly_chart(fig)
