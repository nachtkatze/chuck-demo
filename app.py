from random import choice
from flask import Flask
app = Flask(__name__)

with open('cookies.cook','r') as f:
    cookies = f.read().split('%')


@app.route('/')
def fortune():
    return(choice(cookies).strip())

if __name__ == '__main__':
        app.run(host='0.0.0.0')
