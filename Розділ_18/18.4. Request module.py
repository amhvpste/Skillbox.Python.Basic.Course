import requests
import json

my_req = requests.get('https://swapi.dev/api/people/3/')
print(my_req.text)


data = json.loads(my_req.text)
print(data)
