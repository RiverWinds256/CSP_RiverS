#River Stanley, Financial Calculator Python



print("welcome to the finance calculator")

income=float(input("what is your income? "))

rent=float(input("how much do you spend on rent? "))

rentpercent=round(((rent/income)*100), 1)

utilities=float(input("how much do you spend on utities? "))

utilitiespercent=round(((utilities/income)*100), 1)

groceries=float(input("how much do you spend on groceries? "))

groceriespercent=round(((groceries/income)*100), 1)

transportation=float(input("how much do you spend on transportation? "))

transportaionpercent=round(((transportation/income)*100), 1)

spending=income-rent-utilities-groceries-transportation
saving=income*0.1
print("")

print("your rent is", rent, "$ which is", rentpercent, "% of your income\n")

print("your utilities cost is", utilities, "$ which is", utilitiespercent, "% of your income\n")

print("your groceries cost is", groceries, "$ which is", groceriespercent, "% of your income\n")

print("your transportation cost is", transportation, "$ which is ", transportaionpercent, "% of your income\n")

print("your ideal saving amount would be 10% of your income which would be", saving, ("$\n"))

print("what you have left is to spend is",spending,"$\n")

if spending<0: print("you are in debt, skill issue")
if saving<0: print ("you cannot save right now, you dont have enough money")


