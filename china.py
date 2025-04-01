import streamlit as st
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="VCT China", layout="wide")
left_co, left_co2, cent_co,right_co, last_co = st.columns(5)
with cent_co:
    st.image("https://i.namu.wiki/i/41yyRkKsK1NPKvfS9j0CEF9wtsWTW-b-6RMgS2tEz1LqK48A4F0yF_wgOX5H19j5FvoZfpcqIP146X8ZjmzMhg.svg")

st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/f/fb/Valorant_Champions_Tour_logo.png", use_container_width=True)
st.sidebar.title("Divisions")
divisions = ["Americas", "EMEA", "Pacific", "China"]
for division in divisions:
    st.sidebar.page_link(f"pages/{division.lower()}.py", label=division)

colors = {
    "red": "#FF0000",
    "green": "#008000",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
    "orange": "#FFA500",
    "purple": "#800080",
    "pink": "#FFC0CB",
    "brown": "#A52A2A",
    "black": "#000000",
    "white": "#FFFFFF",
    "gray": "#808080",
    "cyan": "#00FFFF",
    "magenta": "#FF00FF",
    "lime": "#00FF00",
    "indigo": "#4B0082",
    "gold": "#FFD700",
    "navy": "#000435",
    "fpx": "#480808",
    "drg": "#72ceb2",
}

# Dictionary of VCT Americas teams with their rating and color
teams = {
    "EDG": {"rating": 9.5, "color": "blue"},
    "Trace Esports": {"rating": 7.0, "color": "white"},
    "Bilibili": {"rating": 9.0, "color": "cyan"},
    "DRG": {"rating": 8.8, "color": "drg"},
    "FPX": {"rating": 8.5, "color": "fpx"},
    "Nova": {"rating": 5.5, "color": "purple"},
    "JDG": {"rating": 6.5, "color": "red"},
    "Wolves": {"rating": 5.0, "color": "yellow"},
    "Titan": {"rating": 4.5, "color": "green"},
}

def calculate_win_probability(team1_rating, team2_rating):
    """Calculate win probability"""
    rating_diff = team1_rating - team2_rating
    probability = 1 / (1 + 10 ** (-rating_diff / 4))
    return probability

st.title("VCT China Head 2 Head Predictor")

# Create two columns for team selection
col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox("Select Team 1", list(teams.keys()), key="team1")
    st.write(f"Power Rating: {teams[team1]['rating']}")

with col2:
    team2 = st.selectbox("Select Team 2", list(teams.keys()), key="team2")
    st.write(f"Power Rating: {teams[team2]['rating']}")

if st.button("Calculate Matchup"):
    if team1 != team2:
        prob_team1 = calculate_win_probability(teams[team1]['rating'], teams[team2]['rating'])
        prob_team2 = 1 - prob_team1

        st.write("---")
        st.write("### Predicted Win Probabilities")
        
        # Create pie chart data
        values = [prob_team1, prob_team2]
        labels = [f"{team1}\n{prob_team1:.1%}", f"{team2}\n{prob_team2:.1%}"]
        colors_pie = [colors[teams[team1]['color']], colors[teams[team2]['color']]]
        
        # Create and display pie chart
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, colors=colors_pie, explode=(0.1, 0),
               autopct='%1.1f%%', startangle=90, 
               wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
        ax.axis('equal')
        st.pyplot(fig)
    else:
        st.error("Please select different teams to compare!")

