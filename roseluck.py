#!/usr/bin/env python3
#Roseluck.py
#Irrigation controler component of Pinkie home automation
#Provides command line scheduling for drip irrigation

from gpiozero import DigitalOutputDevice
from time import sleep
from threading import Thread

class ValveWorker(Thread):
  def __init__(self, rose, valve, duration):
    Thread.__init__(self)
    self.rose = rose
    self.valve = valve
    self.duration = duration

  def run(self):
    self.rose.turnon(self.valve)
    sleep(self.duration)
    self.rose.turnoff(self.valve)

class Roseluck:
  #gpizero uses broadcom pin numbers
  VALVE_1_PIN = 23
  VALVE_2_PIN = 24
  
  def __init__(self, v1pin = VALVE_1_PIN, v2pin = VALVE_2_PIN):
    self.valve1 = DigitalOutputDevice(v1pin)
    self.valve2 = DigitalOutputDevice(v2pin)
    self.valves = [self.valve1, self.valve2]
    self.valve1thread = None
    self.valve2thread = None
    self.threads = [self.valve1thread, self.valve2thread]

  #function to turn off valves, either zone 1 or zone 2 by int.
  #pass 0 or nothing to turn both valves off.
  def turnoff(self, valve = 0):
    if ((valve < 0) or (valve > 2)):
      print ("Invalid valves in turnoff function")
      return 1
    if ((valve == 1) or (valve == 0)):
      self.valve1.off()
    if ((valve == 2) or (valve == 0)):
      self.valve2.off()
    return 0

  #Turns on the passed valve as long as it's valid
  def turnon(self, valve):
    if (valve < 1 or valve > 2):
      print("Invalid valve in turnon function")
      return 1
    self.valves[valve-1].on()

  #function to trigger a valve for a duration
  def runstation(self, valve, duration):
    if valve < 1 or valve > 2:
      print ("Invalid valve or duration in runstation")
      print ("Attempted to run station " + str(valve) + " for " + str(duration) + "seconds.")
      return 1
    if self.threads[valve-1] is not None and self.threads[valve - 1].is_alive():
      print ("Valve " + str(valve) + " is already active.")
      return 2
    else:
      self.threads[valve-1] = ValveWorker(self, valve, duration)
      #self.threads[valve-1].daemon = True
      self.threads[valve-1].start()
    return 0

  #function to test the system. Engage each zone for five minutes.
  def systemtest(self):
    print ('System test:')
    print ("Triggering zone 1 for 5 minutes...")
    self.runstation (1, 300)
    print ("Triggering zone 2 for 5 minutes...")
    self.runstation (2, 300)
    print ("System test complete")
    print ("____________________")

if __name__ == "__main__":
  rose = Roseluck()
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
      rose.systemtest()
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
      rose.runstation(stat,dur)
    elif (option == 3):
      rose.turnoff()
      exit()
    else:
      print ("")
      print ("Invalid selection:")
      print ("__________________")
      option = 0
      continue
