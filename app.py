#Loop through numbers from 1 to 100
for i in range(1, 101):
    #If number is a multiple of 3 print Fizz, if a mulitiple of 5 print Buzz, if a multiple of 
    #both 3 and 5 print FizzBuzz, otherwise print the number
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)