# Attendance Scanner

import csv
import datetime as dt
from os.path import exists

members = {}
timeFormat = "%H:%M:%S"

def checkIfNewDay():
  fileExists = exists(f"attendance/{dt.date.today().isoformat()}.csv")

  if fileExists is False:
    open(f"attendance/{dt.date.today().isoformat()}.csv", "w").close() # creates file

def getAlreadySignedIn():
  with open(f"attendance/{dt.date.today().isoformat()}.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    lines = 0
    
    for row in reader: 
      members[row[0]] = row[1]
      lines += 1

def checkInUser(): 
  id = input("SWIPE: ")

  if id == "000000000": print("Stopped Scanning"), exit() # exit code

  if len(id) == 9: # validates input is OSIS number

    if id not in members: # validates no duplicates

      members[id] = dt.datetime.now().strftime("%H:%M:%S")
      
      file.write(f"{id},{dt.datetime.now().strftime(timeFormat)}\n")

      print("Successfully Scanned")

    else: print("Already Scanned")

  else: print("Invalid ID. Swipe Again.")

if __name__ == "__main__":
  
  checkIfNewDay()
  getAlreadySignedIn()

  with open(f"attendance/{dt.date.today().isoformat()}.csv", "a") as file:
    while True: 
        checkInUser()
