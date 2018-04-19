import requests
import json

url = "http://perun.nti.tul.cz/~honza/ws/users"
headers = {'Content-type': 'application/json'}


user = {
    "name" : "vladimir.nevyhosteny",
    "pass" : "123456789"
}
user_json = json.dumps(user)

response_insert = requests.post(url, data=user_json, headers=headers)

print("insert request: " + response_insert.text)


response_read = requests.get(url)
users = response_read.json()
users_json = json.loads(json.dumps(users))

print("list of users:\n" + json.dumps(users_json, indent=4, sort_keys=True))