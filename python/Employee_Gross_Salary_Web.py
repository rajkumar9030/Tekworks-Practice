import streamlit as st
st.title("Gross Salary Calculator")
def calculate_gross_salary(basic_salary):
    if basic_salary < 0:
        return "Salary cannot be negative"
    else:
        if basic_salary < 10000:
            hra = (67 / 100) * basic_salary
            da = (73 / 100) * basic_salary
        elif basic_salary < 20000:
            hra = (69 / 100) * basic_salary
            da = (76 / 100) * basic_salary
        else:
            hra = (73 / 100) * basic_salary
            da = (89 / 100) * basic_salary
        gross_salary = hra + da + basic_salary
        return "Gross Salary is: " + str(gross_salary)
basic_salary = st.number_input("Enter your basic salary", min_value=0, step=100)
if st.button("Calculate"):
    if basic_salary > 0:
        result = calculate_gross_salary(basic_salary)
        st.write(result)
    else:
        st.write("Please enter a valid basic salary.")