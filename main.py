import streamlit as st
import csv
import datetime
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
def show_form_page():
    st.write("Form Page")

    # Automatic inputs
    start_date = generate_start_date()

    st.write(f"Disaster Start Date: {start_date}")

    # Manual inputs
    disaster_group = st.selectbox("Disaster Group", ["Natural", "Man-made"])
    if disaster_group=="Natural":
        disaster_subgroup = st.selectbox("Disaster Subgroup", ["Geophysical", "Meteorological", "Hydrological", "Climatological", "Biological", "Technological"])
    else:
        disaster_subgroup=st.selectbox("Disaster Subgroup",["Human Conflicts"])
    if disaster_subgroup=="Geophysical":
        disaster_type = st.selectbox("Disaster Type",["Earthquake","Glacial lake outburst","Landslide"])
    elif disaster_subgroup=="Meteorological":
        disaster_type = st.selectbox("Disaster Type",["Strom","Extreme Temprature","Wildfire"])
    elif disaster_subgroup=="Hydrological":
        disaster_type = st.selectbox("Disaster Type",["Flood","Dam failure",])
    elif disaster_subgroup=="Climatological":
        disaster_type = st.selectbox("Disaster Type",["Drought"])
    elif disaster_subgroup=="Biological":
        disaster_type = st.selectbox("Disaster Type",["Epidemic","Insect infestation"])
    elif disaster_subgroup=="Human Conflicts":
        disaster_type=st.selectbox("Disaster Type",["Terrorism attacks","Civil unrest and riots","Mass shootings"])
    else:
        disaster_type = st.selectbox("Disaster Type", ["Industrial chemical spill","Gas pipeline rupture","Building collapse","Train derailment","Electrical grid failure"])

    disaster_subtype = st.text_input("Disaster Subtype", help="This field is mandatory")
    location = st.text_input("City")
    state = st.selectbox("State:",[
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
])
    glide = generate_glide(disaster_subgroup, disaster_type,state,start_date)
    st.write(f"Glide No.: {glide}")

    if st.button("Save"):
        save_to_csv(glide, start_date, disaster_group, disaster_subgroup, disaster_type, disaster_subtype, location, state)

def generate_glide(disaster_subgroup, disaster_type,state,start_date):
    glide=""
    glide=disaster_subgroup[0:3].upper()+"-"+disaster_type[0:3].upper()+"-"+state[0:3].upper()+"-"+start_date
    return glide

def generate_start_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_to_csv(glide, start_date, disaster_group, disaster_subgroup, disaster_type, disaster_subtype, location, state):
    with open('Cleaned_Dataset.csv', mode='a', newline='') as file:

        if '' in (disaster_group, disaster_subgroup, disaster_type, disaster_subtype, location):
            st.error("Please fill in all fields.")
        else:
            start_date1=datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
            year=start_date1.year
            month=start_date1.month
            day=start_date1.day
            time=start_date1.strftime("%H:%M:%S")
            writer = csv.writer(file)
            writer.writerow([glide, disaster_group, disaster_subgroup, disaster_type, disaster_subtype,"", location+state,"",0,"","","",time,year,month,day,0,0,0,0,0,0,0,0,0])
            st.success("Data saved successfully.")

#####################################################################################################################
def edit_form():
    st.title("Disaster Data Edit")
    if "Glide" not in st.session_state:
        st.session_state["Glide"] = ""
    Glide = st.text_input("Enter Glide Number:", st.session_state["Glide"])

    if st.button("Search"):
        st.session_state["Glide"] = Glide  # Update session state on search
        show_edit_form(Glide)
data = pd.read_csv("Cleaned_Dataset.csv")


def show_edit_form(Glide):
    data_to_edit = data[data["Glide"] == Glide]

    if data_to_edit.empty:
        st.error(f"Glide number '{Glide}' not found in the dataset.")
        return
    state = st.selectbox("State:",[
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
])
# Local Time,Start Year,Start Month,Start Day,End Year,End Month,End Day,Total Deaths,No Injured,No Affected,Total Affected,Insured Damages (000 US$),Total Damages (000 US$)
    disaster_group = st.selectbox("Disaster Group", ["Natural", "Man-made"])
    if disaster_group=="Natural":
        disaster_subgroup = st.selectbox("Disaster Subgroup", [data_to_edit["Disaster Subgroup"].iloc[0],"Geophysical", "Meteorological", "Hydrological", "Climatological", "Biological", "Technological"])
    else:
        disaster_subgroup=st.selectbox("Disaster Subgroup",[data_to_edit["Disaster Subgroup"].iloc[0],"Human Conflicts"])
    if disaster_subgroup=="Geophysical":
        disaster_type = st.selectbox("Disaster Type",[data_to_edit["Disaster Type"].iloc[0],"Earthquake","Glacial lake outburst","Landslide"])
    elif disaster_subgroup=="Meteorological":
        disaster_type = st.selectbox("Disaster Type",[data_to_edit["Disaster Type"].iloc[0],"Strom","Extreme Temprature","Wildfire"])
    elif disaster_subgroup=="Hydrological":
        disaster_type = st.selectbox("Disaster Type",[data_to_edit["Disaster Type"].iloc[0],"Flood","Dam failure",])
    elif disaster_subgroup=="Climatological":
        disaster_type = st.selectbox("Disaster Type",[data_to_edit["Disaster Type"].iloc[0],"Drought"])
    elif disaster_subgroup=="Biological":
        disaster_type = st.selectbox("Disaster Type",[data_to_edit["Disaster Type"].iloc[0],"Epidemic","Insect infestation"])
    elif disaster_subgroup=="Human Conflicts":
        disaster_type=st.selectbox("Disaster Type",[data_to_edit["Disaster Type"].iloc[0],"Terrorism attacks","Civil unrest and riots","Mass shootings"])
    else:
        disaster_type = st.selectbox("Disaster Type",[data_to_edit["Disaster Type"].iloc[0],"Industrial chemical spill","Gas pipeline rupture","Building collapse","Train derailment","Electrical grid failure"])
    disaster_subtype = st.text_input("Disaster Subtype", placeholder=data_to_edit["Disaster Subtype"].iloc[0])
    event_name = st.text_input("Event Name", placeholder=data_to_edit["Event Name"].iloc[0])
    location = st.text_input("Location", placeholder=data_to_edit["Location"].iloc[0])
    origin = st.text_input("Origin", placeholder=data_to_edit["Origin"].iloc[0])
    dis_mag_value = st.text_input("Dis Mag Value", placeholder=data_to_edit["Dis Mag Value"].iloc[0])
    dis_mag_scale = st.text_input("Dis Mag Scale", placeholder=data_to_edit["Dis Mag Scale"].iloc[0])
    latitude = st.text_input("Latitude", placeholder=data_to_edit["Latitude"].iloc[0])
    longitude = st.text_input("Longitude", placeholder=data_to_edit["Longitude"].iloc[0])
    total_deaths = st.number_input("Total Deaths", placeholder=data_to_edit["Total Deaths"].iloc[0])
    no_injured = st.number_input("No Injured", placeholder=data_to_edit["No Injured"].iloc[0])
    no_affected = st.number_input("No Affected", placeholder=data_to_edit["No Affected"].iloc[0])
    insured_damages = st.number_input("Insured Damages (000 US$)", placeholder=data_to_edit["Insured Damages (000 US$)"].iloc[0])
    total_damages = st.number_input("Total Damages (000 US$)", placeholder=data_to_edit["Total Damages (000 US$)"].iloc[0])
    if st.button("End Emergency"):
        end_date=generate_start_date
        year=end_date.year
        month=end_date.month
        day=end_date.day
        st.write(year+"-"+month+"-"+day)

    if st.button("Save Changes"):
        # Update data in the DataFrame
        data_to_edit.loc[:, "Disaster Group"] = disaster_group
        data_to_edit.loc[:, "Disaster Subgroup"] = disaster_subgroup
        data_to_edit.loc[:, "Disaster Type"] = disaster_type
        data_to_edit.loc[:, "Disaster Subtype"] = disaster_subtype
        data_to_edit.loc[:, "Event Name"] = event_name
        data_to_edit.loc[:, "Location"] = location
        data_to_edit.loc[:, "Origin"] = origin
        data_to_edit.loc[:, "Dis Mag Value"] = dis_mag_value
        data_to_edit.loc[:, "Dis Mag Salue"] = dis_mag_scale
        data_to_edit.loc[:, "Latitude"] = latitude
        data_to_edit.loc[:, "Longitude"] = longitude
        data_to_edit.loc[:, "Event Name"] = event_name
        data_to_edit.loc[:, "Location"] = location
        data_to_edit.loc[:, "Total Deaths"] = total_deaths
        data_to_edit.loc[:, "No Injured"] = no_injured
        data_to_edit.loc[:, "No Affected"] = no_affected
        data_to_edit.loc[:, "Total Affected"] =  no_injured+no_affected
        data_to_edit.loc[:, "Insured Damages (000 US$)"] = insured_damages
        data_to_edit.loc[:, "Total Damages (000 US$)"] = total_damages
        data_to_edit.loc[:, "End Year"] =  year
        data_to_edit.loc[:, "End Month"] = month
        data_to_edit.loc[:, "End Day"] = day 
        
        # Save updated DataFrame back to CSV
        data.to_csv("FIR1.csv", index=False)
        st.success("Data saved successfully!")

def generate_start_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
##################################################################################################################

st.set_page_config(page_title="Disaster Management Dashboard" ,page_icon=":tornado:",layout="wide")

st.title(":tornado: Disaster Management Dashboard")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)
df=pd.read_csv("Cleaned_Dataset.csv")
# Basic statistics
st.subheader("Basic Statistics")
st.write(df.describe())

# Visualizations
st.subheader("Visualizations")

# Bar chart for counting incidents by area
disaster_type_counts = df['Disaster Type'].value_counts()
fig = px.bar(disaster_type_counts, x=disaster_type_counts.index, y=disaster_type_counts.values,
             labels={'x': 'Disaster Type', 'y': 'Frequency'},
             title='Distribution of Different Types of Disasters')
fig.update_layout(xaxis={'categoryorder': 'total descending'})
st.plotly_chart(fig)

# Impact Analysis: Total deaths and total affected by disaster type

impact_fig = px.bar(df, x='Disaster Type', y=['Total Deaths', 'Total Affected'], 
                    title='Total Deaths and Total Affected by Disaster Type', barmode='group')
st.plotly_chart(impact_fig)


# Geospatial Analysis: Locations of disasters on a map 

map_fig = px.scatter_geo(df, lat='Latitude', lon='Longitude', hover_name='Location', color='Disaster Type',
                         title='Locations of Disasters in India', projection='equirectangular', center={'lat': 20, 'lon': 77})
st.plotly_chart(map_fig)

# Create Choropleth map
df_copy = df.copy()
damage_by_location = df_copy.groupby(['Latitude', 'Longitude'])['Total Damages (000 US$)'].sum().reset_index()
fig = px.scatter_geo(damage_by_location, lat='Latitude', lon='Longitude',
                     color='Total Damages (000 US$)', size='Total Damages (000 US$)',
                     projection="natural earth", title='Total Damage by Location',
                     hover_name='Total Damages (000 US$)')
fig.update_geos(showcountries=True, countrycolor="Black", showland=True, showcoastlines=True, coastlinecolor="Black")
st.plotly_chart(fig)

# Create a pie chart for each disaster type's subtype

# Group data by Disaster Type and Disaster Subtype
disaster_type_counts = df['Disaster Type'].value_counts()
disaster_type_fig = px.pie(values=disaster_type_counts, names=disaster_type_counts.index,
                           title='Distribution of Disaster Types')
st.plotly_chart(disaster_type_fig)
grouped_data = df.groupby(['Disaster Type', 'Disaster Subtype']).size().reset_index(name='count')
for disaster_type in grouped_data['Disaster Type'].unique():
    filtered_data = grouped_data[grouped_data['Disaster Type'] == disaster_type]
    fig = px.pie(filtered_data, values='count', names='Disaster Subtype',
                 title=f'Distribution of Subtypes for {disaster_type}')
    st.plotly_chart(fig)



# Preprocess the data for box plots
box_data = pd.DataFrame({
    'Category': ['Total Damage'] * len(df) + ['Insured Damage'] * len(df),
    'Value': list(df['Total Damages (000 US$)']) + list(df['Insured Damages (000 US$)'])
})

fig = px.box(box_data, x='Category', y='Value', 
             title='Distribution of Total Damage and Insured Damage')
fig.update_layout(yaxis_title='Damage (\'000 US$)', xaxis_title='')
st.plotly_chart(fig)

df_copy = df.copy()

# Convert relevant columns to datetime in the copied DataFrame
df_copy['Start Year'] = pd.to_datetime(df_copy['Start Year'], format='%Y', errors='coerce')
df_copy['End Year'] = pd.to_datetime(df_copy['End Year'], format='%Y', errors='coerce')

# Extract year from the datetime objects
df_copy['Start Year'] = df_copy['Start Year'].dt.year
df_copy['End Year'] = df_copy['End Year'].dt.year

# Group data by year and calculate total deaths
time_series_data = df_copy.groupby(['Start Year', 'End Year'])['Total Deaths'].sum().reset_index()

# Create line chart of total deaths with time

line_fig = px.line(time_series_data, x='Start Year', y='Total Deaths', 
                   title='Total Deaths Over Time')
line_fig.update_xaxes(title='Year')
line_fig.update_yaxes(title='Total Deaths')
st.plotly_chart(line_fig)

# Scatter plot for Total Damage vs. Magnitude Value
scatter_fig = px.scatter(df, x='Dis Mag Value', y='Total Damages (000 US$)',
                         title='Total Damage vs. Magnitude Value',
                         labels={'Dis Mag Value': 'Magnitude Value', 'Total Damages (000 US$)': 'Total Damage'})
scatter_fig.update_traces(marker=dict(size=8, opacity=0.8))  # Update marker size and opacity
scatter_fig.update_layout(showlegend=False)  # Hide legend
st.plotly_chart(scatter_fig)

df_copy = df.copy()

# Aggregate total damage by magnitude scale
damage_by_scale = df_copy.groupby('Dis Mag Scale')['Total Damages (000 US$)'].sum().reset_index()

# Copying the DataFrame to keep the original intact


# Aggregate total damage by latitude and longitude




parallel_fig = px.parallel_coordinates(df, color='Total Deaths',
                                       dimensions=['Dis Mag Value', 'Total Deaths', 
                                                   'Total Affected', 'Total Damages (000 US$)'],
                                       title='Parallel Coordinates Plot of Disaster Attributes')
st.plotly_chart(parallel_fig)


violin_fig = px.violin(df, x='Disaster Type', y='Dis Mag Value',
                       title='Violin Plot of Disaster Magnitude by Disaster Type',
                       labels={'Disaster Type': 'Disaster Type', 'Dis Mag Value': 'Magnitude Value'},
                       box=True, points='all')
violin_fig.update_layout(xaxis_title='Disaster Type', yaxis_title='Magnitude Value')
st.plotly_chart(violin_fig)

fig = px.line(df, x='Start Year', y=['Insured Damages (000 US$)', 'Total Damages (000 US$)'],
              labels={'value': 'Damages (000 US$)', 'Start Year': 'Year'},
              title='Trend of Insured Damages and Total Damages Over Time',
              color_discrete_sequence=['#1f77b4', '#ff7f0e'])  # Custom color palette
st.plotly_chart(fig)

# Create a new column combining start and end years
df['Year'] = df.apply(lambda row: pd.date_range(start=str(row['Start Year']), end=str(row['End Year']), freq='Y'), axis=1)

# Explode the 'Year' column to have one row per year
df = df.explode('Year')

# Group by year and disaster type and sum total affected
affected_over_time = df.groupby(['Year', 'Disaster Type'])['Total Affected'].sum().reset_index()

# Create the stacked area chart using Plotly
fig = px.area(affected_over_time, x='Year', y='Total Affected', color='Disaster Type',
              labels={'Total Affected': 'Total Affected Individuals', 'Year': 'Year'},
              title='Total Affected Individuals by Disaster Type Over Time')
st.plotly_chart(fig)

# Selecting relevant columns for correlation analysis
relevant_columns = ['Total Deaths', 'No Injured', 'No Affected', 'Total Affected', 
                    'Insured Damages (000 US$)', 'Total Damages (000 US$)']

# Calculate correlation matrix
correlation_matrix = df[relevant_columns].corr()

# Creating the heatmap using Plotly
fig = px.imshow(correlation_matrix,
                labels=dict(x="Attributes", y="Attributes", color="Correlation"),
                x=relevant_columns,
                y=relevant_columns,
                title="Correlation Heatmap")
st.plotly_chart(fig)
if st.button("New Form"):
    show_form_page()
if st.button("Edit Forms"):
    edit_form()
        



