from flask import Flask
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

host = os.environ.get(config.get('Redis','host'))
port = os.environ.get(config.get('Redis','port'))
db = os.environ.get(config.get('Redis','db'))

print(host,port,db)
print(os.environ.get('REDIS_URL'))

# r = redis.StrictRedis(host=host, port=port, db=db)
r = redis.Redis(url=os.environ.get('REDIS_URL'))

for i, cookie in enumerate(cookies):
    r.set(i, cookie.strip())

@app.route('/')
def fortune():
    return r.get(random.randrange(0,l))

if __name__ == '__main__':
        app.run(host='0.0.0.0')
