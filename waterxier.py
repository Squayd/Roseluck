#!/usr/bin/env python3
import roseluck
from datetime import datetime

if (__name__ == "__main__"):
  print (str(datetime.now()));
  roseluck.runstation(2,3600)
