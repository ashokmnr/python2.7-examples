#!/usr/bin/python2.7

users = [
    {"admin": False, "active": False, "name": "Ashok"},
    {"admin": True, "active": True, "name": "John"},
    {"admin": False, "active": True, "name": "Sky"},
    {"admin": True, "active": False, "name": "Ben"}
]

line = 1

for user in users:
    if user["admin"] and user["active"]:
        print("%s ACTIVE - (ADMIN) %s" % (line, user["name"]))
    elif user["admin"]:
        print("%s (ADMIN) %s" % (line, user["name"]))
    elif user["active"]:
        print("%s ACTIVE - %s" % (line, user["name"]))
    else:
        print("%s %s" % (line, user["name"]))
    line += 1
