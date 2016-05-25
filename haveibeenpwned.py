# Imports
import requests
import json
from sys import argv
import time, sys
# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# Decision Prompt
yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])
# Ask for a user!
user = raw_input(bcolors.BOLD + "Please enter a username or email. \n" + bcolors.ENDC)
# Do the request
r = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/' + user)
# Check if it failed.
if r.status_code is 200:
    print bcolors.FAIL + "You have been pwned." + bcolors.ENDC
    print bcolors.OKBLUE + "Do you want a list of pwns? (y/n)" + bcolors.ENDC
    choice = raw_input().lower()
    if choice in yes:
        unload_json = r.text
        load_json = json.loads(unload_json)
        print json.dumps(load_json, indent=4, sort_keys=True)
    elif choice in no:
       exit()
    else:
       sys.stdout.write(bcolors.WARNING + "Please respond with 'yes' or 'no'\n" + bcolors.ENDC)
else:
    print bcolors.OKGREEN + "You have no records of being pwned, ;)" + bcolors.ENDC
x = 1
exit()
