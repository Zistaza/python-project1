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
elif page == "Fun Facts":  # Make sure it's properly placed in an elif block
    # Title with Icon
    st.markdown("<h2 style='text-align: center;'>🎲 Fun Fact Generator</h2>", unsafe_allow_html=True)

# Fun Fact List
facts = [
    # Science Facts
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
    
    # Animal Facts
    "A group of flamingos is called a 'flamboyance'!",
    "Sloths can hold their breath longer than dolphins!",
    "Tigers have striped skin, not just striped fur!",
    "A shrimp's heart is in its head!",
    "Cows have best friends and get stressed when separated!",
    "Ostriches can run faster than horses!",
    "Penguins propose to their mates with a pebble!",
    "Butterflies can taste with their feet!",
    "Some cats are allergic to humans!",

    # Space Facts
    "Neutron stars are so dense that a sugar-cube-sized piece would weigh billions of tons!",
    "One day on Mercury lasts about 176 Earth days!",
    "There’s a giant cloud of alcohol in space!",
    "The moon is slowly moving away from Earth at a rate of about 3.8 cm per year!",
    "If two pieces of the same metal touch in space, they will fuse together permanently!",

    # History Facts
    "Cleopatra lived closer in time to the invention of the iPhone than to the construction of the Great Pyramid!",
    "The shortest war in history lasted just 38 minutes!",
    "Napoleon was once attacked by a horde of bunnies!",
    "Ancient Romans used mouse brains as toothpaste!",

    # Human Body Facts
    "Your bones are about five times stronger than steel!",
    "The human brain generates enough electricity to power a small light bulb!",
    "You share about 60% of your DNA with bananas!",
    "The human body contains around 37.2 trillion cells!",
    "Your stomach gets a new lining every few days to prevent digesting itself!",

    # Random Fun Facts
    "You can’t hum while holding your nose!",
    "Wombat poop is cube-shaped!",
    "There’s an island in Japan ruled entirely by bunnies!",
    "Scotland has 421 words for snow!",
    "There's a species of fish that can climb waterfalls!",
    "A single spaghetti noodle is called a 'spaghetto'!",
    "Some turtles can breathe through their butts!",
    "The world’s longest hiccup spree lasted 68 years!",
    "Pineapples take about 2 years to grow!",
    "A group of crows is called a 'murder'!",
    "Your heart beats about 100,000 times per day!",
]

 # Button to Generate Fun Fact
    if st.button("Get a Fun Fact!", key="fun_fact_button"):
        fun_fact = random.choice(facts)  # Ensure 'facts' is defined before this line
        st.markdown(f"<div class='fact-box'>📢 {fun_fact}</div>", unsafe_allow_html=True)
        
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
        # 😀 Emotions
        "happy": "😃", "smile": "😊", "grin": "😁", "joy": "😂",
        "sad": "😢", "cry": "😭", "tear": "😿", "heartbroken": "💔",
        "love": "❤️", "heart": "💖", "kiss": "😘", "hug": "🤗",
        "angry": "😡", "mad": "🤬", "furious": "😠", "annoyed": "😤",
        "surprised": "😲", "shocked": "😱", "wow": "🤯",
        "laugh": "🤣", "funny": "😆", "joke": "😂",
        "bored": "😐", "confused": "😕", "thinking": "🤔",
        "sleep": "😴", "tired": "🥱", "yawn": "🥱",
        "cool": "😎", "nerd": "🤓", "robot": "🤖",

        # 🎉 Celebration
        "party": "🥳", "celebrate": "🎉", "clap": "👏", "cheers": "🍻",
        "win": "🏆", "medal": "🥇", "star": "⭐", "confetti": "🎊",
        "gift": "🎁", "trophy": "🏆", "prize": "🏅", "gold": "🥇",

        # 🔥 Actions & Gestures
        "thumbs up": "👍", "thumbs down": "👎", "ok": "👌",
        "peace": "✌️", "wave": "👋", "pray": "🙏",
        "muscle": "💪", "run": "🏃", "walk": "🚶",
        "dance": "💃", "yoga": "🧘", "clap": "👏",

        # 🌍 Nature
        "sun": "☀️", "moon": "🌙", "star": "⭐", "rain": "🌧️",
        "snow": "❄️", "cloud": "☁️", "fire": "🔥", "lightning": "⚡",
        "tree": "🌳", "flower": "🌸", "leaf": "🍃", "ocean": "🌊",
        "earth": "🌍", "mountain": "⛰️", "volcano": "🌋", "rainbow": "🌈",

        # 🍔 Food & Drinks
        "food": "🍕", "pizza": "🍕", "burger": "🍔", "fries": "🍟",
        "hotdog": "🌭", "taco": "🌮", "sushi": "🍣", "noodles": "🍜",
        "cake": "🎂", "chocolate": "🍫", "ice cream": "🍦", "cookie": "🍪",
        "coffee": "☕", "tea": "🍵", "wine": "🍷", "beer": "🍺",
        "water": "💧", "milk": "🥛", "juice": "🧃",

        # 🚗 Transportation
        "car": "🚗", "bike": "🚲", "bus": "🚌", "train": "🚆",
        "plane": "✈️", "rocket": "🚀", "boat": "⛵", "helicopter": "🚁",

        # 💻 Tech & Devices
        "computer": "💻", "laptop": "💻", "phone": "📱", "tablet": "📲",
        "watch": "⌚", "tv": "📺", "camera": "📷", "keyboard": "⌨️",
        "headphones": "🎧", "game": "🎮", "video": "📹", "music": "🎵",

        # 🎶 Music & Entertainment
        "song": "🎶", "guitar": "🎸", "piano": "🎹", "microphone": "🎤",
        "drum": "🥁", "radio": "📻", "movie": "🎬", "popcorn": "🍿",

        # ⚽ Sports
        "football": "⚽", "basketball": "🏀", "baseball": "⚾",
        "tennis": "🎾", "golf": "⛳", "running": "🏃",
        "swimming": "🏊", "cycling": "🚴", "boxing": "🥊",

        # 💰 Money & Finance
        "money": "💰", "rich": "🤑", "cash": "💵",
        "credit card": "💳", "bank": "🏦", "shopping": "🛍️",

        # 🏡 Home & Objects
        "house": "🏠", "building": "🏢", "bed": "🛏️",
        "light": "💡", "book": "📖", "newspaper": "📰",
        "pencil": "✏️", "paint": "🎨", "lock": "🔒",

        # 🛑 Warning & Symbols
        "stop": "🛑", "danger": "⚠️", "warning": "⚠️",
        "check": "✅", "cross": "❌", "question": "❓",
        "exclamation": "❗", "infinity": "♾️", "plus": "➕",
        "minus": "➖", "equal": "➗"
    }

    user_input = st.text_input("Type something (e.g., 'I am happy today!'):")

    if user_input:
        words = user_input.lower().split()
        converted_text = " ".join([emoji_dict.get(word, word) for word in words])
        st.write("🔄 Converted Text: ", converted_text) 
