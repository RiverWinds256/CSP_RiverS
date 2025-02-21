#River Stanley, Financial Calculator Python updated

def info(cost, income, type):
    percent = cost/income*100
    print(f"your {type} is {cost:.2f} dollars which is {percent:.2f} percent of your income\n")

print("welcome to the finance calculator")

def spend(type):
    return float(input(f"How much do you spend on {type}? "))
    

income=float(input("what is your income? "))
rent=spend("rent")
utilities=spend("utilities")
groceries=spend("groceries")
transportation=spend("transportation")

spending=income-rent-utilities-groceries-transportation
saving=income*0.1

info(rent, income, "rent")
info(utilities, income, "utities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(spending, income, "spending")

print("your ideal saving amount would be 10% of your income which would be", saving, ("$\n"))

print("what you have left is to spend is",spending,"$\n")
