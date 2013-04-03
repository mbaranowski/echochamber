#!ve/bin/python
import sys
from subprocess import check_output
from shlex import split
from time import sleep

import requests


def shpotify(cmd):
    return check_output(split("osascript -e 'tell application \"Spotify\" to {0}'".format(cmd)))

def play(track):
    shpotify('play track {0}'.format(track))

def sync(position):
    shpotify('set player position to {0}'.format(position))


server = sys.argv[1]
if not server.startswith('http'):
    raise ValueError("Need a scheme there, genius [{0}]".format(server))

while True:
    remote_track = requests.get(server + '/playing/').content
    my_track = shpotify("spotify url of current track")

    if remote_track != my_track:
        play(remote_track)

    remote_position = float(requests.get(server + '/position').content)
    my_position = float(shpotify("player position"))

    sync((remote_position + my_position) / 2)

    sleep(1)
