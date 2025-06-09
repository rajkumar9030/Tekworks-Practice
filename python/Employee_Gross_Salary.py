"""Accept basic salary and find gross salary
GrossSalary = HRA+DA+Basic
basic_salary<10000 -- HRA - 67% on basic_salary DA is 73% on basic_salary
basic_salary b/w 10k and 20k -- HRA - 69% on basic salary DA is 76% on basic_salary
basic_salary above 20k -- HRA - 73% on basic_salary DA is 89% on basic_salary"""


def Calculate_Gross_Salary(basic_salary):
    if basic_salary < 0:
        print("Salary cannot be negative")
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
        print("Gross Salary is : " + str(gross_salary))


basic_salary = int(input("Enter your salary : "))
Calculate_Gross_Salary(basic_salary)
