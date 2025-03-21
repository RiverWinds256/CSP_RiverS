
temp=int(input("What temperature will you set the oven?\n"))   
if temp>=320 and temp<=375: 
    temp=2
    print("Your cake is perfect!")
elif temp<319:
     temp = 1
     print("Your cake is a little undercooked but it will work\n")
elif temp<375:
     temp=3
     print("Your cake is a little overcooked but it will work\n")  
     
else:
     print("The oven has lit on fire and burned down the bakery, game over")
     exit()
     print (temp)