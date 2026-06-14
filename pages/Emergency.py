import streamlit as st

st.set_page_config(page_title="Emergency Assistance", page_icon="🚨")

# Styling
st.markdown("""
<style>

.stButton button {
    background: linear-gradient(90deg,#DC2626,#EF4444);
    color: white;
    border-radius: 12px;
    border: none;
    height: 50px;
    font-size: 16px;
    font-weight: bold;
    width: 100%;
}

</style>
""", unsafe_allow_html=True)

st.title("🚨 Emergency Assistance")

st.warning(
    "Use this section only for urgent situations requiring immediate community support."
)

# Emergency Type
emergency_type = st.selectbox(
    "🚨 Emergency Type",
    [
        "Medical Emergency",
        "Blood Donation",
        "Vehicle Breakdown",
        "Safety Concern",
        "Pet Emergency",
        "Other"
    ]
)

# Hyderabad Areas & Locations
locations = {

    "Habsiguda": [
        "Habsiguda Metro Station",
        "NGRI",
        "Osmania University Gate",
        "CCPL Mall",
        "More Supermarket",
        "Street No 8",
        "Other"
    ],

    "Uppal": [
        "Uppal Metro Station",
        "Uppal Bus Depot",
        "Rajiv Gandhi Stadium",
        "Asian Mall",
        "Survey of India",
        "Other"
    ],

    "Tarnaka": [
        "Tarnaka Metro Station",
        "OU Main Gate",
        "St Ann's College",
        "Tarnaka Cross Roads",
        "Other"
    ],

    "Mallapur": [
        "Mallapur X Road",
        "Shakti Sai Nagar",
        "Mallapur Industrial Area",
        "Mallapur Bus Stop",
        "Other"
    ],

    "Nacharam": [
        "Nacharam Mall",
        "HMT Nagar",
        "Ramanthapur Road",
        "Nacharam Bus Stop",
        "Other"
    ],

    "Boduppal": [
        "Boduppal Kaman",
        "Boduppal Main Road",
        "Ambedkar Nagar",
        "Other"
    ],

    "LB Nagar": [
        "LB Nagar Metro Station",
        "LB Nagar Junction",
        "Kamineni Hospital",
        "Other"
    ],

    "Dilsukhnagar": [
        "Dilsukhnagar Metro",
        "Konark Theatre",
        "Chaitanyapuri",
        "Other"
    ],

    "Ameerpet": [
        "Ameerpet Metro",
        "Satyam Theatre",
        "Punjagutta Road",
        "Other"
    ],

    "Kukatpally": [
        "KPHB",
        "Forum Mall",
        "JNTU",
        "Other"
    ],

    "Madhapur": [
        "Madhapur Police Station",
        "Inorbit Mall",
        "Cyber Towers",
        "Other"
    ],

    "Hitech City": [
        "Cyber Towers",
        "Mindspace",
        "Google Office",
        "Other"
    ],

    "Gachibowli": [
        "Gachibowli Stadium",
        "DLF",
        "Financial District",
        "Other"
    ],

    "Banjara Hills": [
        "Road No 1",
        "Road No 12",
        "GVK Mall",
        "Other"
    ],

    "Himayat Nagar": [
        "Liberty Circle",
        "Minerva Coffee Shop",
        "St Paul's School",
        "Other"
    ]
}

st.subheader("📍 Location Details")

area = st.selectbox(
    "Select Area",
    list(locations.keys())
)

exact_location = st.selectbox(
    "Select Exact Location",
    locations[area]
)

custom_location = ""

if exact_location == "Other":
    custom_location = st.text_input(
        "✏️ Enter Exact Location",
        placeholder="Example: ABC Hotel, Street No 4"
    )

description = st.text_area(
    "📝 Describe the Emergency",
    placeholder="Provide details of the emergency..."
)

radius = st.slider(
    "📏 Alert Radius (KM)",
    min_value=1,
    max_value=5,
    value=3
)

if st.button("🚨 SEND EMERGENCY ALERT"):

    st.error("Emergency Alert Sent Successfully!")

    st.markdown("### Emergency Summary")

    st.write("🚨 Emergency Type:", emergency_type)

    st.write("📍 Area:", area)

    if exact_location == "Other":
        st.write("📌 Exact Location:", custom_location)
    else:
        st.write("📌 Exact Location:", exact_location)

    st.write("📏 Alert Radius:", radius, "KM")

    st.write("📝 Description:", description)