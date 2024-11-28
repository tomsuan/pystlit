import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="My First Streamlit App", layout="wide")

# Add a title and intro text
st.title("Welcome to My Website")
st.write("This is a simple example of what you can build with Streamlit!")

# Add a sidebar with options
st.sidebar.header("Settings")
name = st.sidebar.text_input("Enter your name")
color = st.sidebar.color_picker("Pick a color")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.header("Interactive Elements")
    # Add a slider
    age = st.slider("How old are you?", 0, 100, 25)
    st.write(f"I'm {age} years old")
    
    # Add a button
    if st.button("Click me!"):
        st.write(f"Hello {name}! You selected {color} as your color.")

with col2:
    st.header("Data Display")
    # Create some sample data
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 20, 30, 40]
    })
    
    # Display the data
    st.write("Here's a sample data table:")
    st.dataframe(data)
    
    # Create a chart
    st.bar_chart(data.set_index('Category'))

# Add a file uploader
st.header("Upload Files")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("File uploaded successfully!")

# Add a footer
st.markdown("---")
st.markdown("Built with Streamlit and Python ❤️")
