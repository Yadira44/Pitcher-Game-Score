# GSC code
# calculate game score for a pitcher using updated Tom Tango version

# start the game

import streamlit as st

# Streamlit app title
st.title("Pitcher Game Score Calculator")

# Input fields using Streamlit
pitcher_name = st.text_input("Pitcher's Name: ")
outs_recorded = st.number_input("Enter how many outs the pitcher recorded: ", min_value=0, step=1)
number_strikeouts = st.number_input("How many strikeouts did they accumulate: ", min_value=0, step=1)
hits_allowed = st.number_input("How many hits did they allow? ", min_value=0, step=1)
earned_runs = st.number_input("How many earned and unearned runs were allowed? ", min_value=0, step=1)
bb_allowed = st.number_input("How many walks (BB) were allowed? ", min_value=0, step=1)
home_runs = st.number_input("How many home runs were allowed? ", min_value=0, step=1)

# formula for game score total
Game_Score_Total = 40 + (outs_recorded * 2) + (number_strikeouts * 1) - (bb_allowed * 2) - (hits_allowed * 2) - (earned_runs * 3) - (home_runs * 6)

# Calculate and print the total
if st.button("Calculate Game Score"):
    st.success(f"{pitcher_name}'s Game Score: {Game_Score_Total}")
