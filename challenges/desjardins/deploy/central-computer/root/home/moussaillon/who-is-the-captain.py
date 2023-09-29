#!/usr/bin/env python3

# Félicitation, c'est une bonne idée d'explorer les fichiers du répertoire
# d'un utilisateur. 
# 
# Congratulation, it's a good idea to explore the files in a user's home
# directory. 
# 
# FLAG-ImNotTheCaptainYet

import requests
import argparse
import time
import sys

parser = argparse.ArgumentParser(
    prog='who-is-the-captain.py',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Tells you if you\'re the captain or not!\nVous dit si vous êtes le capitaine ou pas!',
    epilog='No one will find a way to abuse this script to spray credentials, right?\nPersonne ne va abuser du script pour faire de la pulvérisation de mot de passe, right?'
)
parser.add_argument('-u', '--username', required=True)
parser.add_argument('-p', '--password', required=True)
args = parser.parse_args()

req = requests.get('http://central-computer.pirate-ship/captain.php', auth=(args.username, args.password))

if req.status_code == 401:
    print('Wrong credentials!')
    exit(1)

if args.username in req.text:
    print('You\'re the captain!')
else:
    print('You\'re not the captain...')

print('Press Enter to continue...')
while sys.stdin.read(1) != '\n':
    time.sleep(0.1)
