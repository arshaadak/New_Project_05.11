import streamlit as st

st.title(Hello, Streamlit!)
st.write(This is a simple Streamlit app.)
name=st.text_input(What is your name?)
if name:
    st.write(fWelcome to the app {name})
    age_input = st.text_input(What is your age?)

    if age_input:  # Check if the input is not empty
        try:
            age = int(age_input)
            st.write(fYour age is: {age})
        except ValueError:
            st.write(Please enter a valid number.)
    else:
        st.write(Please enter your age.)
