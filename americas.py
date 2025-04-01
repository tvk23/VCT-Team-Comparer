import streamlit as st
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="VCT Americas", layout="wide")

left_co, left_co2, cent_co,right_co, last_co = st.columns(5)
with cent_co:
    st.image("https://i.namu.wiki/i/bvEj_JwMmqs4VoPrpaP3GoChb2XDOmLoN_0PU7CHYoquAzl3x29M8s5y2LUGVOiz3ZV233OxpZcukrlK_wEm9A.webp")

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
    "navy": "#000435"
}

# Dictionary of VCT Americas teams with their rating and color
teams = {
    "LOUD": {"rating": 9.5, "color": "green"},
    "Evil Geniuses": {"rating": 9.2, "color": "white"},
    "NRG": {"rating": 9.0, "color": "orange"},
    "Sentinels": {"rating": 8.8, "color": "red"},
    "100 Thieves": {"rating": 8.7, "color": "gray"},
    "Cloud9": {"rating": 8.6, "color": "cyan"},
    "FURIA": {"rating": 8.5, "color": "indigo"},
    "KRÜ Esports": {"rating": 8.4, "color": "purple"},
    "MIBR": {"rating": 8.3, "color": "brown"},
    "Leviatán": {"rating": 8.2, "color": "navy"},
}

def calculate_win_probability(team1_rating, team2_rating):
    """Calculate win probability using Elo-like formula"""
    rating_diff = team1_rating - team2_rating
    probability = 1 / (1 + 10 ** (-rating_diff / 4))
    return probability

st.title("VCT Americas Head 2 Head Predictor")

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
