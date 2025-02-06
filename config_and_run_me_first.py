#===CHANGE=ME===#
import sys

# Relative directory to API key file. You can get this file from
# Access > Users > [a user with enought permission] > API Keys
api_file = "api_key.txt"

# IP/hostname of your opnsense router.
opnsense_host = "192.168.42.1"

#==CODE==#
import sys
import requests
from os import path, listdir

# Read api key
with open(api_file) as f:
    api_key = f.readline().strip().removeprefix("key=")
    api_secret = f.readline().strip().removeprefix("secret=")

opnsense_api = f"https://{opnsense_host}/api"
print("==API==")
print(f"key: {api_key}")
print(f"secret: {api_secret}")
print(f"Going to {opnsense_api}")

# API
session = requests.Session()
session.auth = (api_key, api_secret)

# Interactive locator
response = session.get(f"{opnsense_api}/wireguard/client/list_servers", verify=False)
print(response.json())