#!/usr/bin/python2.7
import os

with open("xmen.txt", "a") as xmen_file:
    xmen_file.write("Professor Xavier\n")

#xmen_file = open("xmen.txt", "a")
#xmen_file.writelines(["Morph\n", "Rogue\n"])

#xmen_file.seek(-1, os.SEEK_END)
# xmen_file.write("\nBeast\n")
# xmen_file.write("Phoenix\n")
# print(xmen_file.read())

# xmen_file.close()
