#!/usr/bin/env python3
from roseluck import Roseluck
from datetime import datetime
from time import sleep

if (__name__ == "__main__"):
  rose = Roseluck()
  print (str(datetime.now()))
  rose.runstation(1,3600)
