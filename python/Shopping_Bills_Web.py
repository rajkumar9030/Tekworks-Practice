import streamlit as st
st.title("Salary and Bill Spending Calculator")
salary = st.number_input("Enter your salary", min_value=0, step=1000)
bill1 = st.number_input("Enter your bill1 amount", min_value=0, step=100)
bill2 = st.number_input("Enter your bill2 amount", min_value=0, step=100)
bill3 = st.number_input("Enter your bill3 amount", min_value=0, step=100)
if st.button("Calculate"):
    total_bill = bill1 + bill2 + bill3
    bill_percent = (total_bill / salary) * 100 \
        if salary > 0 \
        else 0
    if total_bill > salary:
        st.warning("You are spending more than your salary!")
    else:
        st.write("Your Salary is: " + str(salary))
        st.write("Your total spending is: " + str(total_bill))
        st.write("Your percentage of spending from salary is: " + str(bill_percent))