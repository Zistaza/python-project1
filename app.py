import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io
import os
from io import BytesIO

# Set up Streamlit page
st.set_page_config(page_title="Best Way to Build Python Apps", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Features", "Live Demo", "Data Sweeper", "Fun Facts", "Draw Something", "Text-to-Emoji"]
)

# ------------------- Home Page -------------------
if page == "Home":
    st.title("🌟 Growth Mindset Web App: Innovate, Create & Analyze with Ease")
    st.write("Explore a suite of intelligent tools designed to boost efficiency, spark creativity, and simplify data processing.")

    # Display Image
    image_path = "webappbanner.jpg"
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.warning("⚠️ Image not found! Please ensure 'webappbanner.jpg' is in the same directory.")

    st.markdown("### Why Use This Web App?")
    features = [
        "🛠️ **Features:** A collection of AI-powered utilities designed for efficiency and engagement.",
        "🚀 **Live Demo:** Experience real-time interactions with AI-driven tools.",
        "📊 **Data Sweeper:** Effortlessly clean and preprocess data for better insights.",
        "🎉 **Fun Facts:** Discover random, interesting facts that spark curiosity.",
        "🎨 **Draw Something:** Express your creativity with an AI-assisted drawing tool.",
        "😃 **Text-to-Emoji:** Instantly transform text into meaningful emoji expressions."
    ]
    for feature in features:
        st.write(feature)

    st.markdown("### Built with:")
    st.write("⚡ **Streamlit** for fast and interactive UI development")
    st.write("🤖 **AI & Data Processing** for automation and intelligent insights")
    st.write("📊 **Visualization Tools** for enhanced data representation")

# ------------------- Features Page -------------------
elif page == "Features":
    st.subheader("🚀 Explore the Key Features!")
    feature_list = [
        "Seamless User Experience with an intuitive interface",
        "Live Data Updates for real-time insights",
        "AI-Powered Enhancements for smarter interactions",
        "Stunning Visualizations to make data easy to understand",
        "Interactive Tools for a hands-on experience",
        "Multi-Platform Support for accessibility anywhere"
    ]
    for feature in feature_list:
        st.write("- " + feature)

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

# ------------------- Data Sweeper -------------------
elif page == "Data Sweeper":
    st.title("Datasweeper Sterling Integrator By Zeenat Yameen")
    st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization.")

    # File Uploader
    uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

    if uploaded_files:
        for file in uploaded_files:
            file_ext = os.path.splitext(file.name)[-1].lower()
            df = None

            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue

            # File details
            st.write(f"Preview of {file.name}")
            st.dataframe(df.head())

            # Data Cleaning
            st.subheader(f"Data Cleaning Options for {file.name}")
            if st.checkbox(f"Remove duplicates from {file.name}"):
                df.drop_duplicates(inplace=True)
                st.write("Duplicates removed!")

            if st.checkbox(f"Fill missing values for {file.name}"):
                numeric_cols = df.select_dtypes(include=['number']).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.write("Missing values filled!")

            # Select Columns to Keep
            st.subheader("Select Columns to Keep")
            columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
            df = df[columns]

            # Data Visualization
            st.subheader("📊 Data Visualization")
            if st.checkbox(f"Show visualization for {file.name}"):
                st.bar_chart(df.select_dtypes(include='number'))

            # File Conversion
            st.subheader("Conversion Options")
            conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".csv")
                    mime_type = "text/csv"
                else:
                    df.to_excel(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                buffer.seek(0)
                st.download_button(label=f"Download {file.name} as {conversion_type}", data=buffer, file_name=file_name, mime=mime_type)

# ------------------- Fun Facts -------------------
elif page == "Fun Facts":
    st.subheader("🎲 Fun Fact Generator")
    facts = [
        "Honey never spoils!",
        "Bananas are berries, but strawberries aren’t!",
        "A shrimp's heart is in its head!",
        "Octopuses have three hearts!",
        "Penguins propose with pebbles!",
        "You share about 60% of your DNA with bananas!"
    ]
    if st.button("Get a Fun Fact!"):
        st.success(random.choice(facts))

# ------------------- Draw Something -------------------
elif page == "Draw Something":
    st.subheader("🎨 Draw Something!")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)", 
        stroke_width=5,
        stroke_color="black",
        background_color="white",
        height=300,
        width=400,
        key="canvas"
    )

    if canvas_result.image_data is not None:
        img_array = canvas_result.image_data[:, :, :3]
        if not np.all(img_array == 255):
            st.image(img_array)
            img_bytes = io.BytesIO()
            Image.fromarray(img_array.astype('uint8')).save(img_bytes, format="PNG")
            img_bytes.seek(0)
            st.download_button("📥 Download Drawing", img_bytes, "drawing.png", "image/png")

# ------------------- Text-to-Emoji -------------------
elif page == "Text-to-Emoji":
    st.subheader("😃 Text-to-Emoji Converter")
    emoji_dict = {"happy": "😃", "sad": "😢", "love": "❤️", "angry": "😡", "fire": "🔥", "cool": "😎"}
    text_input = st.text_input("Enter a word:")
    if text_input:
        emoji = emoji_dict.get(text_input.lower(), "❓")
        st.write(f"Emoji: {emoji}")
