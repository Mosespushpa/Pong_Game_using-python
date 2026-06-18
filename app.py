import streamlit as st
import time
import random

st.set_page_config(layout="wide")

# --- Game State ---
if "ball_x" not in st.session_state:
    st.session_state.ball_x = 0
    st.session_state.ball_y = 0
    st.session_state.ball_dx = 10
    st.session_state.ball_dy = 10
    st.session_state.speed = 0.05

    st.session_state.l_paddle = 0
    st.session_state.r_paddle = 0

    st.session_state.l_score = 0
    st.session_state.r_score = 0


# --- UI Controls ---
col1, col2, col3 = st.columns([1,2,1])

with col1:
    st.subheader("Left Player")
    if st.button("Up (W)"):
        st.session_state.l_paddle += 20
    if st.button("Down (S)"):
        st.session_state.l_paddle -= 20

with col3:
    st.subheader("Right Player")
    if st.button("Up (↑)"):
        st.session_state.r_paddle += 20
    if st.button("Down (↓)"):
        st.session_state.r_paddle -= 20


# --- Game Display ---
placeholder = st.empty()

def draw():
    game_html = f"""
    <div style="background:black;height:500px;position:relative;">
        <!-- Ball -->
        <div style="
            width:20px;height:20px;background:white;
            position:absolute;
            left:{st.session_state.ball_x + 390}px;
            bottom:{st.session_state.ball_y + 240}px;
            border-radius:50%;">
        </div>

        <!-- Left Paddle -->
        <div style="
            width:20px;height:100px;background:white;
            position:absolute;
            left:10px;
            bottom:{st.session_state.l_paddle + 200}px;">
        </div>

        <!-- Right Paddle -->
        <div style="
            width:20px;height:100px;background:white;
            position:absolute;
            right:10px;
            bottom:{st.session_state.r_paddle + 200}px;">
        </div>

        <!-- Score -->
        <div style="color:white;text-align:center;font-size:40px;">
            {st.session_state.l_score} : {st.session_state.r_score}
        </div>
    </div>
    """
    placeholder.markdown(game_html, unsafe_allow_html=True)


# --- Game Loop ---
run = st.button("Start Game")

if run:
    for _ in range(1000):
        time.sleep(st.session_state.speed)

        # Move ball
        st.session_state.ball_x += st.session_state.ball_dx
        st.session_state.ball_y += st.session_state.ball_dy

        # Wall bounce
        if st.session_state.ball_y > 250 or st.session_state.ball_y < -250:
            st.session_state.ball_dy *= -1

        # Paddle collision
        if (
            st.session_state.ball_x > 340 and
            abs(st.session_state.ball_y - st.session_state.r_paddle) < 60
        ):
            st.session_state.ball_dx *= -1

        if (
            st.session_state.ball_x < -340 and
            abs(st.session_state.ball_y - st.session_state.l_paddle) < 60
        ):
            st.session_state.ball_dx *= -1

        # Score
        if st.session_state.ball_x > 380:
            st.session_state.l_score += 1
            st.session_state.ball_x, st.session_state.ball_y = 0, 0

        if st.session_state.ball_x < -380:
            st.session_state.r_score += 1
            st.session_state.ball_x, st.session_state.ball_y = 0, 0

        draw()
