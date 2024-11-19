# Save this as 'football_stats_app.py' and run with Streamlit.
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import subprocess


process = subprocess.Popen([
    "streamlit", "run", "alt1-file.py",
    "--server.port", "769",
    "--server.headless", "true"
])

# Load the CSV file
file_path = 'Alt1_exG_DataBase(in).csv'
data = pd.read_csv(file_path)

# Set up Streamlit layout
st.title("Football Statistics Information System")
st.write("Select a club and a statistic to display relevant football statistics graphically.")

# Dropdown options
teams = sorted(data['Team'].unique())  # List of unique teams for dropdown
statistics = ['Most Goals', 'Most Expected Goals', 'Biggest Difference']  # Statistic options

# Dropdowns for club and statistic selection
selected_team = st.selectbox("Select Club:", teams)
selected_stat = st.selectbox("Select Statistic:", statistics)

# Filter the data based on the selected team
team_data = data[data['Team'] == selected_team]

# Display the relevant statistic based on selection
if selected_stat == 'Most Goals':
    # Find the player with most goals
    top_player = team_data.loc[team_data['Actual Goals'].idxmax()]
    st.subheader("Most Goals")
    st.write(f"Player: {top_player['Player']} - Goals: {top_player['Actual Goals']}")

    # Bar chart for actual goals of all players in the selected team
    plt.figure(figsize=(10, 6))
    plt.bar(team_data['Player'], team_data['Actual Goals'], color='skyblue')
    plt.title("Actual Goals by Player")
    plt.xlabel("Player")
    plt.ylabel("Actual Goals")
    plt.xticks(rotation=45)
    st.pyplot(plt)  # Display the plot

elif selected_stat == 'Most Expected Goals':
    # Find the player with most expected goals
    top_player = team_data.loc[team_data['Expected Goals (xG)'].idxmax()]
    st.subheader("Most Expected Goals")
    st.write(f"Player: {top_player['Player']} - Expected Goals: {top_player['Expected Goals (xG)']}")

    # Bar chart for expected goals of all players in the selected team
    plt.figure(figsize=(10, 6))
    plt.bar(team_data['Player'], team_data['Expected Goals (xG)'], color='lightgreen')
    plt.title("Expected Goals by Player")
    plt.xlabel("Player")
    plt.ylabel("Expected Goals (xG)")
    plt.xticks(rotation=45)
    st.pyplot(plt)  # Display the plot

elif selected_stat == 'Biggest Difference':
    # Find the player with the biggest absolute goal difference
    team_data['Abs Difference'] = team_data['Goal difference'].abs()
    top_player = team_data.loc[team_data['Abs Difference'].idxmax()]
    st.subheader("Biggest Difference in Goals")
    st.write(f"Player: {top_player['Player']} - Goal Difference: {top_player['Goal difference']}")

    # Bar chart for goal differences of all players in the selected team
    plt.figure(figsize=(10, 6))
    plt.bar(team_data['Player'], team_data['Goal difference'], color='salmon')
    plt.title("Goal Difference by Player")
    plt.xlabel("Player")
    plt.ylabel("Goal Difference")
    plt.xticks(rotation=45)
    st.pyplot(plt)  # Display the plot
