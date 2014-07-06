#!/usr/bin/env python3
#Roseluck.py
#Irrigation controler component of Pinkie home automation
#Provides command line scheduling for drip irrigation

import pifacedigitalio
from time import sleep

#function to turn off valves, either zone 1 or zone 2 by int.
#pass 0 or nothing to turn both valves off.
def turnoff(faceoff = pifacedigitalio.PiFaceDigital(), valves = 0):
  if ((valves < 0) or (valves > 2)):
    print ("Invalid valves in turnoff function")
    return 1
  if ((valves == 1) or (valves == 0)):
    faceoff.relays[0].turn_off()
  if ((valves == 2) or (valves == 0)):
    faceoff.relays[1].turn_off()
  return 0

#function to trigger a valve for a duration
def runstation(valve, duration):
  stations = pifacedigitalio.PiFaceDigital()
  if ((0 < valve < 3) and (duration > 0)):
    print ("Activating valve " + str(valve) + " for " + str(duration) + " seconds.")
    stations.relays[valve - 1].turn_on()
    sleep(duration)
    turnoff(stations, valve)
  else:
    print ("Invalid valve or duration in runstation")
    print ("Attempted to run station " + str(valve) + " for " + str(duration) + "seconds.")
    return 1
  return 0

#function to test the system. Engage each zone for five minutes.
def systemtest():
  print ('System test:')
  print ("Triggering zone 1 for 5 minutes...")
  runstation (1, 300)
  print ("Triggering zone 2 for 5 minutes...")
  runstation (2, 300)
  print ("System test complete")
  print ("____________________")

if __name__ == "__main__":
  option = 1
  #present a basic menu
  while (option != 3):
    print ("Roseluck control menu:")
    print ("1. Test the system (each valve open for 5 minutes)")
    print ("2. Run a station for a duration")
    print ("3. Resume schedule and exit")
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
    if (option == 2):
      print("")
      inp = input("Which station would you like to run? (1, 2): ")
      try: #check for bad input again
        stat = int(inp)
      except TypeError:
        print("")
        print("Invalid selection")
        print("_________________")
        continue
      inp = input ("How many minutes would you like to run it?: ")
      try: #type check
        dur = int(inp) * 60
      except TypeError:
        print("")
        print("Invalid selectin")
        print("________________")
        continue
      runstation(stat,dur)
    elif (option == 3):
      turnoff()
      exit()
    else:
      print ("")
      print ("Invalid selection:")
      print ("__________________")
      option = 0
      continue
