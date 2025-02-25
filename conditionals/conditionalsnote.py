
#River Stanley 

#1 What puts something inside of the “if” statement?
    #if condion: then do this
name=input("what is your name:\n")
if name== "laRose":
    print("Hi Ms. LaRose")
# A tab/ that weird gap, it shows its in the statement



#2 What do if statements do?
#Checks a condition, and if it is true, it will do a thing
name=input("what is your name:\n")
if name== "laRose": #<- this is a condition
    print("Hi Ms. LaRose")##<- this is what it does if true
else: #This happens if the condition is false
    print(f"hello{name}")



#3 What are boolean statements? 
name=input("what is your name:\n") #<- boolean either true or false
if name== "laRose": 
    print("Hi Ms. LaRose")
else: 
    print(f"hello{name}")
#part of your conditional that has true/false



#4 What do else statements do?

    #if boolean is false, thing happens
name=input("what is your name:\n") 
if name== "laRose": 
    print("Hi Ms. LaRose")
else: 
    print(f"hello{name}") #<- else



#5 What kind of statement do you use if you have more than 2 needed outcomes?

num = input("how many cookies are there? ")
    #computers read things up to down, put least likely first than most  

if num == 0: # <- if always starts the conditional
    print("there are none.")
    
elif  num != 1: 
    print("there is one") # <- everything in between is elif 

elif num <4: 
    print("there is a couple")

elif num < 10: 
    if num==8:
        print("this prints at 8")
    ("there are a few")

else: # <- ends the condirional
    print ("there are many")



#6 What do each of the different symbols mean in conditionals?

    #< less than
    #> greater than
    #<= less than or equal to
    #>= greater than or equal to
    #== equal to 
    #=== doesnt exist in python (in c it checks if the data type is also the same)
    #! means not equal to


#7 What are the 3 logical operators?

    #and, or, not

if num <10 and num > 5: # both booleans must be true to have an and, or means one must be true
    print("this is a big single digit number")

elif not num  < 10: #Not cahnges to check if false

    print("this is a big single digit number")
    #multiple can be in 1 statement 



#8 What are logical operators for?
    #allows code to be be able to handle more complex things 



#9 What does a nested conditional statement do?
    #conditonal in another one, only checked if the first one is true. Never go past 3 

if num <10: 
    if num == 8:
        print ("this prints at 8")
    else: 
        if num == 4: 
            print ("i didnt get this")    

