#!/usr/bin/python2.7

import os

stage = (os.getenv("STAGE") or "development").upper()

output = "We're running is %s" % stage

if stage.startswith("PROD"):
    output = "DANGER!!! - %s" % output
print(output)
