"""
project, internal and external scores --- 100
total marks:
    project - 70%
    Internal - 10%
    External - 20%
        90+ A grade
        80 - 90 B grade
        50-80 C grade
if project 90 , internal - 60 , external - 45
failed in external and score is - 45
"""


def Student_Grade(project_score, internal_score, external_score):
    if project_score < 0 or internal_score < 0 or external_score < 0:
        print("Score cannot be negative. Please enter valid score")
    else:
        if project_score < 50:
            print("Failed in project and your score is " + str(project_score))
        if internal_score < 50:
            print("Failed in internal and your score is " + str(internal_score))
        if external_score < 50:
            print("Failed in external and your score is " + str(external_score))
        elif project_score >= 50 and internal_score >= 50 and external_score >= 50:
            project_score = (70 / 100) * project_score
            internal_score = (10 / 100) * internal_score
            external_score = (20 / 100) * external_score
            total_score = project_score + internal_score + external_score
            if total_score > 90:
                print("Grade A and your score is " + str(total_score))
            elif total_score > 80:
                print("Grade B and your score is " + str(total_score))
            else:
                print("Grade C and your score is " + str(total_score))


project_score = int(input("Enter your Project Score : "))
internal_score = int(input("Enter your internal Score : "))
external_score = int(input("Enter your external Score : "))
Student_Grade(project_score, internal_score, external_score)
