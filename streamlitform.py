import streamlit as st
import csv
import datetime
        
def show_form_page():
    st.write("Form Page")

    # Automatic inputs
    start_date = generate_start_date()

    st.write(f"Disaster Start Date: {start_date}")

    # Manual inputs
    caller_name = st.text_input("Caller Name:")
    caller_num = st.text_input("Caller Number:")
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
    house_id = st.text_input("House ID:")
    society = st.text_input("Society:")
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
    medical_help = st.radio("Medical help needed?", ("Yes", "No"))
    victim = st.selectbox("Victim:",["Self", "Known", "Unknown"])
    glide = generate_glide(disaster_subgroup, disaster_type,state,start_date)
    st.write(f"Glide No.: {glide}")

    if st.button("Save"):
        save_to_csv(glide, start_date, disaster_group, disaster_subgroup, disaster_type, disaster_subtype, location, caller_name, caller_num, house_id, society, state, victim, medical_help)

def generate_glide(disaster_subgroup, disaster_type,state,start_date):
    glide=""
    glide=disaster_subgroup[0:3].upper()+"-"+disaster_type[0:3].upper()+"-"+state[0:3].upper()+"-"+start_date
    return glide

def generate_start_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_to_csv(glide, start_date, disaster_group, disaster_subgroup, disaster_type, disaster_subtype, location, caller_name, caller_num, house_id, society, state, victim, medical_help):
    with open('FIR1.csv', mode='a', newline='') as file:

        if '' in (disaster_group, disaster_subgroup, disaster_type, disaster_subtype, location):
            st.error("Please fill in all fields.")
        else:
            writer = csv.writer(file)
            writer.writerow([glide, start_date, disaster_group, disaster_subgroup, disaster_type, disaster_subtype, location, caller_name, caller_num, house_id, society, state, victim, medical_help])
            st.success("Data saved successfully.")

st.title("Disaster Management system")
show_form_page()
# username = st.text_input("Username:")
# password = st.text_input("Password:", type="password")
# if st.button("Login"):
#     login(username, password)
