import streamlit as st
from incident_response import load_scenario, check_actions

st.title("Incident Response Simulation Tool")

st.write("Welcome to the Incident Response Simulation Tool! Select a scenario to begin.")

scenario_id = st.selectbox("Select a scenario:", ["1", "2"])
scenario = load_scenario(scenario_id)

if scenario:
    st.subheader(scenario["title"])
    st.write(scenario["description"])

    actions = st.multiselect("Select your actions:", scenario["actions"])

    if st.button("Submit Actions"):
        correct_actions, incorrect_actions = check_actions(actions, scenario["correct_actions"])

        if correct_actions:
            st.success(f"Correct actions: {', '.join(correct_actions)}")
        if incorrect_actions:
            st.error(f"Incorrect actions: {', '.join(incorrect_actions)}")

        st.write("Feedback:")
        if len(incorrect_actions) > 0:
            st.write("Review the following actions to improve your response.")
        st.write("Good luck with your next scenario!")
