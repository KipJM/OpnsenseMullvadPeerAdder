#===CHANGE=ME===#
import sys

# Relative directory to API key file. You can get this file from
# Access > Users > [a user with enought permission] > API Keys
api_file = "api_key.txt"

# IP/hostname of your opnsense router.
opnsense_host = "192.168.42.1"

# Relative directory containing all of your .conf files generated by mullvad.
conf_dir = "mullvad_confs"

# Removes the redundant "-wg-" from peer name.
prettify_name = True

#===Peer configs===#
instance_UUID = "70eb3d4f-bae6-4d01-a2f0-d47ac6c3414d" # The wireguard instance UUID, run get_uuid.py to find out what the UUID is.
keepalive_interval = 15 # Default: 25

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

print("==CONFS==")
conf_files = [path.join(conf_dir, f) for f in listdir(conf_dir) if path.isfile(path.join(conf_dir, f))]
print(f"There are {len(conf_files)} config files in {conf_dir}.")
print("== == ==")
if input("Type Y to start: ") != "Y":
    sys.exit(-1)

print("==START==")
for conf_file in conf_files:
    print(f"File: {conf_file}")

    name = path.basename(conf_file).removesuffix(".conf")
    if prettify_name:
        name = name.replace("-wg", "")

    with open(conf_file) as f:
        for line in f:
            if line.startswith("PublicKey = "):
                public_key = line.strip().removeprefix("PublicKey = ")
                continue

            if line.startswith("AllowedIPs = "):
                allowed_ips = line.strip().removeprefix("AllowedIPs = ")
                continue

            if line.startswith("Endpoint = "):
                endpoint_host = line.strip().removeprefix("Endpoint = ").split(':')[0]
                endpoint_port = line.strip().removeprefix("Endpoint = ").split(':')[1]
                continue


    print("==PEER CONFIGs==")
    print(f"name: {name}")
    print(f"public key: {public_key}")
    print(f"allowed ips: {allowed_ips}")
    print(f"endpoint host: {endpoint_host}")
    print(f"endpoint port: {endpoint_port}")
    print(f"keepalive interval: {keepalive_interval}")
    print(f"instance UUID: {instance_UUID}")
    print()

    request_json = {
        "client":
            {
                "enabled": 0,
                "name": name,
                "pubkey": public_key,
                "psk": "",
                "tunneladdress": allowed_ips,
                "serveraddress": endpoint_host,
                "serverport": endpoint_port,
                "servers": instance_UUID,
                "keepalive": str(keepalive_interval),
            }
    }

    # print(request_json)
    # API add peer
    output = session.post(f"{opnsense_api}/wireguard/client/addClient/", json = request_json, verify=False, params={"key" : public_key, "secret" : api_secret})
    print(output.content)
    print("=== === ===")
    # sys.exit(0)

print("All Done! Refresh your Opnsense dashboard!")