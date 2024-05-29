import streamlit as st
import requests
import json

st.title("Player Value Prediction App ⚽")
leagues = [
        "Premier League and Championship", "EFL", "Bundesliga",
        "La liga","Serie A","Serie B",
        "Ligue 1","Eredivisie","Eerste Divisie",
        "Liga NOS","Premier Liga","Super Lig",
        "TFF","Bundesliga","Brasileiro",
        "MLS","Primera División","Liga MX",
        "DStv","J-League","Saudi Pro League",
        "K-League","A-League"
    ]

# Taking user inputs
appearance = st.slider("Appearance", 0, 300, 10)
minutes_played = st.slider("Minutes Played", 0, 10000, 500)
award = st.selectbox('Award', range(0,93))
goals = st.number_input("Insert a goals", value=None, placeholder="Type a number...")
assists = st.number_input("Insert a assists", value=None, placeholder="Type a number...")
days_injured = st.number_input("Insert a days_injured", value=None, placeholder="Type a number...")
games_injured = st.number_input("Insert a games_injured", value=None, placeholder="Type a number...")
highest_value = st.number_input("Insert a highest_value", value=None, placeholder="Type a number...")

league = st.selectbox(
   "Choose player league",
   leagues,
   index=None,
   placeholder="choose player league...",
)


# Converting the inputs into a JSON format
inputs = {
    "league": league,
    "appearance": appearance,
    "goals": goals,
    "assists": assists,
    "minutes_played": minutes_played, 
    "days_injured": days_injured,
    "games_injured": games_injured,
    "award": award,
    "highest_value": highest_value,
    }

# When the user clicks on the button, it will fetch the API
if st.button('Get Prediction'):
    try:
        res = requests.post(
            url="http://127.0.0.1:8000/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(inputs)
        )
        res.raise_for_status()  # Check for HTTP request errors
        st.subheader(f"Prediction result 🚀 = {res.json()}")

    except requests.exceptions.RequestException as e:
        st.error(f"HTTP Request failed: {e}")
    except ValueError as e:
        st.error(f"Failed to parse JSON response: {e}")