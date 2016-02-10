from flask import Flask
from urlparse import urlparser
import os
import random
import ConfigParser
import redis

app = Flask(__name__)

config = ConfigParser.ConfigParser()
config.read('config.ini')

with open(config.get('Cookies', 'cookies'),'r') as f:
    cookies = f.read().split('%')
l = len(cookies)

# host = config.get('Redis','host')
# port = config.get('Redis','port')
# db = config.get('Redis','db')

redis_url = os.environ.get('REDIS_URL')
redis_url = urlparse(redis_url)

r = redis.StrictRedis(host=redis_url.hostname, port=redis_url.port,
                      db=redis_url.path[1:])

for i, cookie in enumerate(cookies):
    r.set(i, cookie.strip())

@app.route('/')
def fortune():
    return r.get(random.randrange(0,l))

if __name__ == '__main__':
        app.run(host='0.0.0.0')
