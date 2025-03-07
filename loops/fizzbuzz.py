# River Stanley Fizzbuzz

for x in range(0,51):
    if x%5 ==0 and x%3 ==0:
        print("fizzbuzz")
    elif x%5 ==0:
        print("buzz")
    elif x%3 ==0:
        print("fizz")
    else: 
        print(x)