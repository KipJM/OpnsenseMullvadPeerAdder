# This is a simple script that can make adding Mullvad servers (wireguard peers) to your OPNSense wireguard service easier.
# How to use
**0. Assuming you have already setup the Mullvad wireguard instance in your OPNSense router.**
1. Download the two scripts (or clone the repo)
2. Open the first script
3. Get the API key file from OPNSense, put it in the same dir as the scripts.
4. modify the first script's contents based on the comments, then run to get the wireguard instance UUID
5. Open the second script
6. Extract the folder of .conf files you got from mullvad into a subfolder of the script directory.
7. Based on the comments, modify the second script, then run.
8. Auto tests and overviews will be shown for the modifications, confirm to let the script add these locations to your OPNSense wireguard service.
9. Refresh your OPNSense WebGUI to see the newly added locations!
