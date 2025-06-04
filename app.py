import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from game import HillClimbGame

st.set_page_config(layout="wide")
st.title("🏎️ Hill Climb Racing in Streamlit")

if "game" not in st.session_state:
    st.session_state.game = HillClimbGame()

game = st.session_state.game

# Game loop
if st.button("Step Forward"):
    game.update()

state = game.get_state()

fig, ax = plt.subplots()
ax.set_xlim(0, 300)
ax.set_ylim(0, 300)

# Plot terrain
terrain = game.terrain_points
xs, ys = zip(*terrain)
ax.plot(xs, ys, "k-")

# Plot vehicle
ax.plot(*state["wheel1"], "ro", label="Wheel 1")
ax.plot(*state["wheel2"], "bo", label="Wheel 2")
ax.plot(*state["chassis"], "go", label="Chassis")
ax.legend()
st.pyplot(fig)
