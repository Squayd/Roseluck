#!/usr/bin/env python3
#Roseluck.py
#Irrigation controler component of Pinkie home automation
#Provides command line scheduling for drip irrigation

import pifacedigitalio

def turnoff(faceoff: pifacedigitalio.core.PiFaceDigital, valves = 0):
  if ((valves < 0) or (valves > 2)):
    print ("Invalid valves in turnoff function")
    return 1
  if ((valves == 1) or (valves == 0)):
    faceoff.relays[0].turn_off()
  if ((valves == 2) or (valves == 0)):
    faceoff.relays[1].turn_off()
  return 0

def systemtest():
  print ('System test')

def runstation():
  print ('Run station')

if __name__ == "__main__":
  option = 1
  face = pifacedigitalio.PiFaceDigital()
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
      turnoff(face)
      exit()
    else:
      print ("")
      print ("Invalid selection:")
      print ("__________________")
      option = 0
      continue
