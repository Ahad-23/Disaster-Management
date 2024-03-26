import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Disaster Management Dashboard" ,page_icon=":tornado:",layout="wide")

st.title(":tornado: Disaster Management Dashboard")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)
data=pd.read_csv("")
# Basic statistics
st.subheader("Basic Statistics")
st.write(data.describe())

# Visualizations
st.subheader("Visualizations")

# Bar chart for counting incidents by area
area_counts = data['area'].value_counts()
area_fig = px.bar(area_counts, x=area_counts.index, y=area_counts.values, labels={'x':'Area', 'y':'Number of Incidents'}, title='Incidents by Area')
st.plotly_chart(area_fig, use_container_width=True)

# Pie chart for medical help requests
medical_help_counts = data['medical_help'].value_counts()
medical_help_fig = px.pie(medical_help_counts, values=medical_help_counts.values, names=medical_help_counts.index, title='Medical Help Requests')
st.plotly_chart(medical_help_fig, use_container_width=True)

# Pie chart for types of incidents
incident_counts = data['incident_type'].value_counts()
incident_fig = px.pie(incident_counts, values=incident_counts.values, names=incident_counts.index, title='Types of Incidents')
st.plotly_chart(incident_fig, use_container_width=True)

# Line chart for incidents over time
data['date'] = pd.to_datetime(data['date'])  # Assuming you have a 'date' column in your dataset
incidents_over_time = data.resample('M', on='date').size()
incidents_over_time_fig = px.line(x=incidents_over_time.index, y=incidents_over_time.values, labels={'x':'Date', 'y':'Number of Incidents'}, title='Incidents Over Time')
st.plotly_chart(incidents_over_time_fig, use_container_width=True)

# Stacked bar chart for incidents by area and incident type
area_incident_counts = data.groupby(['area', 'incident_type']).size().unstack(fill_value=0)
area_incident_fig = px.bar(area_incident_counts, barmode='stack', title='Incidents by Area and Type')
st.plotly_chart(area_incident_fig, use_container_width=True)

# Scatter plot for incidents by caller number and medical help requested
scatter_fig = px.scatter(data, x='caller_num', y='medical_help', color='medical_help', title='Incidents by Caller Number and Medical Help')
st.plotly_chart(scatter_fig, use_container_width=True)


