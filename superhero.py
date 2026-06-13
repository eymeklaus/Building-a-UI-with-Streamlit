import streamlit as st

# 1. Title
st.title("Superhero Name Creator")

# 2. Header
st.header("Everyone is a superhero")

# 3. Subheader
st.subheader("I want to know more about you")

# 4. Input Widgets
color = st.text_input("Enter your favorite color:")
st.write(f"Hello, {color}!")

# 5. Input Widgets
animal = st.text_input("Enter your favorite animal:")
st.write(f"Hello, {animal}!")

# 6. Input Widgets
number = st.text_input("Enter your lucky number:")
st.write(f"Hello, {number}!")

# 7. Selectbox
superpower = st.selectbox("Choose an option:", ["flying", "invisibility", "super strength"])
st.write(f"You selected: {superpower}")

if st.button('Your Superhero Generator'):
    superhero_name = f'{color[:2]} {animal[:2]} of {number[:2]} {superpower[:2]}'  # Fixed
    st.subheader(f"Your Superhero Name: {superhero_name}")  # Fixed