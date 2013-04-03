#!ve/bin/python
from subprocess import check_output
from shlex import split

from flask import Flask

app = Flask(__name__)


@app.route('/playing/')
def playing():
    return check_output(split("osascript -e 'tell application \"Spotify\" to spotify url of current track'"))


@app.route('/position/')
def position():
    return check_output(split("osascript -e 'tell application \"Spotify\" to player position'"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
