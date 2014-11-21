#!/usr/bin/env python3

from flask import Flask
from flask_bootstrap import Bootstrap

def create_app(configfile=None):
  hip = Flask(__name__)
  Bootstrap(hip)
  @hip.route('/Roseluck')

  def showcontent():
    return render_template('rosepage.html')
  
  return hip

if __name__ == '__main__':
  create_app().run(host='0.0.0.0')
