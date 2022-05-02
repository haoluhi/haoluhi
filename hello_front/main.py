from flask import Flask, request, render_template
import os
import random
import redis
import socket
import sys

app = Flask(__name__)

# Load configurations from environment or config file
app.config.from_pyfile('config_file.cfg')

"""
if ("VOTE1VALUE" in os.environ and os.environ['VOTE1VALUE']):
    button1 = os.environ['VOTE1VALUE']
else:
    button1 = app.config['VOTE1VALUE']

if ("VOTE2VALUE" in os.environ and os.environ['VOTE2VALUE']):
    button2 = os.environ['VOTE2VALUE']
else:
    button2 = app.config['VOTE2VALUE']

if ("TITLE" in os.environ and os.environ['TITLE']):
    title = os.environ['TITLE']
else:
    title = app.config['TITLE']
"""

# Redis configurations
"""
redis_server = os.environ['REDIS']
"""

# Redis Connection
"""
try:
    if "REDIS_PWD" in os.environ:
        r = redis.StrictRedis(host=redis_server,
                        port=6379,
                        password=os.environ['REDIS_PWD'])
    else:
        r = redis.Redis(redis_server)
    r.ping()
except redis.ConnectionError:
    exit('Failed to connect to Redis, terminating.')

# Change title to host name to demo NLB
if app.config['SHOWHOST'] == "true":
    title = socket.gethostname()
"""

# Init Redis
"""
if not r.get(button1): r.set(button1,0)
if not r.get(button2): r.set(button2,0)
"""

COUNT = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global COUNT
    if request.method == 'GET':
        COUNT = COUNT + 1
        return "Hello " + str(COUNT)

if __name__ == "__main__":
    app.run()
