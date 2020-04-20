#!/usr/bin/python2.7

message = raw_input("Enter the message: ")
count = raw_input("Enter the count: ")

if count:
    count = int(count)
else:
    count = 1


def multi_echo(message, count):
    while count > 0:
        print(message)
        count -= 1


multi_echo(message, count)
