import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import openai
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")  # Get API key from .env file

# Set up Streamlit page
st.set_page_config(page_title="Best Way to Build Python Apps", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Features", "Live Demo", "AI Chatbot", "Weather"])

# ------------------- Home Page -------------------
if page == "Home":
    st.title("🚀 Streamlit Project: The Best Way to Build Python Apps?")
    st.write("This web app demonstrates how to build interactive Python apps using Streamlit.")
    
    # Ensure the image exists inside assets folder
    try:
        st.image("assets/banner.png", use_column_width=True)
    except:
        st.warning("⚠️ Image not found in 'assets/' folder!")

    st.markdown("### Why Streamlit?")
    st.write("✅ Quick Development, 🛠️ Easy Deployment, 📊 Great for Data Apps")

# ------------------- Features Page -------------------
elif page == "Features":
    st.subheader("📌 Key Features of This Web App")
    st.write("- Interactive UI Elements")
    st.write("- Real-time Data Fetching")
    st.write("- AI-Powered Features")
    st.write("- Beautiful Data Visualizations")

# ------------------- Live Demo Page -------------------
elif page == "Live Demo":
    st.subheader("📊 Live Data Visualization")

    # Generate Random Data
    df = pd.DataFrame({
        "x": np.random.randn(100),
        "y": np.random.randn(100)
    })

    # Plotly Scatter Plot
    fig = px.scatter(df, x="x", y="y", title="Random Data Distribution")
    st.plotly_chart(fig)

# ------------------- AI Chatbot -------------------
elif page == "AI Chatbot":
    st.subheader("🤖 AI Chatbot")
    openai_key = st.text_input("Enter OpenAI API Key", type="password")
    user_input = st.text_input("Ask me anything:")

    if openai_key and user_input:
        openai.api_key = openai_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        st.write("Chatbot:", response["choices"][0]["message"]["content"])

# ------------------- Real-time Weather Data -------------------
elif page == "Weather":
    st.subheader("🌦️ Real-Time Weather Data")
    city = st.text_input("Enter a city:")

    if city and api_key:
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(api_url).json()

        if response.get("main"):
            st.write(f"🌡️ Temperature: {response['main']['temp']}°C")
            st.write(f"💨 Wind Speed: {response['wind']['speed']} m/s")
        else:
            st.error("City not found!")
    elif not api_key:
        st.error("⚠️ API Key is missing. Please check your .env file.")

# ------------------- Dark Mode & Custom Styling -------------------
st.markdown("""
    <style>
        .main {
            background-color: #222;
            color: white;
        }
        .stTextInput>div>div>input {
            background-color: #333 !important;
            color: white !important;
        }
        .stAlert {
            background-color: #444 !important;
        }
    </style>
""", unsafe_allow_html=True)
