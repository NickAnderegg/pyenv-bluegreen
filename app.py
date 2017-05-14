import requests
import json

response = requests.get('https://status.digitalocean.com/api/v1/status.json')
status = response.json()

print(status['status']['description'])
