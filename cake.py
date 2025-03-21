#general ideas,  I was thinking two inputs for each person -River

#welcome banner, intro 

#customer speech EX: Bake me your best cake!

#Chiara What kind of cake? EX: vallinia, 
#chocolate, strawberry

#Chiara what kind of frosting EX: Buttercream, cream cheese, swiss meringue

#River Cake pans EX: circle, square, cupcake

#River temperature EX: 325-375 normal bake, under is underbaked, over by like 20 is overbaked any further is broken and on fire oven

#Lizzie frosting EX: pipped on, spooned on, none 

#Lizzie toppings EX: sprinkles, strawberries, cream

#Lila results EX: The customer loved your (size, flavor, topping) cake! The custom demanded a refund as their cake was over/under baked


shape=input("What kind of kind of cake will you bake? A circle cake, a square cake or cupcakes?\n").strip()
if shape!="circle" and shape!="square" and shape!="cupcakes":
     print("We dont have that kind of cakepan\n")     

temp=input("What temperature will you set the oven?\n")   
if temp<320:
     print("Your cake hasn't baked")
elif temp<319:
     print("Your cake is a little undercooked but it will work\n")
elif temp>=320 and temp<=375: 
    print("Your cake is perfectly baked")
elif temp>=400 and temp<=420:
     print("Your cake is a little burnt but it will work\n")   
else:
     print("The oven has lit on fire and burned down the bakery, game over")
     exit()