#!/usr/bin/env python3
#Roseluck.py
#Irrigation controler component of Pinkie home automation
#Provides command line scheduling for drip irrigation

import pifacedigitalio

def turnoff():
  print ('Turn off')

def systemtest():
  print ('System test')

def runstation():
  print ('Run station')

if __name__ == "__main__":
  option = 1
  #present a basic menu
  while (option != 3):
    print ("Roseluck control menu:")
    print ("1. Test the system (each valve open for 5 minutes)")
    print ("2. Run a station for a duration")
    print ("3. Turn system off, resume schedule, and exit")
    print ("")
    inp = input ("What would you like to do?: ")
    try: #Check for bad input
      option = int(inp)
    except TypeError:
      print ("")
      print ("Invalid selection")
      print ("_________________")
      option = 0
      continue
    if (option == 1):
      systemtest()
    elif (option == 2):
      runstation()
    elif (option == 3):
      turnoff()
      exit()
    else:
      print ("")
      print ("Invalid selection:")
      print ("__________________")
      option = 0
      continue
