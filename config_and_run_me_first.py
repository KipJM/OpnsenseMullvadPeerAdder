# === READ ME ===
# FIRST, Modify THIS file and run this to get the UUID!
# THEN, modify and run config_and_run_me_second.py!

#===CHANGE=ME===#
# Relative directory to API key file. You can get this file from
# Access > Users > [a user with enought permission] > API Keys
api_file = "api_key.txt"

# IP/hostname of your opnsense router.
opnsense_host = "192.168.42.1"

#==CODE==#
import requests
import sys

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

# locator
try:
    response = session.get(f"{opnsense_api}/wireguard/client/list_servers", verify=False)
    response_json = response.json()
    # print(response_json)
    if response_json["status"] != "ok":
        raise Exception(f"JSON response is not OK! ({response_json})")
except Exception as e:
    print(f"Something went wrong during API call. Make sure the API key is correct and it can access wireguard. ({e})")
    sys.exit(-1)

print("Name\tUUID")
print("__________")
for row in response_json["rows"]:
    print(row["name"] + "\t" + row["uuid"])