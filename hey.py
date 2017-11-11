import json
from userClass import User

def hey():
	json_data=open("dummy_user.json").read()
	data = json.loads(json_data)
	for i in len(data):
		print(data[accounts][i])

def create_user():
	# username = "janedoe"
	# password = "password"
	new_u = User("jane", "password")
	print(str(new_u))

create_user() 