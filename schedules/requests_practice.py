import requests
import json


url = "https://jsonplaceholder.typicode.com/comments"
params = {"postId": 1}

response = requests.get(url, params=params)
print(response.text)
a = response.json()

with open("requests_pracrice.json", "w") as req_json:
	json.dump(a, req_json, sort_keys=True, indent=4)

