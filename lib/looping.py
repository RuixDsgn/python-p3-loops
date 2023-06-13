#!/usr/bin/env python3

def happy_new_year():
    countdown = 10

    while countdown > 0:
        print(countdown)
        countdown -= 1

    print("Happy New Year!")
    

def square_integers(int_list):
    squared_numbers = [num * num for num in int_list]
    return squared_numbers

def fizzbuzz():
    for countdown in range(1, 101):
        if countdown % 5 == 0 and countdown % 3 == 0:
            print ("FizzBuzz")
        elif countdown % 5 == 0:
            print ("Buzz")
        elif countdown % 3 == 0:
            print ("Fizz")
        else:
            print (countdown)
        
        
