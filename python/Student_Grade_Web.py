import streamlit as st
st.title("Student Grade Calculator")
def student_grade(project_score, internal_score, external_score):
    if project_score < 0 or internal_score < 0 or external_score < 0:
        return "Score cannot be negative. Please enter valid scores."

    failed = []
    if project_score < 50:
        failed.append("Project (score: " + str(project_score) + ")")
    if internal_score < 50:
        failed.append("Internal (score: " + str(internal_score) + ")")
    if external_score < 50:
        failed.append("External (score: " + str(external_score) + ")")
    if failed:
        return "Failed in: " + ', '.join(failed)

    project_score = (70 / 100) * project_score
    internal_score = (10 / 100) * internal_score
    external_score = (20 / 100) * external_score
    total_score = project_score + internal_score + external_score
    if total_score >= 90:
        return "Grade A with total score: " + str(total_score)
    elif total_score >= 80:
        return "Grade B with total score: " + str(total_score)
    else:
        return "Grade C with total score: " + str(total_score)

project_score = st.number_input("Enter your Project Score", min_value=0, max_value=100, step=1)
internal_score = st.number_input("Enter your Internal Score", min_value=0, max_value=100, step=1)
external_score = st.number_input("Enter your External Score", min_value=0, max_value=100, step=1)

if st.button("Calculate Grade"):
    if project_score >= 0 and internal_score >= 0 and external_score >= 0:
        result = student_grade(project_score, internal_score, external_score)
        st.write(result)
    else:
        st.write("Please enter valid scores for all subjects.")