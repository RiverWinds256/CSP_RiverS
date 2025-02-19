# River Stanley, function notes python

#functions hold actions to be resused
#numer = (int(input)"please tell me a number:\n") 
def add(num0ne, numTwo):
   # num0ne = int(input("please tell me a number:\n"))

   # numTwo = int(input("please tell me another number:\n"))
    return num0ne + numTwo
#add(int(input)"please tell me a number:\n")
#add(5, 21)
#aruments set the vaule of of the parameters, which can change
#add(6, 22)

def vaules(type):
    return input(f"please give me a {type}:\n")

name = vaules("name")
place = vaules("place")
verb = vaules("verb (past tense)")

print(f"{name} was really fast getting to {place} because they {verb}ed the whole way there")