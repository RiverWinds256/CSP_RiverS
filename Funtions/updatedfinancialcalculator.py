#River Stanley, Financial Calculator Python updated

def info(cost, income, type):
    percent = cost/income*100
    print(f"your {type} is {cost:.2f} dollars which is {percent:.2f} percent of your income\n")

print("welcome to the finance calculator")

def user():
    float(input("how much do you spend on rent? "))

income=float(input("what is your income? "))

rent=float(input("how much do you spend on rent? "))

utilities=float(input("how much do you spend on utities? "))

groceries=float(input("how much do you spend on groceries? "))

transportation=float(input("how much do you spend on transportation? "))

spending=income-rent-utilities-groceries-transportation
saving=income*0.1

info(rent, income, "rent")
info(utilities, income, "utities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(spending, income, "spending")
print("")

print("your ideal saving amount would be 10% of your income which would be", saving, ("$\n"))

print("what you have left is to spend is",spending,"$\n")
