#general ideas,  I was thinking two inputs for each person -River

#welcome banner, intro 

#customer speech EX: Bake me your best cake!

#Chiara What kind of cake? EX: vallinia, 
#chocolate, strawberry

#Chiara ingredients and cake mix EX: eggs, water, cakemix (This will probably be void and just for playtime)

#River Cake pans EX: circle, square, cupcake

#River temperature EX: 325-375 normal bake, under is underbaked, over by like 20 is overbaked any further is broken and on fire oven

#Lizzie frosting EX: vallinia, chocolate, strawberry 

#Lizzie toppings EX: sprinkles, strawberries, cream

#Lila results EX: The customer loved your (size, flavor, topping) cake! The custom demanded a refund as their cake was over/under baked


shape=input("What kind of kind of cake will you bake? A circle cake, a square cake or cupcakes?").strip()
if shape!="circle" and shape!="square" and shape!="cupcakes":
     print("We dont have that kind of cakepan")     

temp=input("What temperature will you set the oven?\n")   
if temp>=320 and temp<=375: 
    temp=1
    print("Your cake is perfectly baked")
elif temp<319:
     temp=0
     print("Your cake is a bit unbaked")
elif temp>=400 and temp<=420:
     temp=2
     print("Your cake is burnt")   
else:
     print("The oven has lit on fire and burned down the bakery, game over")
     exit()
print (temp)