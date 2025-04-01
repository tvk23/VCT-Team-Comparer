from numpy import True_
import streamlit as st

# Set page config
st.set_page_config(
    page_title="VCT Head 2 Head Predictor",
    layout="wide"
)

# Main title and description
st.title("Welcome to the VCT Head 2 Head Predictor")
st.write("Click on one of the divisions in the Sidebar to get started!")

st.image("https://cdn.thespike.gg/Franchise%2520Teams%2FSEN_tenz_1677519139321.png")
st.caption("(Also say hello to my GOAT TenZ)")
#Create sidebar with division options

st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/f/fb/Valorant_Champions_Tour_logo.png", use_container_width=True)
st.sidebar.title("Divisions")
divisions = ["Americas", "EMEA", "Pacific", "China"]
for division in divisions:
    st.sidebar.page_link(f"pages/{division.lower()}.py", label=division)