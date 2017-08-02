import textblob
import os
import json
import requests
import random
with open("Json/greetings.json",'r+') as f:
	greetings=json.load(f)
	gr=input(" ")
	if gr in greetings["User_Greeting"]:
		print(random.choice(greetings["Greetings"]))
