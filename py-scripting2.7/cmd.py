#!/usr/bin/python2.7

import subprocess

'''
code = subprocess.call(["ls", "-l"])
if code == 0:
    print("Command finished sucessfully")
else:
    print("failed with code: %i" % code)
'''

try:
    output = subprocess.check_output(
        "ls fake.txt",
        stderr=subprocess.STDOUT
    )
except OSError as err:
    print("Caught OSError")
    output = err
except subprocess.CalledProcessError as err:
    print("Caught CalledProcessErro")
    output = err

print(output)
