from flask import Flask
import random
import ConfigParser
import redis

app = Flask(__name__)

config = ConfigParser.ConfigParser()
config.read('config.ini')

with open(config.get('Cookies', 'cookies'),'r') as f:
    cookies = f.read().split('%')
l = len(cookies)

r = redis.StrictRedis(host=config.get('Redis','host'),
                      port=config.get('Redis','port'),
                      db=config.get('Redis','db'))

for i, cookie in enumerate(cookies):
    r.set(i, cookie.strip())

@app.route('/')
def fortune():
    return r.get(random.randrange(0,l))

if __name__ == '__main__':
        app.run(host='0.0.0.0')
