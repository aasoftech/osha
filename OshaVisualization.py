# Import required libraries
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# To ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Remove the limit from the number of displayed columns and rows. It helps to see the entire dataframe while printing it
pd.set_option("display.max_columns", None)

import pandas as pd
import plotly.express as px

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

fig.show()
