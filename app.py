import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io

# Set up Streamlit page
st.set_page_config(page_title="Best Way to Build Python Apps", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .fact-box {
            padding: 15px;
            border-radius: 10px;
            background-color: #f9f9f9;
            border-left: 5px solid #ff6f61;
            font-size: 18px;
            margin-top: 10px;
        }
        .emoji-box {
            padding: 15px;
            border-radius: 10px;
            background-color: #e0f7fa;
            border-left: 5px solid #00796b;
            font-size: 20px;
            margin-top: 10px;
            font-weight: bold;
        }
        .styled-btn {
            background-color: #4CAF50 !important;
            color: white !important;
            font-weight: bold !important;
            border-radius: 8px !important;
        }
        .stTextInput>div>div>input {
            font-size: 18px !important;
            padding: 10px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Features", "Live Demo", "Fun Facts", "Draw Something", "Text-to-Emoji"])

# ------------------- Fun Facts -------------------
if page == "Fun Facts":
    st.markdown("<h2 style='text-align: center;'>🎲 Fun Fact Generator</h2>", unsafe_allow_html=True)

    # Fun Fact List
    facts = [
        "Honey never spoils. Archaeologists have found 3000-year-old honey that's still good!",
        "A day on Venus is longer than a year on Venus!",
        "Octopuses have three hearts!",
        "Water can boil and freeze at the same time in special conditions called the 'triple point'!",
        "Bananas are berries, but strawberries aren’t!",
        "Sharks have been around longer than trees!",
        "Your body has more bacterial cells than human cells!",
        "The Eiffel Tower grows taller in summer due to metal expansion!",
        "Some jellyfish are biologically immortal!",
        "There are more stars in space than grains of sand on Earth!",
    ]

    if st.button("Get a Fun Fact!", key="fun_fact_button", help="Click to reveal a fun fact"):
        fun_fact = random.choice(facts)
        st.markdown(f"<div class='fact-box'>📢 {fun_fact}</div>", unsafe_allow_html=True)

# ------------------- Text-to-Emoji Converter -------------------
elif page == "Text-to-Emoji":
    st.subheader("😃 Text-to-Emoji Converter")

    emoji_dict = {
        "happy": "😃", "smile": "😊", "grin": "😁",
        "sad": "😢", "cry": "😭", "laugh": "🤣",
        "cool": "😎", "party": "🥳", "fire": "🔥",
        "love": "❤️", "thumbs up": "👍", "clap": "👏",
        "sun": "☀️", "moon": "🌙", "pizza": "🍕",
        "car": "🚗", "game": "🎮", "music": "🎵",
    }

    user_input = st.text_input("Type something (e.g., 'I am happy today!'):")

    if user_input:
        words = user_input.lower().split()
        converted_text = " ".join([emoji_dict.get(word, word) for word in words])
        st.markdown(f"<div class='emoji-box'>🔄 {converted_text}</div>", unsafe_allow_html=True)
