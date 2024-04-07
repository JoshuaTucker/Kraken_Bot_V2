import requests
import os
import pprint

resp = requests.get('https://api.kraken.com/0/public/Time')

print(resp.json())

print(os.environ['HOME'])