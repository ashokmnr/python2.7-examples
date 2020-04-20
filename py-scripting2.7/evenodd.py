#!/usr/bin/python2.7

user_input = float(input("Please enter value between 1 to 100: "))
while True:
    if user_input < 0 or user_input > 100:
        user_input = float(input("Please enter value between 1 to 100: "))
    else:
        if user_input % 2 == 0:
            print("This number is even %s" % user_input)
        else:
            print("This number is odd %s" % user_input)
        break
