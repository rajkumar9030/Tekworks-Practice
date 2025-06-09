import streamlit as st
st.title("Even or Odd Number Checker")
number = st.number_input("Enter a number:", step=1)
if st.button('Check'):
    if number % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    st.write(f"The number {number} is {result}.")