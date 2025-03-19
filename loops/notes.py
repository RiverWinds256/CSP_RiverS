# River Stanley, Loop notes python 

#What is a loop? 
    # A section of code that repeats multiple times
#1 What are the two types of loops?
    
#2 for loop
nums = [12,3,66]

for nums in nums:
    print (nums)

    #while loop
x = 0 

while x <10:
    print(x)
    x+= 1 


#3 What is iteration
     #is just one instence of the loop  that specific instance of the loop
    #iteration the amount of times youaa re looping though 

#3 What are lists? 
    #a varible that holds multipole vaules 
nums = [1,2,3,4,5,6,7,6]
siblings = ["alex", "Katie", "andew"]

print(nums)
print(siblings[2]) #to call one thing

siblings[1]= "jake"
siblings.pop()
siblings.insert(1, "jaysshree")
siblings.insert (2,["joe", "noah", "bob"])
print(siblings)

#5 how do you make lists in python? 
    #STEP 1, []
    #step 2 varaibles with cooorevyt data type 
    #step 3 needed commas 


#6  How do you make for loops in python? 
for sibling in siblings:
    print(sibling)


for x in range(0,100, 20 ):
    print(x)
#7 How do you make while loops in python?
import random 

x = 1#varaiable to keep count of iterration
goose = random.randint(1,20)

while x <= 20: #infinete loops
    if x == goose:
        print("goose")
        break #tells loop to stop
else: 
    print("duck")

    print ("duck")
    x+= 1

#comtnue moves to the next interration 


#How do you make lists in C?
#How do you make for loops in C?
#How do you make while loops in C?