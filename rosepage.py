#!/usr/bin/env python3

from flask import Flask

hip = Flask(__name__)

@hip.route('/')

def hello_world():
  return 'Hello world!'

if __name__ == '__main__':
  hip.run(host='0.0.0.0')
