salary = int(input("Enter your salary : "))
bill1 = int(input("Enter your bill1 amount : "))
bill2 = int(input("Enter your bill2 amount : "))
bill3 = int(input("Enter your bill3 amount : "))
total_bill = bill1 + bill2 + bill3
bill_percent = (total_bill/salary) * 100
if total_bill > salary:
    print("You are spending more than salary")
else:
    print("Your Salary is : " + str(salary))
    print("Your percentage of spending salary is : " + str(bill_percent))
