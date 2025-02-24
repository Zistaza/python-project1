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

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Features", "Live Demo", "Fun Facts", "Draw Something", "Text-to-Emoji"])

# ------------------- Home Page -------------------
if page == "Home":
    st.title("🚀 Streamlit Project: The Best Way to Build Python Apps?")
    st.write("This web app demonstrates how to build interactive Python apps using Streamlit.")
    
    # Ensure the image exists inside assets folder
    try:
        st.image("/banner.png", use_container_width=True)
    except:
        st.warning("⚠️ Image not found!")

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

# ------------------- Fun Facts -------------------
elif page == "Fun Facts":
    st.subheader("🎲 Fun Fact Generator")

    facts = [
        "Honey never spoils. Archaeologists have found 3000-year-old honey that's still good!",
        "A day on Venus is longer than a year on Venus!",
        "Octopuses have three hearts!",
        "Bananas are berries, but strawberries aren’t!",
        "You can’t hum while holding your nose!"
    ]

    if st.button("Get a Fun Fact!"):
        st.write("📢", random.choice(facts))

# ------------------- Draw Something -------------------

        # ------------------- Draw Something -------------------
if page == "Draw Something":
    st.subheader("🎨 Draw Something!")

    # Create a drawing canvas
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)", 
        stroke_width=5,
        stroke_color="black",
        background_color="white",
        height=300,
        width=400,
        key="canvas"
    )

    # Check if drawing exists
    if canvas_result.image_data is not None:
        img_array = canvas_result.image_data[:, :, :3]  # Remove alpha channel

        # Check if the image is blank (all pixels white)
        if not np.all(img_array == 255):  
            st.write("✅ Your Drawing Preview:")
            image = Image.fromarray(img_array.astype('uint8'))

            # Convert to bytes for download
            img_bytes = io.BytesIO()
            image.save(img_bytes, format="PNG")
            img_bytes.seek(0)

            # Download button
            st.download_button(
                label="📥 Download Drawing",
                data=img_bytes,
                file_name="drawing.png",
                mime="image/png"
            )
        else:
            st.warning("⚠️ Draw something first before downloading!")
# ------------------- Text-to-Emoji Converter -------------------
elif page == "Text-to-Emoji":
    st.subheader("😃 Text-to-Emoji Converter")

    emoji_dict = {
        "happy": "😃",
        "sad": "😢",
        "love": "❤️",
        "fire": "🔥",
        "cool": "😎",
        "angry": "😡"
    }

    user_input = st.text_input("Type something (e.g., 'I am happy today!'):")

    if user_input:
        words = user_input.lower().split()
        converted_text = " ".join([emoji_dict.get(word, word) for word in words])
        st.write("🔄 Converted Text: ", converted_text)
