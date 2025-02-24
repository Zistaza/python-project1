import streamlit as st
import pandas as pd
import numpy as np
import emoji
import matplotlib.pyplot as plt

# App Title
st.set_page_config(page_title="Multi-Feature App", layout="wide")
st.title("🚀 Multi-Feature Streamlit App")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Fun Facts", "Drawing", "Text to Emoji", "Data Sweeper"])

if page == "Home":
    st.write("Welcome to the multi-feature app! Navigate using the sidebar.")

elif page == "Fun Facts":
    st.header("Did You Know? 🤔")
    facts = [
        "Bananas are berries, but strawberries aren't! 🍌",
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible! 🍯",
        "Octopuses have three hearts and blue blood. 🐙",
        "A bolt of lightning is five times hotter than the surface of the sun. ⚡"
    ]
    st.write(np.random.choice(facts))

elif page == "Drawing":
    st.header("Draw Something! 🎨")
    canvas_result = st.text_area("Describe your drawing:")
    if st.button("Save Drawing"):
        st.success("Drawing description saved!")

elif page == "Text to Emoji":
    st.header("Convert Text to Emoji 🔠➡️😀")
    user_input = st.text_input("Enter a word or phrase:")
    if user_input:
        st.write("Emoji Translation: ", emoji.emojize(user_input, language='alias'))

elif page == "Data Sweeper":
    st.header("📊 Data Sweeper - Sterling Integrator")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Raw Data:")
        st.write(df.head())
        
        # Data Cleaning Options
        st.subheader("🔍 Data Cleaning")
        if st.button("Drop Duplicates"):
            df = df.drop_duplicates()
            st.success("Duplicates removed!")
            st.write(df.head())
        
        missing_values_option = st.selectbox("Handle Missing Values", ["None", "Drop Rows", "Fill with Mean", "Fill with Zero"])
        if missing_values_option == "Drop Rows":
            df = df.dropna()
            st.success("Rows with missing values removed!")
        elif missing_values_option == "Fill with Mean":
            df = df.fillna(df.mean())
            st.success("Missing values filled with column mean!")
        elif missing_values_option == "Fill with Zero":
            df = df.fillna(0)
            st.success("Missing values replaced with zero!")
        
        st.write("### Cleaned Data:")
        st.write(df.head())
        
        # Data Visualization
        st.subheader("📊 Data Visualization")
        column = st.selectbox("Select a Column to Visualize", df.columns)
        if column:
            fig, ax = plt.subplots()
            df[column].hist(ax=ax, bins=20, edgecolor='black')
            st.pyplot(fig)
        
        # Save cleaned data
        if st.button("Download Cleaned Data"):
            df.to_csv("cleaned_data.csv", index=False)
            st.success("Cleaned data ready for download!")
