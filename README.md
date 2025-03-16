# A collection of simple scripts that can help simplify the process of adding Mullvad servers (wireguard peers) to your OPNSense WireGuard service.

## How to use
**0. Assuming you have already setup the Mullvad WireGuard instance in your OPNSense router ([Setup Example](https://docs.opnsense.org/manual/how-tos/wireguard-client.html)).**
1. Download the two scripts (or clone the repo)
2. Open the first script
3. Get the API key file from OPNSense, put it in the same dir as the scripts. (You can get this file by creating a new API key from user management)
4. modify the first script's contents based on the comments, then run to get the WireGuard instance UUID
5. Open the second script
6. Extract the folder of .conf files you got from mullvad into a subfolder of the script directory.
7. Based on the comments, modify the second script, then run.
8. After some API checks, the modification overview will be shown in console. Confirm to let the script add these peers to your OPNSense WireGuard service.
9. Refresh your OPNSense WebGUI to see the newly added locations
