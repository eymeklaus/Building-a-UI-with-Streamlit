import streamlit as st

# 1. Title
st.title("Superhero Name Creator")

# 2. Header
st.header("Everyone is a superhero")

# 3. Subheader
st.subheader("I want to know more about you")

# 4. Input Widgets
color = st.text_input("Enter your favorite color:")
if color:
    st.write(f"Beautiful color, {color}!")

# 5. Input Widgets
animal = st.text_input("Enter your favorite animal:")
if animal:
    st.write(f"Good choice, {animal}!")

# 6. Input Widgets
number = st.text_input("Enter your lucky number:")
if number:
    st.write(f"That gives us your luck, {number}!")

# 7. Selectbox
superpower = st.selectbox("Choose an option:", ['Choose one option', "flying", "invisibility", "super strength"])
if superpower != 'Choose one option':
    st.write(f"Amazing super power: {superpower}!")

if st.button('Your Superhero Generator'):
    if color and animal and number and superpower != 'Choose one option':
        superhero_name = f'{color} {animal} of {number} {superpower}'
        st.subheader(f"Your Superhero Name: {superhero_name}")
    else:
        st.warning("Please fill in all fields first!")