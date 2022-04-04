# -*- coding: utf-8 -*-
import requests
import json

LOC="/translate/enis"
LOC="/process/service"


inp = """
Parents are being urged not to give their children certain Kinder Surprise chocolate eggs due to the possible presence of salmonella.

The UK's Food Standards Agency (FSA) said the eggs have a "potential link to a salmonella outbreak" where 57 cases have been found, with just over three quarters of those being children aged five or younger.
"""

print("INP:",inp)
r = requests.post("http://localhost:8080"+LOC, json={"type":"text","content":inp})
print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))
print()
