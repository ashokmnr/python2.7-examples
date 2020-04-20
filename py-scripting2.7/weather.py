#!/usr/bin/python2.7

import requests
import sys
import os
from argparse import ArgumentParser

parser = ArgumentParser(description="Get the current weather information")
parser.add_argument("zip", help="zip/postal code to get the weather for")
parser.add_argument("--country", default="us",
                    help="country zip/postal belongs to, default is US")

args = parser.parse_args()

url = "http://api.openweathermap.org/data/2.5/weather?zip=%s,%s&appid=%s" % (
    args.zip, args.country, os.getenv("OWM_API_KEY"))

res = requests.get(url)

if res.status_code != 200:
    print("Error talking to weather provider: %s" % res.status_code)
    sys.exit(1)

print(res.json())
